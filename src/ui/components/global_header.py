from nicegui import ui
from core.io import character
import state
from core.io.character import delete_character
from core.models.character import Character


def global_header():

    with ui.dialog() as delete_dialog, ui.card().classes('p-4'):
        ui.label('Are you sure you want to delete this character?').classes('text-lg')
        with ui.row().classes('w-full justify-end'):
            ui.button('Cancel', on_click=delete_dialog.close).props('flat')
            # We use state.current_char.index directly inside the lambda
            ui.button('Delete', color='red',
                      on_click=lambda: execute_delete(state.current_char.index, delete_dialog))

    with ui.header().classes('bg-white text-slate-900 border-b items-center py-2'):
        ui.label('Adventuring Companion').classes('text-2xl font-bold tracking-tight px-4')

        ui.space()
        ui.button(icon='save', on_click=perform_save) \
            .props('flat round color=primary') \
            .tooltip('Save Character (Ctrl+S)')

        # The Menu Button
        with ui.button(icon='more_vert').props('flat round color=slate-600'):
            with ui.menu().classes('w-48'):
                # Save Option
                with ui.menu_item(on_click=lambda: perform_save()):
                    with ui.row().classes('items-center gap-2'):
                        ui.icon('save', size='sm')
                        ui.label('Save Character')

                ui.separator()

                with ui.menu_item(on_click=lambda: ui.notify('Coming soon!')).classes('text-gray-400'):
                    with ui.row().classes('items-center gap-2'):
                        ui.icon('upgrade', size='sm')
                        ui.label('Level Up')

                with ui.menu_item(on_click=lambda: ui.notify('Coming soon!')).classes('text-gray-400'):
                    with ui.row().classes('items-center gap-2'):
                        ui.icon('chair', size='sm')
                        ui.label('Short Rest')

                with ui.menu_item(on_click=lambda: ui.notify('Coming soon!')).classes('text-gray-400'):
                    with ui.row().classes('items-center gap-2'):
                        ui.icon('bed', size='sm')
                        ui.label('Long Rest')

                with ui.menu_item(on_click=lambda: ui.notify('Coming soon!')).classes('text-gray-400'):
                    with ui.row().classes('items-center gap-2'):
                        ui.icon('sunny', size='sm')
                        ui.label('New Day')

                with ui.menu_item(on_click= delete_dialog.open):
                    with ui.row().classes('items-center gap-2 text-red-500'):
                        ui.icon('delete', size='sm')
                        ui.label('Delete Character')


def perform_save():
    try:
        character.save_character(state.current_char)
        ui.notify(f'Saved {state.current_char.name}!', type='positive')
    except Exception as e:
        ui.notify(f'Error saving: {e}', type='negative')

def execute_delete(index, dialog):
    try:
        delete_character(index)
        state.current_char = Character(name="New Adventurer")
        ui.notify('Character deleted successfully.', type='positive')
        dialog.close()
        ui.navigate.to('/')

    except Exception as e:
        ui.notify(f'Delete failed: {e}', type='negative')