from nicegui import ui
from ui.components.feature_dialog import FeatureDialog

@ui.page('/features')
def features():
    add_dialog = FeatureDialog()
    ui.button('Add New Feature', on_click=add_dialog.open)
