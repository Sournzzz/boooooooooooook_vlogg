from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class BaseBookForm(FlaskForm):
    titlebook = StringField('Title', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])

class BookSearchForm(BaseBookForm): 
    submit = SubmitField("Search")
     

class BookAddForm(BaseBookForm): 
    submit = SubmitField("Search") 
