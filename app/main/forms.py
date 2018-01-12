from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, IntegerField, SelectField, RadioField, StringField, PasswordField, BooleanField
from wtforms.validators import Required,Email,EqualTo
from wtforms.validators import Required


class UpdateProfile(FlaskForm):
    age = IntegerField('Age',validators = [Required()])
    status = RadioField('default field arguments', choices=[('Single', 'Single'), ('Dating', 'Dating')],validators = [Required()])
    intrested_in = SelectField('Intrested In', choices=[('Women', 'Women'),('Men','Men'),('Both','Both')],validators = [Required()])
    bio = TextAreaField('Say something about you.',validators = [Required()])
    submit = SubmitField('Submit')

class MessageForm(FlaskForm):
    message =  TextAreaField('Your Message',validators = [Required()])
    submit = SubmitField('Send')

class ProposalForm(FlaskForm):
    message =  TextAreaField('Your Message',validators = [Required()])
    submit = SubmitField('Propose')

class AcceptProposal(FlaskForm):
    proposal_results = RadioField('Accept or Reject', choices=[('Accept', 'Accept'), ('Reject', 'Reject')],validators = [Required()])
    submit = SubmitField('Submit')

class DitchPatner(FlaskForm):
    submit = SubmitField('Ditch Patner')

class RegistrationForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    username = StringField('Enter your username',validators = [Required()])
    intrested_in = SelectField('Intrested In', choices=[('Women', 'Women'),('Men','Men'),('Both','Both')],validators = [Required()])
    age = IntegerField('Age',validators = [Required()])
    password = PasswordField('Password',validators = [Required(),
    EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [Required()])
    submit = SubmitField('Sign Up')

    def validate_email(self,data_field):
            if User.query.filter_by(email =data_field.data).first():
                raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')

class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    password = PasswordField('Password',validators =[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')
