from nicegui import ui

from ui.components.bottom_tabs import bottom_tabs
from ui.components.global_header import global_header


# For the tables and such

@ui.page('/levelling')
def content():
    global_header()

    ui.label('Levelling').classes('text-h4')
    ui.label('Levelling under construction.').classes('text-h5')

    bottom_tabs()
