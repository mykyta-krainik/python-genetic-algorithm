import matplotlib
import tkinter as tk

from modules.classes.UI import UI
from modules.classes.Route import Route
from modules.classes.City import City
from modules.functions.generate_random_color import generate_random_color

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

matplotlib.use("TkAgg")


class MapUI(UI):
    def __init__(self):
        super().__init__()
        self._window.title("Genetic Algorithm")
        self._window.geometry("800x600")
        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.ax = self.fig.add_subplot()
        self.ax.grid(True)

    def draw_solutions(self, cities: list[City], solutions: list[Route]):
        xs = MapUI._get_x_coordinates(cities)
        ys = MapUI._get_y_coordinates(cities)

        MapUI._draw_points(self.ax, xs, ys)
        MapUI._label_points(self.ax, xs, ys)

        for i, solution in enumerate(solutions):
            if i == len(solutions) - 1:
                MapUI._draw_solution(self.ax, solution, 3)

                continue

            MapUI._draw_solution(self.ax, solution)

        self.ax.set_xticks([i for i in range(int(min(xs)), int(max(xs)) + 1)])
        self.ax.set_yticks([i for i in range(int(min(ys)), int(max(ys)) + 1)])
        self.ax.set_xlabel("x")
        self.ax.set_ylabel("y")

        canvas = FigureCanvasTkAgg(self.fig, master=self._window)
        canvas.draw()

        for i, solution in enumerate(solutions):
            MapUI._create_label(f"Solution {i}: {solution.fitness}", i + 5, 0)

        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self._window.mainloop()

    @staticmethod
    def _draw_solution(ax, solution: Route, line_width=1):
        cities = solution.route
        color = generate_random_color()

        for i in range(len(cities) - 1):
            from_city = cities[i]
            to_city = cities[i + 1]
            ax.plot(
                [from_city.x, to_city.x],
                [from_city.y, to_city.y],
                color=color,
                linestyle="dashed",
                linewidth=line_width,
            )

    @staticmethod
    def _draw_cities(ax, cities: list[City]):
        xs = MapUI._get_x_coordinates(cities)
        ys = MapUI._get_y_coordinates(cities)

        MapUI._draw_points(ax, xs, ys)

    @staticmethod
    def _draw_points(ax, x: list[int], y: list[int]):
        ax.scatter(x, y, color="red", marker="o")

    @staticmethod
    def _label_points(ax, x: list[int], y: list[int]):
        for i, coord in enumerate(zip(x, y)):
            ax.annotate(text=i, xy=coord)

    @staticmethod
    def _get_x_coordinates(cities: list[City]) -> list[int]:
        return [city.x for city in cities]

    @staticmethod
    def _get_y_coordinates(cities: list[City]) -> list[int]:
        return [city.y for city in cities]
