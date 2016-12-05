from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length  # Validator from flask-wtf
class SignupForm(Form):
	first_name = StringField('First name', validators = [DataRequired("Please enter your first name.")]) # customize error messages
	last_name = StringField('Last name', validators = [DataRequired("Please enter your last name.")] )
	email = StringField('Email', validators = [DataRequired("Please enter your email address."),Email("Please enter the correct email.")])
	password = PasswordField('Password', validators = [DataRequired("Please enter your password."), Length(min = 6, message= "Password must be 6 characters or more")])
	submit = SubmitField('Sign up', validators = [DataRequired()])