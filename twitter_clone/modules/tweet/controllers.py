from datetime import datetime

from flask import Blueprint, render_template, session, redirect, url_for, jsonify
from flask.views import MethodView
from flask_babel import gettext as _

from libraries.app_helper import login_required
from models import Tweets
from modules.tweet.forms import TweetCreateForm

tweet_bp = Blueprint("tweet", __name__, url_prefix="/tweet")

class TweetController(MethodView):
    decorators = [login_required]

    def get(self):
        pass


    def post(self):
        data = {"status": "success", "error_message": ""}
        form = TweetCreateForm()

        if form.validate():
            try:
                print(session["user_id"])
                tweet = Tweets(
                    tweet_content = form.tweet_content.data,
                    user = session["user_id"],
                    tweet_date = datetime.now(),
                )
                tweet.save()

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



tweet_bp.add_url_rule("/", view_func=TweetController.as_view("tweet"))