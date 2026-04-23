from nicegui import ui

from ui.components.bottom_tabs import bottom_tabs


@ui.page('/spellbook')
def content():
    ui.label('Spellbook').classes('text-h4')
    ui.label('Spellbook under construction.').classes('text-h5')

    bottom_tabs()
