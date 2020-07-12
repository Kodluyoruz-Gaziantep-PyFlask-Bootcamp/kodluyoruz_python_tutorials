from flask import g
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired,Email,Length,EqualTo
from flask_babel import lazy_gettext as _

from models import Users


class TweetCreateForm(FlaskForm):
    tweet_content = StringField(_("Tweet Content"), validators=[DataRequired(),Length(max=280)])