from datetime import date
import uuid

class Notebook:
    def __init__(self, entries:list = None):
        self.entries = entries if entries is not None else []

    def add_note(self, title:str = '', entry_date:date = None, notes:str = ''):
        if entry_date is None:
            entry_date = date.today()

        entry = {"title": title,
                 "date": entry_date,
                 "notes": notes,
                 "id": str(uuid.uuid4())}

        self.entries.append(entry)

    def update_note(self, note_id, title, entry_date, notes):
        for entry in self.entries:
            if entry['id'] == note_id:
                entry['title'] = title
                entry['date'] = entry_date
                entry['notes'] = notes
                break

