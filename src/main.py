from nicegui import app,ui
import os

from ui.pages import *
from ui.components.bottom_tabs import bottom_tabs

@ui.page('/')
def index():
    home.content()
    bottom_tabs()

app.add_static_files('/static', 'static')

port = int(os.environ.get("PORT", 8080))

ui.run(host="0.0.0.0", port=port, reload=False)