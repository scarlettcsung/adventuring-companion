from nicegui import ui

from ui.components.bottom_tabs import bottom_tabs
from ui.components.global_header import global_header


@ui.page('/notes')
def content():
    global_header()

    ui.label('Notes').classes('text-h4')
    ui.label('Notes under construction.').classes('text-h5')

    bottom_tabs()
