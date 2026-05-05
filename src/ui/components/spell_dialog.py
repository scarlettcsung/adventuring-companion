from nicegui import ui
from core.models.spell import Spell
import state


class SpellDialog(ui.dialog):
    def __init__(self, on_success=None):
        super().__init__()
        self.on_success = on_success
        # Default state
        self.data = {
            'name': '', 'level': 0, 'school': 'Evocation',
            'cast_time': '1 Action', 'range': '60 ft', 'duration': 'Instantaneous',
            'desc': '', 'components': [], 'is_ritual': False,
            'is_concentration': False, 'damage_dice': None, 'damage_type': None
        }

        with self, ui.card().classes('w-[600px] p-6') as self.card:
            self.show_choice_view()

    def show_choice_view(self):
        """Initial view to choose between searching or creating."""
        self.card.clear()
        with self.card:
            ui.label('Add Spell').classes('text-xl font-bold self-center')
            with ui.row().classes('w-full justify-center gap-4 no-wrap'):
                ui.button('Search Spell', icon='search',
                          on_click=lambda: ui.notify('Search logic coming soon!')) \
                    .props('outline stack').classes('flex-1 h-20')
                ui.button('Create Custom', icon='edit',
                          on_click=self.show_form_view) \
                    .props('stack').classes('flex-1 h-20')
            ui.button('Cancel', on_click=self.close).props('flat').classes('self-center mt-4')

    def show_form_view(self):
        """The main form for manual spell entry."""
        self.card.clear()
        with self.card:
            ui.label('Create Custom Spell').classes('text-xl font-bold mt-2')

            # --- Basic Info Row ---
            with ui.row().classes('w-full items-center'):
                ui.input('Name', on_change=lambda e: self.update_data('name', e.value)).classes('flex-grow')
                ui.number('Level', value=0, min=0, max=9, format='%d',
                          on_change=lambda e: self.update_data('level', int(e.value))).classes('w-16')

            # --- School & Cast Time ---
            with ui.row().classes('w-full'):
                ui.select(['Abjuration', 'Conjuration', 'Divination', 'Enchantment',
                           'Evocation', 'Illusion', 'Necromancy', 'Transmutation'],
                          label='School', value='Evocation',
                          on_change=lambda e: self.update_data('school', e.value)).classes('flex-1')
                ui.input('Casting Time', value='1 Action',
                         on_change=lambda e: self.update_data('cast_time', e.value)).classes('flex-1')

            # --- Range & Duration ---
            with ui.row().classes('w-full'):
                ui.input('Range', value='60 ft',
                         on_change=lambda e: self.update_data('range', e.value)).classes('flex-1')
                ui.input('Duration', value='Instantaneous',
                         on_change=lambda e: self.update_data('duration', e.value)).classes('flex-1')

            # --- Tags & Components ---
            with ui.row().classes('items-center gap-4'):
                ui.checkbox('Ritual', on_change=lambda e: self.update_data('is_ritual', e.value))
                ui.checkbox('Concentration', on_change=lambda e: self.update_data('is_concentration', e.value))

                with ui.row().classes('items-center border p-1 rounded'):
                    ui.label('Comp:').classes('text-xs text-gray-500 ml-1')
                    for c in ['V', 'S', 'M']:
                        ui.checkbox(c, on_change=lambda e, val=c: self.update_components(val, e.value))

            ui.separator().classes('my-2')

            # --- Damage Section (Conditional) ---
            dmg_switch = ui.switch('Has Damage/Healing')

            with ui.row().classes('w-full items-center').bind_visibility_from(dmg_switch, 'value'):
                ui.input('Damage Dice (e.g. 1d8)',
                         on_change=lambda e: self.update_data('damage_dice', e.value)).classes('flex-1')
                ui.select(['Slashing', 'Piercing', 'Bludgeoning', 'Acid', 'Cold', 'Fire',
                           'Force', 'Lightning', 'Necrotic', 'Poison', 'Psychic',
                           'Radiant', 'Thunder', 'Healing'],
                          label='Type', on_change=lambda e: self.update_data('damage_type', e.value)).classes('flex-1')

            # --- Description ---
            ui.textarea('Description', on_change=lambda e: self.update_data('desc', e.value)) \
                .classes('w-full').props('outlined autogrow')

            # --- Action Buttons ---
            with ui.row().classes('w-full justify-end mt-4'):
                ui.button('Back', on_click=self.show_choice_view).props('flat')
                ui.button('Save Spell', on_click=self.save_spell)

    def update_data(self, key, value):
        self.data[key] = value

    def update_components(self, label, active):
        if active and label not in self.data['components']:
            self.data['components'].append(label)
        elif not active and label in self.data['components']:
            self.data['components'].remove(label)

    def save_spell(self):
        # Create instance of Spell dataclass
        new_spell = Spell(
            name=self.data['name'] or 'New Spell',
            level=self.data['level'],
            school=self.data['school'],
            cast_time=self.data['cast_time'],
            range=self.data['range'],
            duration=self.data['duration'],
            desc=self.data['desc'],
            components=self.data['components'],
            is_ritual=self.data['is_ritual'],
            is_concentration=self.data['is_concentration'],
            damage_dice=self.data['damage_dice'] if self.data['damage_dice'] else None,
            damage_type=self.data['damage_type'] if self.data['damage_type'] else None
        )

        # Append to character state
        if hasattr(state, 'current_char'):
            state.current_char.spells.append(new_spell)

        if self.on_success:
            self.on_success()

        self.close()
        # Reset view for next time it opens
        self.show_choice_view()