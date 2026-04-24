from nicegui import ui

def bottom_tabs():
    with ui.footer().classes('bg-primary text-white p-0'):
        with ui.tabs().classes('justify-start') as tabs:
            ui.tab('Home', icon='home').on('click', lambda: ui.navigate.to('/'))
            ui.tab('Overview', icon='person').on('click', lambda: ui.navigate.to('/overview'))
            ui.tab('Stats', icon='numbers').on('click', lambda: ui.navigate.to('/stats'))
            ui.tab('Features', icon='interests').on('click', lambda: ui.navigate.to('/features'))
            ui.tab('Combat', icon='sports_mma').on('click', lambda: ui.navigate.to('/combat'))
            ui.tab('Spellbook', icon='auto_stories').on('click', lambda: ui.navigate.to('/spellbook'))
            ui.tab('Inventory', icon='backpack').on('click', lambda: ui.navigate.to('/inventory'))
            ui.tab('Notes', icon='notes').on('click', lambda: ui.navigate.to('/notes'))
            ui.tab('Levelling', icon='table_rows').on('click', lambda: ui.navigate.to('/levelling'))

    return tabs