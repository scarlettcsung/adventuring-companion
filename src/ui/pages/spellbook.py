from nicegui import ui

from ui.components.bottom_tabs import bottom_tabs
from ui.components.global_header import global_header


@ui.page('/spellbook')
def content():
    global_header()

    ui.label('Spellbook').classes('text-h4')
    ui.label('Spellbook under construction.').classes('text-h5')

    bottom_tabs()
