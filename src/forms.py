from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from .app import db

class User_register (FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('confirm_password', message='Passwords do not match')])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired()])
    submit = SubmitField('Sign Up')
    
    def validate_email(self, email):
        # email = email.query
        exist_email = db.validate_email(email.data)
        if exist_email: 
            raise ValidationError('This Email is taken')



class User_login (FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')


class New_book_author (FlaskForm):
    auth_name = StringField('Author Name', validators=[DataRequired()])
    country = StringField('Country', validators=[DataRequired()])
    title = StringField('Book Title', validators=[DataRequired()])
    year = IntegerField('Year', validators=[DataRequired()])
    language = SelectField('Language', choices=[('English', 'English'), ('French', 'French'), ('Italian', 'Italian'), ('German', 'German')], validators=[DataRequired()])
    submit = SubmitField('Submit')


class New_book (FlaskForm):
    auth_name = SelectField('Author Name', coerce=int, validators=[DataRequired()])
    title = StringField('Book Title', validators=[DataRequired()])
    year = IntegerField('Year', validators=[DataRequired()])
    language = SelectField('Language', choices=[('English', 'English'), ('French', 'French'), ('Italian', 'Italian'), ('German', 'German')], validators=[DataRequired()])
    submit = SubmitField('Submit')
    

class SearchForm(FlaskForm):
  search = StringField('search', validators=[DataRequired()])