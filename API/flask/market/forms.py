from typing import Mapping, Sequence, Any

from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User
class RegisterForm(FlaskForm):
    def validate_username(self,username_to_check):
        user=User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists! Please Try a different Username')
    def validate_email_address(self, email_to_check):
        email_address=User.query.filter_by(email_address=email_to_check.data).first()
        if email_address:
            raise ValidationError('Email already in use! Try a different email')
    username=StringField(label='username',validators=[Length(min=2,max=30), DataRequired()])
    email_address=StringField(label='email',validators=[Email(),DataRequired()])
    password1=PasswordField(label='password1',validators=[Length(min=6),DataRequired()])
    password2=PasswordField(label='passoword2',validators=[EqualTo('password1'),DataRequired()])
    submit=SubmitField(label='Create Account')

class LoginForm(FlaskForm):
    username=StringField(label='User Name:',validators=[DataRequired()])
    password=StringField(label='Password:',validators=[DataRequired()])
    submit=SubmitField(label="Sign in")

class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label='Purchase Item!')

class SellItemForm(FlaskForm):
    submit = SubmitField(label='Sell Item!')
