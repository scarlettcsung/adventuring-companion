from nicegui import ui


def spell_slots_table():
    # 1. Define rows outside so we can reference the list easily
    rows = [{'level': f'Level {i}', 'max': 0, 'current': 0} for i in range(1, 10)]

    with ui.card().classes('p-0 overflow-hidden'):
        columns = [
            {'name': 'level', 'label': 'Level', 'field': 'level', 'align': 'left'},
            {'name': 'max', 'label': 'Max', 'field': 'max'},
            {'name': 'current', 'label': 'Current', 'field': 'current'},
            {'name': 'edit', 'label': '', 'field': 'edit'},
        ]

        # Use the rows variable
        table = ui.table(columns=columns, rows=rows).classes('bg-transparent')

        table.add_slot('body-cell-current', '''
            <q-td :props="props">
                <q-btn flat round size="sm" icon="remove" @click="props.row.current--" :disable="props.row.current <= 0" />
                <span class="mx-2 text-md">{{ props.row.current }}</span>
                <q-btn flat round size="sm" icon="add" @click="props.row.current++" :disable="props.row.current >= props.row.max" />
            </q-td>
        ''')

        table.add_slot('body-cell-edit', '''
            <q-td :props="props">
                <q-btn flat round size="sm" icon="edit" color="slate-400" @click="$parent.$emit('edit_max', props.row)" />
            </q-td>
        ''')

    # Local Edit Dialog logic
    with ui.dialog() as edit_dialog, ui.card().classes('p-4 w-64'):
        ui.label('Edit Max Slots').classes('text-lg font-bold')
        num_input = ui.number('Max Slots', min=0, precision=0).classes('w-full')

        # We store the index to ensure we target the right row
        context = {'row_index': -1}

        def save():
            idx = context['row_index']
            if idx != -1:
                # Update the actual data source
                table.rows[idx]['max'] = int(num_input.value)
                # Ensure 'current' doesn't exceed the new 'max'
                if table.rows[idx]['current'] > table.rows[idx]['max']:
                    table.rows[idx]['current'] = table.rows[idx]['max']

                table.update()  # Refresh the UI
            edit_dialog.close()

        with ui.row().classes('justify-end w-full mt-2'):
            ui.button('Cancel', on_click=edit_dialog.close).props('flat')
            ui.button('Save', on_click=save)

    # When the edit button is clicked
    def handle_edit(e):
        row = e.args
        # Find the index of the row by matching the level name
        for i, r in enumerate(table.rows):
            if r['level'] == row['level']:
                context['row_index'] = i
                num_input.set_value(r['max'])
                break
        edit_dialog.open()

    table.on('edit_max', handle_edit)