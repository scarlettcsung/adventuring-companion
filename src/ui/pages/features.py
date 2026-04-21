from nicegui import ui
from ui.components.feature_dialog import FeatureDialog
from ui.components.bottom_tabs import bottom_tabs

@ui.page('/features')
def content():
    with ui.column().classes('w-full p-4'):
        ui.label('Features').classes('text-2xl')

        container = ui.column()

        def refresh():
            container.clear()
            with container:
                ui.notify("Refreshing list!")

        dialog = FeatureDialog(on_success=refresh)
        ui.button('Add Feature', on_click=dialog.open)

    bottom_tabs()