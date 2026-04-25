from nicegui import ui
from ui.components.bottom_tabs import bottom_tabs
from ui.components.global_header import global_header


@ui.page('/inventory')
def content():
    global_header()

    ui.label('Inventory').classes('text-h4')
    ui.label('Inventory under construction.').classes('text-h5')

    bottom_tabs()
