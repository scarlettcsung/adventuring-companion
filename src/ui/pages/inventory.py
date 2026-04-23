from nicegui import ui
from ui.components.bottom_tabs import bottom_tabs

@ui.page('/inventory')
def content():
    ui.label('Inventory').classes('text-h4')
    ui.label('Inventory under construction.').classes('text-h5')

    bottom_tabs()
