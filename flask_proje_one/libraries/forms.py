from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email, ValidationError, Length, EqualTo

from libraries.db_helper import get_db


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),Length(min=3,max=50)])
    password = StringField('Password', validators=[DataRequired(),EqualTo('password_confirm', message='Passwords must match')])
    password_confirm = StringField('Password Confirm', validators=[DataRequired()])
    full_name = StringField('Full Name', validators=[DataRequired(),Length(min=3,max=255)])

    def validate_username(form, field):
        db = get_db()
        cr = db.cursor()

        cr.execute("SELECT * FROM users WHERE username=?",(form.username.data,))
        user = cr.fetchone()
        if user:
            raise ValidationError("Zaten bu kullanıcı adında başka biri var. Farklı bir kullanıcı adı deneyiniz")


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])

    #def validate_username(form, field):
    #    if len(field.data) > 2:
    #        raise ValidationError('Name must be less than 50 characters')



class NewPostForm(FlaskForm):
    post_title   = StringField('Post Title', validators=[DataRequired(), Length(min=5,max=255)])
    post_summary = StringField('Post Summary', validators=[DataRequired()])
    post_content = StringField('Post Content', validators=[DataRequired()])


class EditPostForm(FlaskForm):
    post_title   = StringField('Post Title', validators=[DataRequired(), Length(min=5,max=255)])
    post_summary = StringField('Post Summary', validators=[DataRequired()])
    post_content = StringField('Post Content', validators=[DataRequired()])