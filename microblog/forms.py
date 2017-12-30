"""
Form definitions

"""

from wtforms import (
    Form, StringField, PasswordField, BooleanField, SubmitField)
from wtforms.validators import DataRequired

from .app import user_has_password


class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

    def validate(self):
        result = super().validate()
        if not result:
            return False

        if not user_has_password(
                self.data['username'], self.data['username']):
            self.password.errors.append('Incorrect login or password')
            return False

        return True
