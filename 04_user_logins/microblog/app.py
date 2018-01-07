from more.jinja2 import Jinja2App
from more.itsdangerous import IdentityPolicy


class App(Jinja2App):
    pass


class MicroblogIdentityPolicy(IdentityPolicy):
    secret = b'super-secret-impossible-to-crack'


@App.template_directory()
def get_template_directory():
    return 'templates'


@App.setting_section(section='jinja2')
def get_setting_section():
    return {
      'auto_reload': True,
    }


@App.identity_policy()
def get_identity_policy():
    # setting secure for development purposes,
    # as itsdangerous defaults to https only
    return MicroblogIdentityPolicy(secure=False)


@App.verify_identity()
def verify_identity(identity):
    return True


def user_has_password(username, password):
    return username == 'admin' and password == 'admin'
