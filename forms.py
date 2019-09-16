import time
import redis
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField
from wtforms.validators import DataRequired, Length

class TodoAddForm(FlaskForm):
    label = StringField('todolabel', validators=[DataRequired(), Length(min=2, max=40)])
    completed = 'false'
    submit = SubmitField('Add')

class TodoRemoveForm(FlaskForm):
    value = StringField('todolabel', validators=[DataRequired(), Length(min=2, max=40)])
    submit = SubmitField('x')
