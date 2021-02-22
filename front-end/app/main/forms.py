from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class UploadForm(FlaskForm):

    title = StringField('Title', validators=[DataRequired()])
    image = TextAreaField('Image', validators=[DataRequired()])
    sumbit = SubmitField('Upload')