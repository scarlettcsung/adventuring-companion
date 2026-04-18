from nicegui import ui
from ui.pages import home, features
from ui.components.bottom_tabs import bottom_tabs

@ui.page('/')
def index():
    home.content()
    bottom_tabs()

ui.run()