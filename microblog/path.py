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


@App.html(model=Root, template='template.jinja2')
def hello_world(self, request):
    """View displaying the root instance."""
    logged_in = request.identity != morepath.NO_IDENTITY
    return {
        'name': 'Morepath',
        'identity': request.identity,
        'login_link': request.link(Logout() if logged_in else LoginForm())
    }


@App.path(model=LoginForm, path='/login')
def login_path():
    """Path exposing a LoginForm instance for logging in."""
    return LoginForm()


@App.html(model=LoginForm, template='login.jinja2')
def login(self, request):
    """View displaying the form instance."""
    return {
        'form': self,
        'home_link': request.class_link(Root)
    }


@App.html(model=LoginForm, request_method='POST', template='login.jinja2')
def login_post(self, request):
    """View receiving the posted login form."""
    self.process(request.POST)
    if self.validate():
        @request.after
        def remember(response):
            identity = morepath.Identity(
                self.data['username'], password=self.data['password'])
            request.app.remember_identity(response, request, identity)

        return morepath.redirect(request.link(Root()))

    return {
        'form': self,
        'home_link': request.class_link(Root)
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
