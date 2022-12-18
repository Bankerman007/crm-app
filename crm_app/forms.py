from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo



class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators= [DataRequired(), Email()])
    password = PasswordField('Password', validators= [DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators= [DataRequired(), EqualTo('password')])
    submit= SubmitField('Sign Up')

class LogInForm(FlaskForm):
    email = StringField('Email', validators= [DataRequired(), Email()])
    password = PasswordField('Password', validators= [DataRequired()])
    remember = BooleanField('Remember Me')
    submit= SubmitField('Login')

class NewContactForm(FlaskForm):
    name= StringField('Name', validators=[DataRequired(), Length(min=2, max=20)])
    phone= StringField('Phone', validators=[DataRequired()])
    email= StringField('Email', validators= [DataRequired(), Email()])
    notes= TextAreaField('Notes', validators= [Length(min=0, max=250)])
    submit= SubmitField('Create')

    
    




