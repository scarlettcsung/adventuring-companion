import flet as ft
from .views import Homepage


class AppLayout(ft.Column):
    def __init__(self):
        super().__init__(expand=True)
        # Initialize the screens
        self.homepage = Homepage()

        # The "Stage" where views appear
        self.content_area = ft.Container(content=self.homepage, expand=True)

        # The actual layout
        self.controls = [self.content_area]

    def change_tab(self, index):
        if index == 0:
            self.content_area.content = self.homepage
        self.update()