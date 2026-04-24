from nicegui import ui
from core.io import character
from state import current_char


def global_header():
    with ui.header().classes('bg-white text-slate-900 border-b justify-end items-center py-2'):

        # The Menu Button
        with ui.button(icon='more_vert').props('flat round color=slate-600'):
            with ui.menu().classes('w-48'):
                # Save Option
                with ui.menu_item(on_click=lambda: perform_save()):
                    with ui.row().classes('items-center gap-2'):
                        ui.icon('save', size='sm')
                        ui.label('Save Character')

                ui.separator()

                with ui.menu_item(on_click=lambda: current_char.level_up()):
                    with ui.row().classes('items-center gap-2'):
                        ui.icon('upgrade', size='sm')  # Good for "Short Rest"
                        ui.label('Level Up')

                with ui.menu_item(on_click=lambda: ui.notify('Coming soon!')):
                    with ui.row().classes('items-center gap-2'):
                        ui.icon('chair', size='sm')
                        ui.label('Short Rest')

                with ui.menu_item(on_click=lambda: ui.notify('Coming soon!')):
                    with ui.row().classes('items-center gap-2'):
                        ui.icon('bed', size='sm')
                        ui.label('Long Rest')

                with ui.menu_item(on_click=lambda: ui.notify('Coming soon!')):
                    with ui.row().classes('items-center gap-2'):
                        ui.icon('sunny', size='sm')
                        ui.label('New Day')

                with ui.menu_item(on_click=lambda: ui.notify('Coming soon!')):
                    with ui.row().classes('items-center gap-2 text-red-500'):
                        ui.icon('delete', size='sm')
                        ui.label('Delete')


def perform_save():
    try:
        character.save_character(current_char)
        ui.notify(f'Saved {current_char.name}!', type='positive')
    except Exception as e:
        ui.notify(f'Error saving: {e}', type='negative')