from nicegui import app,ui
import os

from ui.pages import *
from ui.components.bottom_tabs import bottom_tabs

@ui.page('/')
def index():
    home.content()
    bottom_tabs()

current_dir = os.path.dirname(os.path.abspath(__file__))
static_dir = os.path.join(current_dir, 'static')

app.add_static_files('/static', static_dir)

port = int(os.environ.get("PORT", 8080))

ui.run(host="0.0.0.0", port=port, reload=False)