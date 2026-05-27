from nicegui import ui
from ui.components.bottom_tabs import bottom_tabs
from ui.components.global_header import global_header
from ui.components.spell_slots_table import spell_slots_table
from ui.components.spells_list import spells_list


@ui.page('/spellbook')
def content():
    ui.context.client.on_connect(lambda _: spell_slots_table.refresh())

    global_header()

    with ui.column().classes('w-full p-4 gap-6'):
        ui.label('Spellbook').classes('text-h4 font-bold')

        with ui.row().classes('w-full items-start no-wrap'):
            # Left Component
            spell_slots_table()

            # Right Component
            spells_list()

    bottom_tabs()