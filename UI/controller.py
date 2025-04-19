import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

        self._selected_provider = None
        self._selected_location = None

    def handle_build_graph(self, e):
        #FARE CONTROLLO INPUT SU txt_distance

        self._model.buildGraph(self._selected_provider, float(self._view._txt_distance.value))

        self._view.txt_result.controls.append(ft.Text(f"Grafo Correttamente creato:\n"
                                                      f"nNodes: {len(self._model._myGraph.nodes)} \n"
                                                      f"nEdges: {len(self._model._myGraph.edges)}"))

        self._view._dd_target.disabled=False
        for n in list(self._model._myGraph.nodes):
            self._view._dd_target.options.append(ft.dropdown.Option(text=n.locName, data=n, on_click=self.readDdLocation))
        self._view.update_page()
        pass

    def handle_analyze_graph(self, e):
        self._view.txt_result.controls.append(ft.Text(f"Graph analysis:"))
        for n in self._model.analyzeGraph():
            self._view.txt_result.controls.append(ft.Text(f"{n.locName} - {n.neighbors}"))
        self._view.update_page()
        pass

    def handle_calculate_path(self, e):
        path = self._model.getPath(self._view._txt_string.value, self._selected_location)
        if path is False:
            self._view.txt_result.controls.append(ft.Text(f"Non esiste un percorso."))
            self._view.update_page()
            return
        self._view.txt_result.controls.append(ft.Text(f"The longest path has a length of {len(path)} locations."))
        self._view.update_page()
        pass

    def fillDdProvider(self):
        providers = list(self._model.getProviders())
        for p in providers:
            self._view._dd_provider.options.append(ft.dropdown.Option(data=p, text=p, on_click=self.readDdProvider))

        pass

    def readDdProvider(self, e):
        if e.control.data is None:
            self._selected_provider = None
        else:
            self._selected_provider = e.control.data

    def readDdLocation(self, e):
        if e.control.data is None:
            self._selected_location = None
        else:
            self._selected_location = e.control.data