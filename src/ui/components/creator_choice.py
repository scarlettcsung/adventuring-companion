from nicegui import ui

import state
from state import current_char
from core.models.character import Character


class CreatorChoiceDialog(ui.dialog):
    def __init__(self, on_success=None):
        super().__init__()
        self.on_success = on_success
        self.data = {'name':''}

        with self, ui.card().classes('w-[300px] p-6') as self.card:
            self.show_choice_view()

    def show_choice_view(self):
        """Clears the card and shows the Select/Create buttons."""
        self.card.clear()
        with self.card:
            ui.label('New Character').classes('text-xl font-bold self-center')

            with ui.row().classes('w-full justify-center gap-4 no-wrap'):
                ui.button('Custom', on_click= self.show_form_view) \
                    .props('outline no-wrap stack').classes('flex-1 h-10')

                ui.button('Generator',
                          on_click= lambda: ui.notify('Character generator under construction.')) \
                    .props('no-wrap stack').classes('flex-1 h-10')

            ui.button('Cancel', on_click=self.close).props('flat').classes('self-center mt-4')

    def show_form_view(self):
        """Clears the card and draws your existing form logic."""
        self.card.clear()
        with self.card:
            ui.label('Create New Character').classes('text-xl font-bold mt-2')

            with ui.row().classes('items-center'):
                ui.input('Name').bind_value(self.data, 'name')

            # Action buttons
            with ui.row().classes('w-full justify-end mt-4'):
                ui.button('Back', on_click=self.show_choice_view).props('flat')
                ui.button('Save', on_click=self.save_data)

    def update_data(self, key, value):
        self.data[key] = value
        print(f"Current State: {self.data}")

    def save_data(self):
        name = self.data['name'] or 'New Adventurer'
        state.current_char = Character(name = name)

        if self.on_success:
            self.on_success()

        self.close()
        self.show_choice_view()