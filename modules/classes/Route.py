import random as rd

from modules.classes import City


# Description: A route represent an individual
class Route:
    def __init__(self, route: list[City]) -> None:
        self.route = route
        self.fitness = Route._calculate_fitness(self.route)

    def __str__(self) -> str:
        return f"Route: {self.route} Fitness: {self.fitness}"

    def __lt__(self, other):
        return self.fitness < other.fitness

    def __gt__(self, other):
        return self.fitness > other.fitness

    def __eq__(self, other):
        for r1, r2 in zip(self.route, other.route):
            if r1 != r2:
                return False

        return True

    def __hash__(self):
        return hash(tuple(self.route))

    def print_route(self):
        for city in self.route:
            print(city)

    def mutate(self):
        route_len = len(self.route)
        index1 = rd.randint(0, route_len - 1)
        index2 = rd.randint(0, route_len - 1)

        while index1 == index2:
            index2 = rd.randint(0, route_len - 1)

        self.route[index1], self.route[index2] = self.route[index2], self.route[index1]
        self.fitness = Route._calculate_fitness(self.route)

    @staticmethod
    def _calculate_fitness(route: list[City]) -> float:
        total_distance = 0

        for i in range(len(route)):
            from_city = route[i]
            to_city = route[i + 1] if i + 1 < len(route) else route[0]
            total_distance += Route._calculate_distance(from_city, to_city)

        return round(total_distance, 5)

    @staticmethod
    def _calculate_distance(from_city: City, to_city: City) -> float:
        return ((from_city.x - to_city.x) ** 2 + (from_city.y - to_city.y) ** 2) ** 0.5
