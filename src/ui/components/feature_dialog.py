from nicegui import ui

class FeatureDialog(ui.dialog):
    def __init__(self):
        super().__init__()
        # Internal state for this specific dialog instance
        self.data = {
            'name': '', 'source': '', 'counter_enabled': False,
            'max_count_type': '', 'custom_val': 0,
            'reset_value': '', 'reset_at': '', 'desc': ''
        }

        with self, ui.card().classes('w-[500px]'):
            ui.label('Add Feature').classes('text-xl font-bold mt-2')

            with ui.row().classes('items-center'):
                ui.input('Name', on_change=lambda e: self.update_feature('name', e.value))
                ui.select(['Custom'], label='Source',
                          on_change=lambda e: self.update_feature('source', e.value)).classes('w-32')
                counter_switch = ui.switch('Counter',
                                           on_change=lambda e: self.update_feature('counter_enabled', e.value))

            # The conditional section
            with ui.column().bind_visibility_from(counter_switch, 'value'):
                with ui.row().classes('items-center'):
                    max_count = ui.select(['Custom'], label='Maximum Count',
                                          on_change=lambda e: self.update_feature('max_count_type', e.value)).classes('w-40')
                    ui.number('Value', value=0, format='%d',
                              on_change=lambda e: self.update_feature('custom_val', e.value)) \
                        .bind_visibility_from(max_count, 'value', value='Custom') \
                        .classes('w-32')

                with ui.row().classes('items-center'):
                    ui.select(['Max','0'], label='Value on Reset',
                              on_change=lambda e: self.update_feature('reset_value', e.value)).classes('w-40')
                    ui.select(['Short Rest','Long Rest','Dawn'], label='Reset at',
                              on_change=lambda e: self.update_feature('reset_at', e.value)).classes('w-40')

            ui.textarea(label='Description', placeholder='Enter feature description here...',
                        on_change=lambda e: self.update_feature('desc', e.value)) \
                .classes('w-full mt-4') \
                .props('autogrow outlined')

            # Action buttons for the dialog
            with ui.row().classes('w-full justify-end mt-4'):
                ui.button('Cancel', on_click=self.close).props('flat')
                ui.button('Save', on_click=self.save_data)

    def update_feature(self, key, value):
        self.data[key] = value
        print(f"Current State: {self.data}")

    def save_data(self):
        # Handle the finished data here
        ui.notify(f"Saved: {self.data['name']}")
        self.close()
