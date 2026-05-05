from nicegui import ui

from ui.components.spell_card import SpellCardDialog
from ui.components.spell_dialog import SpellDialog
import state


def spells_list():
    container = ui.column().classes('w-full max-w-4xl ml-8 px-4 pt-0')

    def refresh():
        list_area.clear()
        with list_area:
            if not state.current_char.spells:
                with ui.card().classes('w-full p-6 border-dashed border-2 border-slate-200 bg-slate-50 shadow-none'):
                    ui.label('Your spellbook is empty.').classes('text-slate-500 italic mx-auto')
                return

            # Group spells by level first to make grid placement easier
            spells_by_level = {}
            for spell in state.current_char.spells:
                spells_by_level.setdefault(spell.level, []).append(spell)

            # Create a 3-column grid
            with ui.element('div').classes('grid grid-cols-3 gap-6 w-full'):
                # Sort levels to ensure they appear in order 0, 1, 2...
                for lvl in sorted(spells_by_level.keys()):
                    with ui.column().classes('gap-1'):
                        # Header for each column section
                        header = "Cantrips" if lvl == 0 else f"Level {lvl}"
                        ui.label(header).classes('text-bold text-sm text-primary uppercase tracking-wider')
                        ui.separator().classes('mb-2')

                        # Sort spells alphabetically within this level
                        level_spells = sorted(spells_by_level[lvl], key=lambda s: s.name)

                        # Inside your spells_list loop:
                        for spell in level_spells:
                            # Use a closure (s=spell) to ensure the button targets the right spell
                            ui.button(spell.name, on_click=lambda s=spell: SpellCardDialog(s).open()) \
                                .props('flat no-caps') \
                                .classes('justify-start px-1 h-8 text-slate-700 hover:text-primary')

    with container:
        with ui.row().classes('w-full items-center justify-between mb-4'):
            ui.label('Known Spells').classes('text-h5')

            dialog = SpellDialog(on_success=refresh)
            ui.button(icon='add', on_click=dialog.open).props('flat round color=primary')

        list_area = ui.column().classes('w-full')
        refresh()