from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email
from application.access_code_model import AccessCode

class GenerateAccessCode(FlaskForm):
    myChoices = [('Admin', 'Admin'), ('Instructor','Instructor'), ('Student','Student')]
    user_type = SelectField('User Type', choices = myChoices, validators=[DataRequired()], coerce=str)
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Generate')

    def validate_email(self, email):
        user = AccessCode.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address, we already sent access code for this email..')