from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired


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
    
