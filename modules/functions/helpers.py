import random as rd

from modules.interfaces.ICoordinates import ICoordinates


def factorial(cities_num: int) -> int:
    if cities_num == 1:
        return 1

    return cities_num * factorial(cities_num - 1)


def shuffle_list(input_list: list[any]) -> list[any]:
    return rd.sample(input_list, len(input_list))


def get_euclidean_distance(
    path1: list[ICoordinates], path2: list[ICoordinates]
) -> float:
    dist = 0

    for city1, city2 in zip(path1, path2):
        dist += (city1.x - city2.x) ** 2 + (city1.y - city2.y) ** 2

    return dist**0.5
