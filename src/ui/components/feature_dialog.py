from nicegui import ui

from core.models.counter import Counter, ResetType
from core.models.dice import Dice
from core.models.feature import Feature
from state import current_char

RESET_MAP = {
    'Short Rest': ResetType.SHORT,
    'Long Rest': ResetType.LONG,
    'Dawn': ResetType.DAILY,
    'No Reset': ResetType.NONE
}

class FeatureDialog(ui.dialog):
    def __init__(self, on_success = None):
        super().__init__()
        self.on_success = on_success
        self.data = {
            'name': '', 'source': '',
            'counter_enabled': False, 'dice_enabled': False,
            'max_count': 0, 'reset_value':None,
            'n_die':None,'die_type':None,
            'reset_at': 'No Reset',
            'desc': ''
        }

        with self, ui.card().classes('w-[550px] p-6') as self.card:
            self.show_choice_view()

    def show_choice_view(self):
        """Clears the card and shows the Select/Create buttons."""
        self.card.clear()
        with self.card:
            ui.label('Add Feature').classes('text-xl font-bold self-center')

            with ui.row().classes('w-full justify-center gap-4 no-wrap'):
                ui.button('Select Existing', icon='search',
                          on_click=lambda: ui.notify('Selection logic soon!')) \
                    .props('outline no-wrap stack').classes('flex-1 h-20')

                ui.button('Create New', icon='add',
                          on_click=self.show_form_view) \
                    .props('no-wrap stack').classes('flex-1 h-20')

            ui.button('Cancel', on_click=self.close).props('flat').classes('self-center mt-4')

    def show_form_view(self):
        """Clears the card and draws your existing form logic."""
        self.card.clear()
        with self.card:
            ui.label('Create New Feature').classes('text-xl font-bold mt-2')

            with ui.row().classes('items-center'):
                ui.input('Name', on_change=lambda e: self.update_feature('name', e.value))
                ui.select(['Custom'], label='Source',
                          on_change=lambda e: self.update_feature('source', e.value)).classes('w-32')
            with ui.row().classes('items-center'):
                counter_switch = ui.switch('Counter',
                                           on_change=lambda e: self.update_feature('counter_enabled', e.value))
                dice_switch = ui.switch('Dice',
                                       on_change=lambda e: self.update_feature('dice_enabled', e.value))

            # Conditional section using bind_visibility
            with ui.column().bind_visibility_from(counter_switch, 'value'):
                ui.label('Counter').classes('text-l font-bold')
                with ui.row().classes('items-center'):
                    max_count = ui.select(['Custom'], label='Maximum Count',
                                          on_change=lambda e: self.update_feature('max_count_type', e.value)).classes(
                        'w-40')
                    ui.number('Value', value=0, format='%d',
                              on_change=lambda e: self.update_feature('max_val', e.value)) \
                        .bind_visibility_from(max_count, 'value', value='Custom') \
                        .classes('w-32')

                with ui.row().classes('items-center'):
                    ui.select(['Max', '0'], label='Value on Reset',
                              on_change=lambda e: self.update_feature('reset_value', e.value)).classes('w-40')
                    ui.select(['Short Rest', 'Long Rest', 'Dawn', 'No Reset'], label='Reset at',
                              on_change=lambda e: self.update_feature('reset_at', e.value)).classes('w-40')

            with ui.column().bind_visibility_from(dice_switch, 'value'):
                ui.label('Dice').classes('text-l font-bold')
                with ui.row().classes('items-center'):
                    ui.number('#', on_change=lambda e: self.update_feature('n_die', e.value)).classes('w-20')
                    ui.select(['4','6','8','10','12','20','100'],
                              on_change=lambda e: self.update_feature('die_type', e.value)).classes('w-20')


            ui.textarea(label='Description', placeholder='Enter feature description here...',
                        on_change=lambda e: self.update_feature('desc', e.value)) \
                .classes('w-full mt-4').props('autogrow outlined')

            # Action buttons
            with ui.row().classes('w-full justify-end mt-4'):
                ui.button('Back', on_click=self.show_choice_view).props('flat')
                ui.button('Save', on_click=self.save_data)

    def update_feature(self, key, value):
        self.data[key] = value
        print(f"Current State: {self.data}")

    def save_data(self):
        name = self.data['name'] or 'Feature'
        lines = [line.strip() for line in self.data['desc'].splitlines() if line.strip()]
        selected_reset = RESET_MAP.get(self.data['reset_at'], ResetType.NONE)

        counter = None
        if self.data['counter_enabled']:
            counter = Counter(
                maximum = self.data['max_val'],
                reset_type= selected_reset,
                start_full=(self.data['reset_value'] == 'Max')
            )

        dice = None
        if self.data['dice_enabled']:
            n = int(self.data.get('n_die')or 1)
            die = int(self.data.get('die_type') or 20)
            dice = Dice(n=n, die_type = die)

        feature = Feature(
            name = name,
            desc = lines,
            counter = counter,
            dice = dice
        )
        current_char.features.append(feature)

        if self.on_success:
            self.on_success()

        self.close()
        self.show_choice_view()