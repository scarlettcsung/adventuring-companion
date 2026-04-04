from nicegui import ui
from ui.pages import home

@ui.page('/')
def index():
    home.content()

ui.run()