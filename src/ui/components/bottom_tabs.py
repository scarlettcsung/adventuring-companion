from nicegui import ui

def bottom_tabs():
    with ui.footer().classes('bg-primary text-white p-0'):
        with ui.tabs().classes('justify-start') as tabs:
            ui.tab('Home', icon='home').on('click', lambda: ui.navigate.to('/'))
            ui.tab('Overview', icon='person').on('click', lambda: ui.navigate.to('/overview'))
            ui.tab('Stats', icon='numbers').classes('text-sky-300') \
                .on('click', lambda: ui.navigate.to('/stats'))
            ui.tab('Features', icon='interests').on('click', lambda: ui.navigate.to('/features'))
            ui.tab('Combat', icon='sports_mma').classes('text-sky-300') \
                .on('click', lambda: ui.navigate.to('/combat'))
            ui.tab('Spellbook', icon='auto_stories').on('click', lambda: ui.navigate.to('/spellbook'))
            ui.tab('Inventory', icon='backpack').on('click', lambda: ui.navigate.to('/inventory'))
            ui.tab('Notebook', icon='book').classes('text-sky-300') \
                .on('click', lambda: ui.navigate.to('/notebook'))
            ui.tab('Levelling', icon='table_rows').classes('text-sky-300') \
                .on('click', lambda: ui.navigate.to('/levelling'))
            ui.tab('Brewery', icon='sports_bar').classes('text-sky-300') \
                .on('click', lambda: ui.navigate.to('/brewery'))

    return tabs