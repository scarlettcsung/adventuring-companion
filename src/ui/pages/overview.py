from nicegui import ui
from ui.components.bottom_tabs import bottom_tabs
import state
from ui.components.global_header import global_header


@ui.page('/overview')
def content():
    global_header()

    ui.label('Overview').classes('text-h4')
    ui.label(f'Character: {state.current_char.name}').classes('text-h5')
    ui.label('Overview under construction.').classes('text-h5')

    bottom_tabs()
