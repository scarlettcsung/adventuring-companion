from nicegui import ui
from core.models.feature import Feature


def feature_card(f: Feature):
    """A reusable UI component to display a single character feature."""
    with ui.card().classes('w-full mb-4 bg-transparent border-2 shadow-none rounded-md'):

        with ui.row().classes('w-full items-center justify-between'):
            with ui.column().classes('gap-0'):
                ui.label(f.name).classes('text-lg font-bold')
                ui.label(f"Source: {f.source or 'Custom'}").classes('text-xs uppercase tracking-wider text-gray-500')

            with ui.row().classes('items-center gap-1'):
                ui.button(icon='edit', on_click=lambda: ui.notify('Edit coming soon!')) \
                    .props('flat round dense size=sm').classes('text-gray-400 hover:text-blue-500')

                ui.button(icon='delete', on_click=lambda: ui.notify('Delete coming soon!')) \
                    .props('flat round dense size=sm').classes('text-gray-400 hover:text-red-500')

        ui.separator()

        # Combined Counter & Dice Row
        if f.counter or f.dice:
            with ui.row().classes('w-full gap-2 justify-start'):

                # Counter Section
                if f.counter:
                    with ui.row().classes('items-center gap-3 bg-slate-50 p-2 rounded border'):
                        with ui.row().classes('items-center gap-3'):
                            with ui.row().classes('items-center gap-1'):
                                ui.label('MAX').classes('text-[10px] font-bold text-gray-400')
                                ui.label(str(int(f.counter.maximum))).classes('font-mono font-bold')
                            with ui.row().classes('items-center gap-1'):
                                ui.label('CURRENT').classes('text-[10px] font-bold text-gray-400')
                                ui.label().bind_text_from(f.counter, 'current').classes(
                                    'font-mono font-bold text-blue-600')

                        with ui.row().classes('gap-0 ml-2'):
                            ui.button(icon='remove', on_click=f.counter.minus_current).props('flat round dense size=sm')
                            ui.button(icon='add', on_click=f.counter.plus_current).props('flat round dense size=sm')

                # Dice Section
                if f.dice:
                    n, die = f.dice.to_tuple()
                    with ui.row().classes('items-center gap-2 bg-slate-50 p-2 rounded border'):
                        with ui.row().classes('items-center gap-1'):
                            ui.label('DICE').classes('text-[10px] font-bold text-gray-400')
                            ui.label(f'{n}d{die}').classes('font-mono font-bold')


        # Description Section
        if f.desc:
            with ui.column().classes('mt-1 text-sm text-gray-700'):
                for line in f.desc:
                    ui.label(line).classes('leading-tight')

