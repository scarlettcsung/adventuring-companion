from nicegui import ui

from ui.components.bottom_tabs import bottom_tabs


@ui.page('/combat')
def content():
    ui.label('Combat').classes('text-h4')
    ui.label('Combat under construction.').classes('text-h5')

    bottom_tabs()
