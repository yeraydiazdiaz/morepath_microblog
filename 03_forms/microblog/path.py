"""
Path and view definitions

"""
import morepath

from .app import App
from .model import Root
from .forms import LoginForm


@App.path(model=Root, path='')
def root_path():
    """Path exposing a Root instance."""
    return Root()


def get_navbar_links(request):
    return {
        'Login': request.link(LoginForm()),
    }


@App.html(model=Root, template='template.jinja2')
def hello_world(self, request):
    """View displaying the root instance."""
    return {
        'name': 'Morepath user',
        'navbar_links': get_navbar_links(request)
    }


@App.path(model=LoginForm, path='/login')
def login_path(request):
    """Path exposing a LoginForm instance for logging in."""
    return LoginForm(request.POST)


@App.html(model=LoginForm, template='login.jinja2')
def login(self, request):
    """View displaying the form instance."""
    return {
        'form': self,
        'navbar_links': get_navbar_links(request)
    }


@App.html(model=LoginForm, request_method='POST', template='login.jinja2')
def login_post(self, request):
    """View receiving the posted login form."""
    if self.validate():
        return morepath.redirect(request.link(Root()))

    return {
        'form': self,
        'navbar_links': get_navbar_links(request)
    }


@App.path(path='/logout')
class Logout:
    pass


@App.view(model=Logout)
def logout(self, request):
    """View performing a logout."""
    @request.after
    def forget(response):
        request.app.forget_identity(response, request)

    return morepath.redirect(request.link(Root()))
