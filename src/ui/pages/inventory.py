from nicegui import ui
from ui.components.bottom_tabs import bottom_tabs
from ui.components.global_header import global_header
from ui.components.wallet_calculator import *
from core.models.inventory import Item, Armor, Weapon, Shield
import state


@ui.page('/inventory')
def content():
    global_header()

    # Data setup
    char = getattr(state, 'current_char', None)
    inv = getattr(char, 'inventory', None) if char else None
    wallet = inv.wallet if inv else None

    # Main Container
    with ui.column().classes('w-full p-4 max-w-4xl ml-4 mb-24 gap-6'):

        # --- Page Header ---
        with ui.row().classes('w-full justify-between items-center'):
            ui.label('Inventory').classes('text-2xl mb-4 font-bold')
            weight = inv.total_weight if inv else 0.0
            ui.label(f'{weight:.1f} lbs').classes('text-subtitle1 text-grey-7')

        # --- 1. Armor & Shields Section ---
        with ui.column().classes('w-full gap-2'):
            ui.label('Armor & Shields').classes('text-h6 text-primary')
            ui.separator()
            if inv:
                render_item_list(inv.armors + inv.shields, inv)
            else:
                ui.label('No armor equipped.').classes('text-grey italic ml-2')

        # --- 2. Coins Section ---
        with ui.column().classes('w-full gap-2'):
            with ui.row().classes('w-full justify-between items-center'):
                ui.label('Currency').classes('text-h6 text-primary')
                # Global +/- buttons
                with ui.row().classes('gap-1'):
                    ui.button(icon='remove', on_click=lambda: wallet_dialog(on_submit=spend_curr)).props('flat dense')
                    ui.button(icon='add', on_click=lambda: wallet_dialog(on_submit=add_curr)).props('flat dense')

            with ui.card().classes('w-full bg-slate-50 ml-0 shadow-sm'):
                with ui.row().classes('w-full justify-around p-2'):
                    units = ['pp', 'gp', 'ep', 'sp', 'cp']
                    for unit in units:
                        val = getattr(wallet, unit, 0) if wallet else 0
                        with ui.column().classes('items-center'):
                            ui.label(unit.upper()).classes('text-xs font-bold text-gray-500')
                            ui.number(value=val, format='%d').classes('w-16').props('dense borderless readonly')

        # --- 3. Equipment & Weapons Section ---
        with ui.column().classes('w-full gap-2'):
            ui.label('Equipment & Weapons').classes('text-h6 text-primary')
            ui.separator()
            if inv:
                # Combining weapons and other items as "Equipment"
                render_item_list(inv.weapons + inv.other_items, inv)
            else:
                ui.label('No equipment found.').classes('text-grey italic ml-2')

        # --- 4. Treasure Section ---
        with ui.column().classes('w-full gap-2'):
            ui.label('Treasure').classes('text-h6 text-primary')
            ui.separator()
            # If your model doesn't have a specific 'treasure' property yet,
            # this serves as a placeholder or a filtered list of high-value items.
            ui.label('No treasure currently held.').classes('text-grey italic ml-2')

        # Floating Add Button
        ui.button(icon='add', on_click=lambda: ui.notify('Add item dialog coming soon!')) \
            .props('round elevated color=primary size=lg') \
            .classes('fixed bottom-24 left-8 z-50')

    bottom_tabs()


def render_item_list(items, inventory_obj):
    if not items:
        ui.label('Empty.').classes('text-gray-400 italic ml-2 mt-1')
        return

    for item in items:
        with ui.card().classes('w-full mb-1 ml-0 hover:bg-slate-50 transition'):
            with ui.row().classes('w-full items-center no-wrap'):
                # Item Name & Quick Stats
                with ui.column().classes('flex-grow'):
                    with ui.row().classes('items-center gap-2'):
                        ui.label(item.name).classes('font-bold')
                        if isinstance(item, Weapon):
                            ui.badge(item.damage_str, color='orange-9')
                        elif isinstance(item, Armor):
                            ui.badge(f"AC {item.base_ac}", color='blue-9')
                        elif isinstance(item, Shield):
                            ui.badge(f"+{item.ac_bonus} AC", color='cyan-8')

                # Quantity, Weight, and Actions
                with ui.row().classes('items-center gap-4'):
                    with ui.column().classes('items-end'):
                        ui.label(f"x{item.quantity}").classes('font-mono text-sm')
                        ui.label(f"{item.weight * item.quantity:.1f} lbs").classes('text-[10px] text-grey')

                    ui.button(icon='delete', color='red',
                              on_click=lambda i=item: [inventory_obj.remove_item(i, i.quantity),
                                                       ui.navigate.to('/inventory')]) \
                        .props('flat dense')