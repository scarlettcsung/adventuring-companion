from nicegui import ui

from state import current_char
from ui.components.feature_card import feature_card
from ui.components.feature_dialog import FeatureDialog
from ui.components.bottom_tabs import bottom_tabs

@ui.page('/features')
def content():

    with ui.column().classes('w-full max-w-2xl ml-8 p-4 p-24'):
        ui.label('Features').classes('text-2xl mb-4 font-bold')
        container = ui.column().classes('w-full')

        def refresh():
            container.clear()
            with container:
                if not current_char.features:
                    ui.label('No features yet.').classes('text-gray-400 italic mt-4')
                else:
                    for feature in current_char.features:
                        feature_card(feature)

        refresh()
        dialog = FeatureDialog(on_success=refresh)

        ui.button(icon='add', on_click=dialog.open) \
            .props('round size=lg').classes('fixed bottom-24 right-8 shadow-lg')


    bottom_tabs()