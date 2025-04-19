import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None

        self._dd_provider = None
        self._btn_build_graph = None

        self._txt_distance = None
        self._btn_analyze_graph = None

        self._txt_string = None
        self._btn_calculate_path = None

        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        # title
        self._title = ft.Text("NYC - Hotspots", color="orange", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        # text field for the name
        self._dd_provider = ft.Dropdown(label="Provider", width=300)
        self._controller.fillDdProvider()

        # button for the "hello" reply
        self._btn_build_graph = ft.ElevatedButton(text="Build Graph", color="orange", on_click=self._controller.handle_build_graph)
        row1 = ft.Row([ft.Container(width=200), ft.Container(self._dd_provider, width=350), ft.Container(self._btn_build_graph, width=200)],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        #ROW 2
        self._txt_distance = ft.TextField(
            label="distance (x)",
            width=300,
            hint_text="Insert the distance"
        )

        self._btn_analyze_graph = ft.ElevatedButton(text="Analyze Graph", color="orange", on_click=self._controller.handle_analyze_graph)

        row2 = ft.Row([ft.Container(width=200), ft.Container(self._txt_distance, width=350), ft.Container(self._btn_analyze_graph, width=200)], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        #ROW3

        self._txt_string = ft.TextField(
            label="string (s)",
            width=300,
            hint_text="Insert the string"
        )

        self._btn_calculate_path = ft.ElevatedButton(text="Calculate Path", color="orange",
                                                    on_click=self._controller.handle_calculate_path)

        row3 = ft.Row([ft.Container(width=200), ft.Container(self._txt_string, width=350),  ft.Container(self._btn_calculate_path, width=200)], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)

        #ROW4

        self._dd_target = ft.Dropdown(label="Target (x)", width=300)

        row4 = ft.Row([ft.Container(width=200), ft.Container(self._dd_target, width=350), ft.Container(width=200),], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row4)




        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
