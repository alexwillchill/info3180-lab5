from flask_wtf import FlaskForm, FileAllowed
from wtforms import StringField, SelectField, IntegerField, FileField, PasswordField
from wtforms.validators import InputRequired
from app import db
from models import UserProfile

class LoginForm(FlaskForm):
    username= StringField('Username',validators=[InputRequired()])
    password= PasswordField('Password',validators=[InputRequired()])
    
class UserProfile(FlaskForm):
    username=StringField('Username',validators=[InputRequired()])
    firstname= StringField('Firstname',validators=[InputRequired()],description='Short')
    lastname= StringField('Lastname',validators=[InputRequired()])
    age=IntegerField('Age',validator=[InputRequired()])
    biography= StringField('Biography',validators=[InputRequired()])
    gender=SelectField('Gender',choices=[('M','Male'),('F','Female')])
    image= FileField('Image File', validator=[FileAllowed(['jpg','png'],'Image')])

      