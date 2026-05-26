from nicegui import ui
from core.models.inventory import Currency
import state

def wallet_dialog(on_submit):
    with ui.dialog() as dialog, ui.card().classes('p-4 w-64 gap-4'):
        ui.label('Adjust Currency').classes('text-lg font-bold')

        # Inputs
        amount = ui.number(label='Amount', value=0, format='%d').classes('w-full')
        unit = ui.select(['PP', 'GP', 'EP', 'SP', 'CP'], value='GP', label='Unit').classes('w-full')

        # Actions
        with ui.row().classes('w-full justify-end gap-2 mt-2'):
            ui.button('Cancel', on_click=dialog.close).props('flat')
            ui.button('OK', on_click=lambda: [
                on_submit(int(amount.value or 0), unit.value.lower()),
                dialog.close()
            ])

    return dialog


def add_curr(amount, unit):
    if not state.current_char:
        ui.notify('No active character found.', type='warning')
        return

    if not hasattr(state.current_char, 'inventory') or state.current_char.inventory is None:
        from core.models.inventory import Inventory
        state.current_char.inventory = Inventory()

    if not hasattr(state.current_char.inventory, 'wallet') or state.current_char.inventory.wallet is None:
        state.current_char.inventory.wallet = Currency()

    state.current_char.inventory.wallet.add_coins(Currency(**{unit: amount}))
    ui.navigate.to('/inventory')


def spend_curr(amount, unit):
    if not state.current_char:
        ui.notify('No active character found.', type='warning')
        return

    if not hasattr(state.current_char, 'inventory') or state.current_char.inventory is None:
        from core.models.inventory import Inventory
        state.current_char.inventory = Inventory()

    if not hasattr(state.current_char.inventory, 'wallet') or state.current_char.inventory.wallet is None:
        state.current_char.inventory.wallet = Currency()

    wallet = state.current_char.inventory.wallet

    try:
        wallet.spend_coins(amount, unit)
        ui.navigate.to('/inventory')
    except ValueError as e:
        ui.notify(str(e), type='negative')



