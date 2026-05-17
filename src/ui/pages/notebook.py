from datetime import date
from nicegui import ui

import state
from ui.components.bottom_tabs import bottom_tabs
from ui.components.global_header import global_header


@ui.page('/notebook')
def content():
    global_header()

    # Track form visibility and which note ID is being edited
    page_state = {
        'show_form': False,
        'editing_id': None  # Stores the unique string ID of the note
    }

    with ui.column().classes('w-full max-w-2xl ml-8 p-4 p-24'):
        ui.label('Notebook').classes('text-2xl mb-4 font-bold')

        form_container = ui.column().classes('w-full mb-6')
        notes_container = ui.column().classes('w-full')

        def refresh():
            notes_container.clear()
            form_container.clear()

            # 1. Render the New Note Form
            if page_state['show_form']:
                with form_container.classes('p-4 border rounded-lg bg-gray-50 gap-4'):
                    ui.label('New Note').classes('text-lg font-bold')
                    title_input = ui.input(label='Title').classes('w-full')
                    date_input = ui.input(label='Date', value=str(date.today())).props('type=date')
                    notes_input = ui.textarea(label='Notes').classes('w-full')

                    with ui.row().classes('justify-end gap-2'):
                        ui.button('Cancel', on_click=toggle_form).props('flat')
                        ui.button('Save',
                                  on_click=lambda: save_note(title_input.value, date_input.value, notes_input.value))

            # 2. Render the Notes List
            with notes_container:
                if not state.current_char.notebook.entries:
                    ui.label('No notes yet.').classes('text-gray-400 italic mt-4')
                else:
                    for entry in state.current_char.notebook.entries:
                        note_id = entry['id']

                        # Check if this specific note ID is being edited
                        if page_state['editing_id'] == note_id:
                            with ui.card().classes('w-full mb-2 p-4 bg-blue-50'):
                                ui.label('Edit Note').classes('text-sm font-bold text-blue-600')
                                edit_title = ui.input(label='Title', value=entry['title']).classes('w-full')
                                edit_date = ui.input(label='Date', value=str(entry['date'])).props('type=date')
                                edit_notes = ui.textarea(label='Notes', value=entry['notes']).classes('w-full')

                                with ui.row().classes('justify-end gap-2 w-full'):
                                    ui.button('Cancel', on_click=cancel_edit).props('flat')
                                    ui.button('Update',
                                              on_click=lambda n_id=note_id: update_note(n_id, edit_title.value,
                                                                                        edit_date.value,
                                                                                        edit_notes.value))
                        else:
                            # Standard read-only card (clickable)
                            with ui.card().classes('w-full mb-2 cursor-pointer hover:bg-gray-50') as card:
                                card.on('click', lambda n_id=note_id: start_edit(n_id))
                                ui.label(entry['title']).classes('font-bold')
                                ui.label(str(entry['date'])).classes('text-xs text-gray-500')
                                ui.label(entry['notes'])

        def toggle_form():
            page_state['show_form'] = not page_state['show_form']
            page_state['editing_id'] = None
            refresh()

        def start_edit(note_id):
            page_state['editing_id'] = note_id
            page_state['show_form'] = False
            refresh()

        def cancel_edit():
            page_state['editing_id'] = None
            refresh()

        def save_note(title, entry_date, notes):
            state.current_char.notebook.add_note(title=title, entry_date=entry_date, notes=notes)
            page_state['show_form'] = False
            refresh()

        def update_note(note_id, title, entry_date, notes):
            # Calls the backend update method using the unique ID
            state.current_char.notebook.update_note(note_id=note_id, title=title, entry_date=entry_date, notes=notes)
            page_state['editing_id'] = None
            refresh()

        # Initial render
        refresh()

        ui.button(icon='add', on_click=toggle_form) \
            .props('round size=lg').classes('fixed bottom-24 right-8 shadow-lg')

    bottom_tabs()