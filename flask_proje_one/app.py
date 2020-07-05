from flask import Flask, g, render_template, request, session, redirect, url_for
from flask_babel import Babel

from controllers.api import api_bp
from libraries.db_helper import get_db
from controllers.auth import auth_bp
from controllers.admin import admin_bp
from controllers.website import website_bp, ShowUsers
from libraries.exceptions import TestErrorException

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/' #same  as = app.config["SECRET_KEY"] = b'_5#y2L"F4Q8z\n\xec]/'
app.config['TESTING'] = True
app.config["BABEL_DEFAULT_LOCALE"] = "tr"

babel = Babel(app)

@app.teardown_appcontext
def close_connection(exception):
    print("close_connection")
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@babel.localeselector
def language_detector():
    return session["lang"] if "lang" in session else "tr"
    #return request.accept_languages.best_match(["tr",'de', 'fr', 'en'])


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


@app.errorhandler(TestErrorException)
def page_not_found(error):
    return "hopppp kardeşim noluyor ne işin var burda. burayı sadece ben biliyorum sen nerden buldun"


@app.route('/hello_world')
def hello_world():
    raise TestErrorException("kasdhfkashdjkfasd")
    return 'Hello World!'

@app.route("/change_lang")
def change_lang():
    lang = request.args.get("lang")
    if lang not in ["tr","en","de"]:
        lang = "tr"

    session["lang"] = lang
    return redirect(url_for("website.posts"))


app.register_blueprint(auth_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(website_bp)
app.register_blueprint(api_bp)

if __name__ == '__main__':
    app.run() # app.run(host="192.168.0.21")
