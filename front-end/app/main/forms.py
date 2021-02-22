from flask_wtf import FlaskForm
from wtforms import StringField, FileField, SubmitField
from wtforms.validators import DataRequired

class UploadForm(FlaskForm):

    title = StringField('Title', validators=[DataRequired()])
    image = FileField('Image', validators=[DataRequired()])
    sumbit = SubmitField('Upload')