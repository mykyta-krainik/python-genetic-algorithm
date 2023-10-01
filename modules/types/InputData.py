from typing import TypedDict

InputData = TypedDict(
    "InputData",
    {
        "iters_num": int,
        "cities_num": int,
        "mutation_rate": float,
        "population_size": int,
    },
)
