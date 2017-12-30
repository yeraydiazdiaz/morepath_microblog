from more.jinja2 import Jinja2App


class App(Jinja2App):
    pass


@App.template_directory()
def get_template_directory():
    return 'templates'
