from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, FileField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import InputRequired, DataRequired
from flask_wtf.file import FileRequired
from app import db


class LoginForm(FlaskForm):
    username= StringField('Username',validators=[InputRequired()])
    password= PasswordField('Password',validators=[InputRequired()])
    
class UserProfile(FlaskForm):
    username=StringField('Username',validators=[InputRequired()])
    firstname= StringField('Firstname',validators=[InputRequired()])
    lastname= StringField('Lastname',validators=[InputRequired()])
    age=IntegerField('Age',validators=[InputRequired()])
    biography= TextAreaField('Biography',validators=[DataRequired("Enter anything you want")])
    gender=SelectField('Gender',choices=[('M','Male'),('F','Female')])
    image= FileField('Image File', validators=[FileRequired()])
    submit= SubmitField("Submit ")
      