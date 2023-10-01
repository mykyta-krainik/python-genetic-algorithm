from modules.types.InputData import InputData
from modules.types.InputDataEntries import InputDataEntries
from modules.functions.validate_input import validate_input
from modules.classes.UI import UI


class InputUI(UI):
    def __init__(self, padding=10):
        super().__init__()
        self._padding = padding
        self._entries: InputDataEntries = dict()

    def start(self, handle_click: callable(InputData)):
        self._window.title("Genetic Algorithm")
        self._window.geometry("500x500")

        self._render_window_items(handle_click)

        self._window.mainloop()

    def _render_window_items(self, handle_click: callable(InputData)):
        iters_num_entry = InputUI._create_entry_with_label(
            "Iters number", 0, 0, self._padding, self._padding
        )["entry"]
        self._entries["iters_num"] = iters_num_entry

        cities_num_entry = InputUI._create_entry_with_label(
            "Cities number", 1, 0, self._padding, self._padding
        )["entry"]
        self._entries["cities_num"] = cities_num_entry

        mutation_rate_entry = InputUI._create_entry_with_label(
            "Mutation rate", 2, 0, self._padding, self._padding
        )["entry"]
        self._entries["mutation_rate"] = mutation_rate_entry

        population_size_entry = InputUI._create_entry_with_label(
            "Population size", 3, 0, self._padding, self._padding
        )["entry"]
        self._entries["population_size"] = population_size_entry

        def on_click():
            handle_click(self.get_input_data())
            self._window.quit()

        InputUI._create_btn("Start", 4, 0, on_click)

    def get_input_data(self) -> InputData:
        iters_num_str = self._entries["iters_num"].get()
        cities_num_str = self._entries["cities_num"].get()
        mutation_rate_str = self._entries["mutation_rate"].get()
        population_size_str = self._entries["population_size"].get()

        if (
            not validate_input(iters_num_str)
            or not validate_input(cities_num_str)
            or not validate_input(mutation_rate_str)
            or not validate_input(population_size_str)
        ):
            raise Exception("Invalid input")

        return InputData(
            iters_num=int(iters_num_str),
            cities_num=int(cities_num_str),
            mutation_rate=float(mutation_rate_str),
            population_size=int(population_size_str),
        )
