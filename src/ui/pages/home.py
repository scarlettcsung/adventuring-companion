from nicegui import ui

from ui.components.creator_choice import CreatorChoiceDialog
from ui.components.global_header import global_header


@ui.page('/')
def content():

    global_header()
    new_char_dialog = CreatorChoiceDialog()

    with ui.column().classes('absolute-center items-center gap-6 w-full max-w-sm p-4'):
        # Header Section
        with ui.column().classes('items-center gap-0'):
            ui.icon('shield', size='64px').classes('text-blue-600')
            ui.label('Adventuring Companion').classes('text-2xl font-bold tracking-tight')

        # Action Buttons
        with ui.column().classes('w-full gap-3'):
            # New Character Button
            with ui.button(on_click=lambda: new_char_dialog) \
                    .props('flat').classes(
                'w-full py-4 border-2 border-dashed border-blue-200 hover:bg-blue-50 rounded-lg group'):
                with ui.row().classes('items-center gap-3'):
                    ui.icon('add_circle').classes('text-blue-500')
                    with ui.column().classes('items-start gap-0'):
                        ui.label('New Character').classes('font-bold text-blue-900')

            # Load Character Button
            with ui.button(on_click=lambda: ui.notify('Loading Gallery...')) \
                    .props('flat').classes('w-full py-4 border-2 border-gray-200 hover:bg-gray-50 rounded-lg'):
                with ui.row().classes('items-center gap-3'):
                    ui.icon('folder_open').classes('text-gray-500')
                    with ui.column().classes('items-start gap-0'):
                        ui.label('Load Character').classes('font-bold text-gray-700')


