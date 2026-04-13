from nicegui import ui

def bottom_tabs():
    with ui.footer().classes('bg-primary text-white p-0'):
        with ui.tabs().classes('justify-start') as tabs:
            ui.tab('Home', icon='home').on('click', lambda: ui.navigate.to('/'))
            ui.tab('Search', icon='search').on('click', lambda: ui.navigate.to('/search'))
            ui.tab('Profile', icon='person').on('click', lambda: ui.navigate.to('/profile'))
    return tabs