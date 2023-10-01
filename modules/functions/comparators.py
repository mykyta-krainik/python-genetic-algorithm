def is_greater_than(num1: float, num2: float, places=2) -> bool:
    return round(num1, places) > round(num2, places)


def is_less_than(a: float, b: float, places=2) -> bool:
    return round(a, places) < round(b, places)
