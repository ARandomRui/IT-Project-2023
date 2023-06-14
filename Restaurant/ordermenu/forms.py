from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, FloatField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, InputRequired
from ordermenu.models import User, Food


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    tryna_user = StringField('Username',
                        validators=[DataRequired()]) #CHANGE THIS
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')


class RequestResetForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There is no account with that email. You must register first.')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')

class AddfoodForm(FlaskForm):
    name = StringField('Food Name',
                           validators=[DataRequired(), Length(min=1, max=40)])
    price = FloatField('Price (RM)', validators=[InputRequired()])
    picture = FileField('Add Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    description = StringField('Description')
    submit = SubmitField('Add Food')
    
    def validate_foodname(self, name):
        food = Food.query.filter_by(name=name.data).first()
        if food:
            raise ValidationError('That food name is taken. Please give it a weirder name.')
        
class UpdateFood(FlaskForm):
    name = StringField('Food Name',
                           validators=[DataRequired(), Length(min=1, max=40)])
    price = FloatField('Price (RM)')
    picture = FileField('Update Food Picture', validators=[FileAllowed(['jpg', 'png'])])
    description = StringField('Description')
    submit = SubmitField('Update')

    def validate_foodname(self, name):
        food = Food.query.filter_by(name = name.data).first()
        if food:
            raise ValidationError('That food name is taken. Please rename the food.')





