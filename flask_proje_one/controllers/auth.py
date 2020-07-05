from flask import Blueprint, render_template, session, redirect, url_for, jsonify
from flask_babel import gettext as _

from libraries.app_functions import hash_password
from libraries.db_helper import get_db
from libraries.exceptions import ValidationException
from libraries.forms import LoginForm, RegisterForm

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')



@auth_bp.route("/register", methods=["GET","POST"])
def register_user():
    data = {"status": "success", "error_message" : ""}

    register_form = RegisterForm()
    if register_form.is_submitted():
        if register_form.validate():
            try:
                db = get_db()
                cr = db.cursor()

                hashedPassword = hash_password(register_form.password.data)

                sql = "INSERT INTO users(username,password,full_name) VALUES(?,?,?)"
                cr.execute(sql, (register_form.username.data, hashedPassword, register_form.full_name.data))
                db.commit()

            except ValidationException as e:
                data["status"] = "error"
                data["error_message"] = str(e)
            except Exception as e:
                data["status"] = "error"
                data["error_message"] = _("Bilinmeyen bir hata oluştu")
            finally:
                if data["status"] == "error":
                    errorHtml = render_template("errors_messages.html", form=register_form, data=data)
                    data["error_message"] = errorHtml
        else:
            data["status"] = "error"
            data["error_message"] = render_template("errors_messages.html", form=register_form, data=data)

        return jsonify(data)

    return render_template("register.html",data=data,register_form=register_form)



@auth_bp.route("/login", methods=["GET","POST"])
def login():
    data = {"status" : "success", "error_message": ""}

    loginForm = LoginForm()
    if loginForm.is_submitted():
        if loginForm.validate():
            try:
                db = get_db()
                cr = db.cursor()

                hashedPassword = hash_password(loginForm.password.data)
                cr.execute("SELECT * FROM users WHERE username=? AND password=?", (loginForm.username.data, hashedPassword))
                user = cr.fetchone()

                if not user:
                    raise ValidationException(_("Lütfen bilgileri eksiksiz giriniz"))

                session["username"] = user["username"]
                session["full_name"] = user["full_name"]
                session["user_id"] = user["user_id"]

            except ValidationException as e:
                data["status"] = "error"
                data["error_message"] = str(e)
            except Exception as e:
                data["status"] = "error"
                data["error_message"] = _("Bilinmeyen bir hata oluştu")
            finally:
                if data["status"]=="error":
                    errorHtml = render_template("errors_messages.html", form=loginForm, data=data)
                    data["error_message"] = errorHtml
        else:
            data["status"] = "error"
            data["error_message"] = render_template("errors_messages.html", form=loginForm, data=data)

        return jsonify(data)

    return render_template("login.html", loginForm=loginForm, data=data)




@auth_bp.route("/logout")
def logout():
    session.pop("username", None)
    session.pop("full_name", None)
    session.pop("user_id", None)
    return redirect(url_for("website.posts"))