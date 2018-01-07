"""
Form definitions

"""

from wtforms import (
    Form, StringField, PasswordField, SubmitField)
from wtforms.validators import DataRequired
from wtforms.csrf.session import SessionCSRF

from .app import user_has_password, MicroblogIdentityPolicy


class LoginForm(Form):
    class Meta:
        csrf = True
        csrf_class = SessionCSRF
        csrf_secret = MicroblogIdentityPolicy.secret

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

    def validate(self):
        result = super().validate()
        if not result:
            return False

        if not user_has_password(
                self.data['username'], self.data['password']):
            self.password.errors.append('Incorrect login or password')
            return False

        return True
