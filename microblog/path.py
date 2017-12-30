"""
Path and view definitions

"""
from .app import App
from .model import Root
from .forms import LoginForm


@App.path(model=Root, path='')
def root_path(self):
    """Path exposing a Root instance."""
    return Root()


@App.html(model=Root, template='template.jinja2')
def hello_world(self, request):
    """View displaying the root instance."""
    return {
        'name': 'Morepath',
        'login_link': request.class_link(LoginForm)
    }


@App.path(model=LoginForm, path='/login')
def login_path(self):
    """Path exposing a LoginForm instance for logging in."""
    return LoginForm()


@App.html(model=LoginForm, template='login.jinja2')
def login(self, request):
    """View displaying the form instance."""
    return {
        'form': self,
        'home_link': request.class_link(Root)
    }
