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

        # Counter Section
        if f.counter:
            with ui.row().classes('w-full items-center justify-between bg-slate-50 p-2 rounded'):
                with ui.row().classes('items-center gap-4'):
                    # Max Display
                    with ui.row().classes('items-center gap-1'):
                        ui.label('MAX').classes('text-[10px] font-bold text-gray-400')
                        ui.label(str(f.counter.maximum)).classes('font-mono font-bold')

                    # Current Display
                    with ui.row().classes('items-center gap-1'):
                        ui.label('CURRENT').classes('text-[10px] font-bold text-gray-400')
                        # Replace your current label with this:
                        ui.label().bind_text_from(f.counter, 'current'). \
                            classes('font-mono font-bold text-blue-600')

                # Quick Action Buttons (Optional but handy)
                with ui.row().classes('gap-1'):
                    ui.button(icon='remove', on_click=f.counter.minus_current).props('flat round dense')
                    ui.button(icon='add', on_click=f.counter.plus_current).props('flat round dense')

        # Description Section
        if f.desc:
            with ui.column().classes('mt-1 text-sm text-gray-700'):
                for line in f.desc:
                    ui.label(line).classes('leading-tight')

