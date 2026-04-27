from nicegui import ui
from ui.components.bottom_tabs import bottom_tabs
from ui.components.global_header import global_header


@ui.page('/spellbook')
def content():
    global_header()

    with ui.column().classes('w-full p-4 gap-6'):
        ui.label('Spellbook').classes('text-h4 font-bold')

        # Main Layout Container
        with ui.row().classes('w-full items-start gap-8'):
            # --- Left Side: Spell Slots Table ---
            with ui.card().classes('p-0 overflow-hidden'):
                with ui.table(columns=[
                    {'name': 'level', 'label': 'Level', 'field': 'level', 'align': 'left'},
                    {'name': 'max', 'label': 'Max', 'field': 'max'},
                    {'name': 'current', 'label': 'Current', 'field': 'current'},
                    {'name': 'edit', 'label': '', 'field': 'edit'},
                ], rows=[
                    {'level': f'Level {i}', 'max': 0, 'current': 0} for i in range(1, 10)
                ]).classes('bg-transparent') as table:
                    # Customizing the 'current' column to be a counter
                    table.add_slot('body-cell-current', '''
                        <q-td :props="props">
                            <q-btn flat round size="sm" icon="remove" @click="props.row.current--" :disable="props.row.current <= 0" />
                            <span class="mx-2 text-md">{{ props.row.current }}</span>
                            <q-btn flat round size="sm" icon="add" @click="props.row.current++" :disable="props.row.current >= props.row.max" />
                        </q-td>
                    ''')

                    # Customizing the 'edit' column for the Max Slot dialog
                    table.add_slot('body-cell-edit', '''
                        <q-td :props="props">
                            <q-btn flat round size="sm" icon="edit" color="slate-400" @click="$parent.$emit('edit_max', props.row)" />
                        </q-td>
                    ''')

            # --- Right Side: Placeholder for Spells ---
            with ui.column().classes('w-full max-w-2xl ml-8 px-4 pt-0'):
                # Header row for Label and Button
                with ui.row().classes('w-full items-center justify-between'):
                    ui.label('Known Spells').classes('text-h5')
                    ui.button(icon='add', on_click=lambda: ui.notify('Spell search coming soon!')) \
                        .props('flat round color=primary')

                # Content area
                with ui.card().classes('w-full p-6 border-dashed border-2 border-slate-200 bg-slate-50 shadow-none'):
                    ui.label('Your spellbook is empty.').classes('text-slate-500 italic mx-auto')

    # Edit Dialog (triggered by the edit button)
    with ui.dialog() as edit_dialog, ui.card():
        ui.label('Edit Max Slots').classes('text-lg')
        new_max = ui.number('Max Slots', value=0, min=0, precision=0)
        with ui.row().classes('justify-end w-full'):
            ui.button('Save', on_click=edit_dialog.close)

    # Simple logic to open dialog (since you mentioned no logic, this is just a placeholder)
    table.on('edit_max', lambda e: edit_dialog.open())

    bottom_tabs()