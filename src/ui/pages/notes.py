from nicegui import ui

from ui.components.bottom_tabs import bottom_tabs


@ui.page('/notes')
def content():
    ui.label('Notes').classes('text-h4')
    ui.label('Notes under construction.').classes('text-h5')

    bottom_tabs()
