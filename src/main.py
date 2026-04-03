from nicegui import ui
from ui.pages import home, settings

@ui.page('/')
def index():
    home.content()

@ui.page('/settings')
def setup():
    settings.content()

ui.run()