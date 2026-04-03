import flet as ft
from ui.layout import AppLayout


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    page.title = "Digital Hireling"

    # Load the UI Skeleton
    layout = AppLayout()

    # Define the Nav Bar here so it can talk to the Layout
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon="home", label="Home"),
            ft.NavigationBarDestination(icon="list", label="Features"),
            ft.NavigationBarDestination(icon="settings", label="Settings"),
        ],
        on_change=lambda e: layout.change_tab(e.control.selected_index)
    )

    page.add(layout)


ft.app(target=main)