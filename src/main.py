from nicegui import app,ui

from ui.pages import *
from ui.components.bottom_tabs import bottom_tabs

@ui.page('/')
def index():
    home.content()
    bottom_tabs()

app.add_static_files('/static', 'static')

ui.run()