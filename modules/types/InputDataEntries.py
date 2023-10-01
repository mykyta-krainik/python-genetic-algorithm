from typing import TypedDict

import tkinter as tk

InputDataEntries = TypedDict(
    "InputDataEntries",
    {
        "iters_num": tk.Entry,
        "cities_num": tk.Entry,
        "mutation_rate": tk.Entry,
        "population_size": tk.Entry,
    },
)
