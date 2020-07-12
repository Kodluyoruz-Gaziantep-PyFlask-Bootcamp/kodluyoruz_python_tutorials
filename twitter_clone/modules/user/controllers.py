from flask import Blueprint, render_template, session, redirect, url_for, jsonify
from flask.views import MethodView

from libraries.app_helper import login_required
from modules.tweet.forms import TweetCreateForm

user_bp = Blueprint("user", __name__, url_prefix="/")

class UserHomeController(MethodView):
    decorators = [login_required]

    def get(self):
        form = TweetCreateForm()
        return render_template("user/home.html", form=form)



user_bp.add_url_rule("/home",view_func=UserHomeController.as_view("home"))

