from nicegui import ui
from ui.components.bottom_tabs import bottom_tabs

@ui.page('/overview')
def content():
    ui.label('Overview').classes('text-h4')
    ui.label('Overview under construction.').classes('text-h5')

    bottom_tabs()
