from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, EmailField
from wtforms.validators import DataRequired, Email, Length


class UserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=1, max=50)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=1, max=100)])
    email = EmailField('Email', validators=[DataRequired(), Email(), Length(min=1, max=100)])
