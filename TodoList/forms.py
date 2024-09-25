from flask_wtf import FlaskForm 
from wtforms import StringField , TextAreaField , validators , SubmitField

class TaskForm(FlaskForm):
    title = StringField('Title' , validators=[validators.DataRequired()])
    task = TextAreaField('Task' , validators=[validators.DataRequired()])
    submit = SubmitField('Add')