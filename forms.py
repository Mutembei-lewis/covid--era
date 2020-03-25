
from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators  import DataRequired, Email,EqualTo
from wtforms import ValidationError

class Login(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password  = PasswordField("Password ", validators=[DataRequired()])
    submit  = SubmitField("Login")

class RegistrationForm( FlaskForm):
        email = StringField('Email', validators=[DataRequired(), Email()])
        username = StringField('username', validators=[DataRequired()])
        password  = PasswordField('password', validators=[DataRequired(), EqualTo("pass_confirm", message="passwords must match")])
        pass_confirm = PasswordField('Confrim Password', validators=[DataRequired()])
        submit = SubmitField( 'Register')
    
        def Check_Email(self,field):
            if User.query.filter_by( email = field.data).first():
                raise ValidationError("Your email is already used please try using another password or go to the login page ")

        def check_username(self,field):
            if User.query.filter_by(username = field.data).first():
                raise ValidationError("The username has been picked select another one")


