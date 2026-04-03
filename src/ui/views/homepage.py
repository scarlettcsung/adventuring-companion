import flet as ft


class Homepage(ft.Container):  # Using Container as a base for easy styling
    def __init__(self):
        super().__init__()
        self.padding = 20
        self.expand = True

        # This is where we "Draw" the UI
        self.content = ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                # A Big, Round Logo or Title
                ft.Container(
                    content=ft.Icon(ft.Icons.PERSON_SEARCH_ROUNDED, size=80, color="#d4af37"),
                    margin=ft.margin.only(top=40),
                ),
                ft.Text("DIGITAL HIRELING", size=32, weight="bold", color="white"),
                ft.Text("Your 2,000 features, ready for action.", color="#949ba4"),

                ft.Divider(height=40, color="transparent"),

                # A big, rounded "Quick Action" Button
                ft.ElevatedButton(
                    text="SEARCH FEATURES",
                    icon=ft.Icons.SEARCH,
                    style=ft.ButtonStyle(
                        color="white",
                        bgcolor="#1f2233",
                        shape=ft.RoundedRectangleBorder(radius=20),  # THE "PILL" SHAPE
                        padding=20,
                    ),
                    on_click=lambda _: print("Searching...")
                ),

                # A simple stats row
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        self.stat_box("2,142", "Features"),
                        self.stat_box("14", "Spells"),
                    ]
                )
            ]
        )

    # A helper function to make reusable "Stat Boxes"
    def stat_box(self, value, label):
        return ft.Container(
            content=ft.Column([
                ft.Text(value, size=20, weight="bold", color="white"),
                ft.Text(label, size=12, color="#949ba4"),
            ], horizontal_alignment="center"),
            padding=15,
            bgcolor="#1a1c26",
            border_radius=15,
            width=100
        )