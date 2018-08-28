from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired,Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                            validators=[DataRequired(), Length(min=2,max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])                        

    password = PasswordField('PasswordField', validators=[DataRequired()])
    cornfirm_password = PasswordField('cornfirm Password',
                                        validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('sign Up')



class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])                        

    password = PasswordField('PasswordField', validators=[DataRequired()])
    remember = BooleanField('_Remember Me_')
    submit = SubmitField('_Login_')


