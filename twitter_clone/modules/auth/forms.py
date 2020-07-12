from flask import g
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired,Email,Length,EqualTo
from flask_babel import lazy_gettext as _

from models import Users


class LoginForm(FlaskForm):
    username_or_email = StringField(_('Username/Email'), validators=[DataRequired()])
    password = StringField(_('Password'), validators=[DataRequired()])


class SignupForm(FlaskForm):
    email = StringField(_('Email'), validators=[DataRequired(),Email()])
    username = StringField(_('Username'), validators=[DataRequired(),Length(min=3,max=50)])
    password = StringField(_('Password'), validators=[DataRequired(),Length(min=6),EqualTo("password_confirm")])
    password_confirm = StringField(_('Password Confirm'), validators=[DataRequired()])

    def validate_username(form,field):
        exists_user_count = (Users.select().where(Users.username == field.data).count())
        if exists_user_count > 0:
            raise ValueError(_("Already exists username"))


    def validate_email(form,field):
        exists_user_count = (Users.select().where(Users.email == field.data).count())
        if exists_user_count > 0:
            raise ValueError(_("Already exists email"))
