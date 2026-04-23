from nicegui import ui

from ui.components.bottom_tabs import bottom_tabs


@ui.page('/stats')
def content():
    ui.label('Stats').classes('text-h4')
    ui.label('Stats under construction.').classes('text-h5')

    bottom_tabs()
