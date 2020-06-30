from flask import Blueprint,g,request,render_template,session,redirect,url_for
from db_helper import get_db

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.route("/login", methods=["GET","POST"])
def login():
    error_message = ""

    if request.method=="POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            error_message = "Lütfen bilgileri eksiksiz giriniz"
        else:
            db = get_db()
            cr = db.cursor()
            cr.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
            user = cr.fetchone()

            if not user:
                error_message = "Lütfen bilgileri eksiksiz giriniz"
            else:
                session["username"] = user["username"]
                session["full_name"] = user["full_name"]
                session["user_id"] = user["user_id"]
                return redirect(url_for("admin.dashboard"))

    return render_template("login.html",error_message=error_message)




@auth_bp.route("/logout")
def logout():
    session.pop("username", None)
    session.pop("full_name", None)
    session.pop("user_id", None)
    return redirect(url_for("posts"))