from nicegui import ui

from ui.components.bottom_tabs import bottom_tabs

# For the tables and such

@ui.page('/levelling')
def content():
    ui.label('Levelling').classes('text-h4')
    ui.label('Levelling under construction.').classes('text-h5')

    bottom_tabs()
