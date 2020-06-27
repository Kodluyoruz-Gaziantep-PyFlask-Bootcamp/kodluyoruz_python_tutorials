from flask import (render_template,request,redirect,url_for,session,g,current_app,
    Blueprint)



bp = Blueprint('auth', __name__, url_prefix='/auth') # template_folder='templates' | static_folder='static'


@bp.route("/kayit_ol", methods=["GET","POST"])
#@app.route("/auth/kayit_ol", methods=["GET","POST"])
def kayit_ol():
    return "kayit ol"

@bp.route('/login',methods=["GET","POST"])
def login():

    # abort(401)
    error = None
    if request.method == 'POST':
        if request.form['username']=="serkan" and request.form['password']=="123":
            #return "Giriş Başarılı"
            session["username"] = request.form["username"]

            return redirect(url_for('anasayfa'))
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('auth/login.html', error=error)




@bp.route("/cikis")
def cikis():
    session.pop("username", None)
    return redirect(url_for("auth.login"))

