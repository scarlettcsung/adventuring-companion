from nicegui import ui
from core.io.character import loadable_characters, load_character
import state


class LoadCharacterDialog(ui.dialog):
    def __init__(self, on_success=None):
        super().__init__()
        self.on_success = on_success

        with self, ui.card().classes('w-80 p-4'):
            ui.label('Load Character').classes('text-xl font-bold self-center mb-2')
            self.render_content()
            ui.button('Cancel', on_click=self.close).props('flat').classes('self-center mt-2')

    def open(self):
        self.render_content.refresh()
        super().open()

    @ui.refreshable
    def render_content(self):
        # Everything inside here is cleared and redrawn when you call .refresh()
        characters = loadable_characters()
        if not characters:
            ui.label('No saves found.').classes('text-gray-400 self-center py-4')
            return

        with ui.column().classes('w-full gap-2'):
            for name, index in characters.items():
                ui.button(name, icon='person', on_click=lambda i=index: self._handle_load(i)) \
                    .props('outline').classes('w-full justify-start')

    def _handle_load(self, index):
        try:
            # 1. Load the object using your existing function
            new_char = load_character(index)

            # 2. Update the global state
            state.current_char = new_char

            ui.notify(f'Loaded {new_char.name}', type='positive')

            # 3. Callback (usually to navigate to /overview)
            if self.on_success:
                self.on_success()

            self.close()
        except Exception as e:
            ui.notify(f'Load failed: {e}', type='negative')