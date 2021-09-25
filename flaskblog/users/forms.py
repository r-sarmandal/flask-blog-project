from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from flaskblog.models import User_table


class RegistrationForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired(),
                                                Length(min=3,max=15)])
    email = StringField("Email",
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',validators=[DataRequired(),
                                                    Length(min=5)])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(),
                                                 Length(min=5),
                                     EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self,username):

        user = User_table.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already taken. Please choose another username.')

    def validate_email(self, email):

            user = User_table.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('An account using this email ID already exists.')

class LoginForm(FlaskForm):

    email = StringField("Email ID",
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',validators=[DataRequired(),
                                                    Length(min=5)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired(),
                                                Length(min=3,max=15)])
    email = StringField("Email",
                        validators=[DataRequired(), Email()])

    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Update')

    def validate_username(self,username):

        if username.data != current_user.username:
         user = User_table.query.filter_by(username=username.data).first()
         if user:
            raise ValidationError('Username already taken. Please choose another username.')

    def validate_email(self, email):
            if email.data != current_user.email:
             user = User_table.query.filter_by(email=email.data).first()
             if user:
                raise ValidationError('An account using this email ID already exists.')


class RequestResetForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):

            user = User_table.query.filter_by(email=email.data).first()
            if user is None:
                raise ValidationError('There is no account with this email id.')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired(),
                                                     Length(min=5)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), Length(min=5), EqualTo('password')])
    submit = SubmitField('Reset Password')


