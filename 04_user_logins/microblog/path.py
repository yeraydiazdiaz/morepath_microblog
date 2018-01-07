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
    if request.identity == morepath.NO_IDENTITY:
        return {
            'Login': request.class_link(LoginForm),
        }
    else:
        return {
            'Logout': request.class_link(Logout),
        }


@App.html(model=Root, template='template.jinja2')
def hello_world(self, request):
    """View displaying the root instance."""
    return {
        'identity': request.identity,
        'navbar_links': get_navbar_links(request)
    }


@App.path(model=LoginForm, path='/login')
def login_path(request):
    """Path exposing a LoginForm instance for logging in."""
    return LoginForm(request.POST, meta={'csrf_context': request.cookies})


@App.html(model=LoginForm, template='login.jinja2')
def login(self, request):
    """View displaying the form instance."""
    request.app.csrf_token = request.cookies['csrf']

    @request.after
    def remember_csrf(response):
        response.set_cookie('csrf', request.app.csrf_token)

    return {
        'form': self,
        'navbar_links': get_navbar_links(request)
    }


@App.html(model=LoginForm, request_method='POST', template='login.jinja2')
def login_post(self, request):
    """View receiving the posted login form."""
    if self.validate():
        @request.after
        def remember(response):
            identity = morepath.Identity(
                self.data['username'], password=self.data['password'])
            request.app.remember_identity(response, request, identity)

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
