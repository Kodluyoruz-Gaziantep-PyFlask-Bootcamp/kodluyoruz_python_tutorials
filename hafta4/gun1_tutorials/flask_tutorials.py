from flask import (Flask,render_template,request,redirect,url_for,session,g,current_app,
    Blueprint)
import functools
from auth import bp as authbp



app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'




def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if "username" not in session:
            return "Lütfen giriş yapınız"

        # if g.user is None:
        #     return redirect(url_for('auth.login'))

        return view(**kwargs)
    return wrapped_view





@app.route('/')
def hello_world():
    #print(dir(g))
    print(dir(current_app))
    return '<b>Hello, World!</b>'


@app.route('/test')
def test():
    return "a=%s | b=%s"% ( request.args["a"], request.args["b"] )
    # print(dir(request))
    # return "Test"

@app.route('/veriler')
def veriler():
    return "Gösterilen sayfa = %s" % request.args.get("sayfa",1)


@app.route('/makale/<int:makale_id>')
def makale_goster(makale_id):
    return "Makale id = %s" % makale_id


# @app.route('/pathtest/<path:subpath>')
# def show_subpath(subpath):
#     # show the subpath after /path/
#     return 'Subpath %s' % escape(subpath)


@app.route("/anasayfa")
@login_required
def anasayfa():
    return render_template("anasayfa.html", username="<b>"+session["username"] + "</b>")
    # return "Ana sayfadasınız = %s" % session["username"]



@app.route("/template_test1/<degisken>")
def asdfasdf():
	pass

@app.route("/template_test/<degisken>")
def template_test(degisken):
    return render_template("test.html",degisken=degisken)


#@app.route("/manuel_route")
def manuel_route():
	return "Manuel route"


# @app.before_request
# @app.after_request
# @app.teardown_request

# @app.errorhandler(500)
# def internal_error(error):
#     return render_template('500.html'), 500


@app.teardown_appcontext
def teardown_appcontext(exception):
    print("teardown_appcontext")


app.add_url_rule("/manuel_route","manuel_route",manuel_route)
app.register_blueprint(authbp)


if __name__=="__main__":
	app.run(host="0.0.0.0", port="8888", debug=True)


