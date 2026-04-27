from nicegui import ui

from ui.components.bottom_tabs import bottom_tabs
from ui.components.global_header import global_header


@ui.page('/brewery')
def content():
    global_header()

    ui.label('Brewery').classes('text-h4')
    ui.label('Brewery under construction.').classes('text-h5')

    bottom_tabs()
