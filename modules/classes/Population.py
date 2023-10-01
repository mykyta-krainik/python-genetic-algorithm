import random as rd

from modules.classes.City import City
from modules.classes.Route import Route
from modules.functions.helpers import factorial, shuffle_list


class Population:
    def __init__(self, population_size: int, cities_num: int):
        self._cities: list[City] = []
        self._population = self.generate_initial_population(population_size, cities_num)

    def generate_initial_population(
        self, population_size: int, cities_num: int
    ) -> set[Route]:
        possible_options = factorial(cities_num)

        if population_size > possible_options:
            raise Exception(
                "Population size is bigger than the number of possible options"
            )

        self._generate_random_cities(cities_num)
        routes: set[Route] = set()

        for i in range(population_size):
            path = shuffle_list(self._cities)
            route = Route(path)

            if route in routes:
                continue

            routes.add(route)

        return routes

    def _generate_random_cities(self, cities_num: int) -> list[City]:
        i = cities_num

        while True:
            city = Population._generate_random_city(cities_num)

            if city in self._cities:
                continue

            self._cities.append(city)
            i -= 1

            if i < 1:
                break

        return self._cities

    @staticmethod
    def _generate_random_city(max_coordinate: int) -> City:
        x = rd.randint(0, max_coordinate)
        y = rd.randint(0, max_coordinate)

        return City((x, y))

    @staticmethod
    def _get_child_route(
        base_parent: Route, end_parent: Route, crossover_point: int
    ) -> Route:
        base_parent_start = base_parent.route[:crossover_point]
        end_parent_start = end_parent.route[:crossover_point]
        end_parent_end = end_parent.route[crossover_point:]

        child = base_parent_start + [
            city for city in end_parent_end if city not in base_parent_start
        ]

        if len(child) < len(base_parent.route):
            for city in end_parent_start:
                if city not in child:
                    child.append(city)

                if len(child) == len(base_parent.route):
                    break

        return Route(child)
