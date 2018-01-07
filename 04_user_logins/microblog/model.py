"""
Models definitions

"""

from .forms import LoginForm

__all__ = ('Root', 'LoginForm')


class Root(object):
    """A dummy model to expose."""
    pass
