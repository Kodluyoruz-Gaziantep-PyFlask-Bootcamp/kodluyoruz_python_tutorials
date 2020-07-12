from datetime import datetime

from flask import Flask, g
from flask_babel import Babel
from peewee import MySQLDatabase, Model

from config import DevelopmentConfig, ServerConfig
from models import database, Users
from modules.public.controllers import public_bd
from modules.auth.controllers import auth_bp
from modules.user.controllers import user_bp
from modules.tweet.controllers import tweet_bp

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
#app.config.from_object(ServerConfig)


babel = Babel(app) # init babel

@app.route('/test_db')
def test_db():
    conn = database.connect()
    user = Users(create_date=datetime.now(),email="serkandaglioglu@gmail.com",first_name="Serkan",
                 surname="Dağlıoğlu",password="akjsdkaf", follower_count=0,following_count=0,
                 username="serkandaglioglu")
    user.save()
    database.close()
    return 'Hello World!'



@app.before_request
def app_before_request():
    g.db = database
    g.db.connect()

@app.teardown_appcontext
def app_teardown_appcontext(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()


app.register_blueprint(public_bd)
app.register_blueprint(auth_bp)
app.register_blueprint(user_bp)
app.register_blueprint(tweet_bp)
if __name__ == '__main__':
    app.run()
