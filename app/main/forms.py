from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, IntegerField, SelectField, RadioField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    age = IntegerField('Age',validators = [Required()])
    status = RadioField('default field arguments', choices=[('Single', 'Single'), ('Dating', 'Dating')],validators = [Required()])
    intrested_in = SelectField('Intrested In', choices=[('Women', 'Women'),('Men','Men'),('Both','Both')],validators = [Required()])
    bio = TextAreaField('Say something about you.',validators = [Required()])
    submit = SubmitField('Submit')   