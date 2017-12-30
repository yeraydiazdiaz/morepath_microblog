"""
Path and view definitions

"""
from .app import App
from .model import Root


@App.path(model=Root, path='')
def root_path(self):
    """Path exposing a Root instance."""
    return Root()


@App.view(model=Root)
def hello_world(self, request):
    """View displaying the root instance."""
    return "Hello world!"
