from datetime import datetime

from flask import Blueprint, render_template, session, redirect, url_for, jsonify
from flask.views import MethodView
from flask_babel import gettext as _

from libraries.app_helper import hash_password
from libraries.exceptions import ValidationException
from models import Users
from modules.auth.forms import LoginForm, SignupForm

auth_bp = Blueprint("auth", __name__, url_prefix="/")

class LoginController(MethodView):

    def get(self):
        form = LoginForm()
        return render_template("auth/login.html", form=form)

    def post(self):
        data = {"status" : "success", "error_message": ""}
        form = LoginForm()

        if form.validate():
            try:
                password = hash_password(form.password.data)
                query = (Users
                        .select()
                        .where(
                            (
                                    (Users.username == form.username_or_email.data) |
                                    (Users.email == form.username_or_email.data)
                            ),
                            (Users.password == password)
                        )
                    )

                # print(query.sql())
                user = query.get()

                session["user_id"] = user.user_id
                session["username"] = user.username
                session["full_name"] = user.full_name

            except Users.DoesNotExist as e:
                data["status"] = "error"
                data["error_message"] = _("Username/Email or password wrong")
            except ValidationException as e:
                data["status"] = "error"
                data["error_message"] = str(e)
            finally:
                if data["status"] == "error":
                    data["error_message"] = render_template("errors/ajax_errors.html", form=form, data=data)
        else:
            data["status"] = "error"
            data["error_message"] = render_template("errors/ajax_errors.html", form=form, data=data)

        return jsonify(data)

class SignupController(MethodView):

    def get(self):
        form = SignupForm()
        return render_template("auth/signup.html", form=form)

    def post(self):
        data = {"status" : "success", "error_message": ""}

        form = SignupForm()
        if form.validate():
            try:
                user = Users(
                    email=form.email.data,
                    username=form.username.data,
                    password=hash_password(form.password.data),
                    first_name=form.username.data,
                    surname="",
                    create_date=datetime.now()
                )
                user.save()
            except Exception as e:
                data["status"] = "error"
                data["error_message"] = _("Unknown error occured")
                print(e)
            finally:
                if data["status"] == "error":
                    data["error_message"] = render_template("errors/ajax_errors.html", form=form, data=data)
        else:
            data["status"] = "error"
            data["error_message"] = render_template("errors/ajax_errors.html", form=form, data=data)

        return jsonify(data)

auth_bp.add_url_rule("/login",view_func=LoginController.as_view("login"))
auth_bp.add_url_rule("/signup",view_func=SignupController.as_view("signup"))