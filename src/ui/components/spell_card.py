from nicegui import ui
from core.models.spell import Spell


class SpellCardDialog(ui.dialog):
    def __init__(self, spell: Spell):
        super().__init__()
        self.spell = spell

        with self, ui.card().classes('w-[500px] p-0 overflow-hidden'):
            # --- Header Section (Colored background for flair) ---
            with ui.row().classes('w-full bg-slate-50 p-4 justify-between items-start border-b'):
                with ui.column().classes('gap-0'):
                    ui.label(spell.name).classes('text-2xl font-bold text-slate-800')
                    lvl_text = "Cantrip" if spell.level == 0 else f"Level {spell.level}"
                    ui.label(f"{lvl_text} • {spell.school}").classes(
                        'text-xs uppercase tracking-widest text-slate-500 font-medium')

                with ui.row().classes('items-center gap-1'):
                    ui.button(icon='edit', on_click=lambda: ui.notify('Edit feature to come')) \
                        .props('flat round dense size=sm').classes('text-slate-400 hover:text-blue-500')
                    ui.button(icon='close', on_click=self.close) \
                        .props('flat round dense size=sm').classes('text-slate-400')

            # --- Content Section ---
            with ui.column().classes('w-full p-6 gap-4'):

                # Metadata Grid
                with ui.row().classes('w-full justify-between pb-2'):
                    self._meta_item('CASTING TIME', spell.cast_time)
                    self._meta_item('RANGE', spell.range)
                    self._meta_item('DURATION', spell.duration)

                # Tags & Damage Row
                if spell.is_ritual or spell.is_concentration or spell.damage_dice:
                    with ui.row().classes('items-center gap-2'):
                        if spell.is_concentration:
                            ui.badge('CONCENTRATION', color='amber-8').props('outline').classes('text-[10px]')
                        if spell.is_ritual:
                            ui.badge('RITUAL', color='blue-8').props('outline').classes('text-[10px]')
                        if spell.damage_dice:
                            with ui.row().classes(
                                    'items-center gap-2 bg-red-50 px-2 py-1 rounded border border-red-100'):
                                ui.label('DMG').classes('text-[10px] font-bold text-red-400')
                                ui.label(f"{spell.damage_dice} {spell.damage_type or ''}") \
                                    .classes('font-mono font-bold text-red-700 text-xs')

                # Description Area
                ui.label('DESCRIPTION').classes('text-[10px] font-bold text-gray-400 mt-2')
                with ui.scroll_area().classes('h-64 border rounded-md p-4 bg-white'):
                    # Handle both list and string descriptions
                    desc_text = spell.desc if isinstance(spell.desc, str) else "\n".join(spell.desc)
                    for paragraph in desc_text.split('\n'):
                        if paragraph.strip():
                            ui.label(paragraph.strip()).classes('text-sm text-gray-700 mb-3 leading-relaxed')

    def _meta_item(self, label, value):
        """Internal helper for metadata layout."""
        with ui.column().classes('gap-0'):
            ui.label(label).classes('text-[10px] font-bold text-gray-400 tracking-tighter')
            ui.label(value).classes('text-sm font-medium text-slate-700')