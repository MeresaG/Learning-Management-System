from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class AccessCodeForm(FlaskForm):
    access_code = StringField('Access Code', validators= [ DataRequired(), Length(10)])
    submit = SubmitField('Submit')