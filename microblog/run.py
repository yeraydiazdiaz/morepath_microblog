import morepath

from microblog.app import App


def run():
    morepath.autoscan()
    App.commit()
    morepath.run(App())


if __name__ == '__main__':
    run()
