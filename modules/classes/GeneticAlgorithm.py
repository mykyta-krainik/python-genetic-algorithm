import sys
import random as rd
from typing import Callable
import copy

from modules.classes.MapUI import MapUI
from modules.classes.Population import Population
from modules.classes.Route import Route

from modules.functions.helpers import get_euclidean_distance
from modules.functions.comparators import is_less_than, is_greater_than


class GeneticAlgorithm(Population):
    def __init__(
        self,
        input_ui: MapUI,
        population_size: int,
        cities_num: int,
        iters_num: int,
        mutation_rate: float,
    ):
        super().__init__(population_size, cities_num)
        self.iters_num = iters_num
        self.mutation_rate = mutation_rate
        self.best_solutions: list[Route] = []
        self.input_ui = input_ui

    def run(self) -> Route:
        solution = copy.deepcopy(self._get_fittest_route())

        if solution.route[0] != solution.route[-1]:
            solution.route.append(solution.route[0])

        self.best_solutions.append(solution)

        for i in range(self.iters_num):
            self._evolve_population()
            solution = copy.deepcopy(self._get_fittest_route())

            if solution.route[0] != solution.route[-1]:
                solution.route.append(solution.route[0])

            self.best_solutions.append(solution)

        self.input_ui.draw_solutions(self._cities, self.best_solutions)

        return solution

    def _get_fittest_route(self) -> Route:
        fittest_route_distance = sys.maxsize
        fittest_route: Route = Route([])

        for route in self._population:
            if round(route.fitness, 2) < round(fittest_route_distance, 2):
                fittest_route = route
                fittest_route_distance = route.fitness

        return fittest_route

    def _select_parent(self) -> Route:
        return rd.choice(list(self._population))

    def _select_parent_breeding(
        self,
        first_parent: Route,
        compare_distances: Callable[[float, float], bool],
        initial_distance=0,
    ) -> Route:
        second_parent: Route = Route([])
        current_distance = initial_distance

        for i, route in enumerate(self._population):
            if route == first_parent:
                continue

            distance = get_euclidean_distance(first_parent.route, route.route)

            if compare_distances(current_distance, distance):
                current_distance = distance
                second_parent = route

        return second_parent

    def _get_parents_outbreeding(self) -> (Route, Route):
        parent1 = self._select_parent()
        parent2 = self._select_parent_breeding(parent1, is_less_than)

        while parent1 == parent2:
            parent2 = self._select_parent_breeding(parent1, is_less_than)

        return parent1, parent2

    def _get_parents_inbreeding(self) -> (Route, Route):
        parent1 = self._select_parent()
        parent2 = self._select_parent_breeding(parent1, is_greater_than, sys.maxsize)

        while parent1 == parent2:
            parent2 = self._select_parent_breeding(
                parent1, is_greater_than, sys.maxsize
            )

        return parent1, parent2

    def _get_parents_panmixia(self) -> (Route, Route):
        parent1 = self._select_parent()
        parent2 = self._select_parent()

        while parent1 == parent2:
            parent2 = self._select_parent()

        return parent1, parent2

    def _evolve_population(self) -> None:
        new_population: set[Route] = set()
        fittest_route = self._get_fittest_route()

        new_population.add(fittest_route)

        while len(new_population) < len(self._population):
            parent1, parent2 = self._get_parents_inbreeding()

            child1, child2 = GeneticAlgorithm._crossover(parent1, parent2)

            if rd.random() < self.mutation_rate:
                child1.mutate()

            if rd.random() < self.mutation_rate:
                child2.mutate()

            new_population.add(child1)
            new_population.add(child2)

        self._population = new_population

    @staticmethod
    def _crossover(parent1: Route, parent2: Route) -> tuple[Route, Route]:
        crossover_point = rd.randint(1, len(parent1.route) - 2)

        child1 = GeneticAlgorithm._get_child_route(parent1, parent2, crossover_point)
        child2 = GeneticAlgorithm._get_child_route(parent2, parent1, crossover_point)

        return child1, child2
