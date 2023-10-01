import random


def generate_random_color() -> str:
    # Generate a random RGB color
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)

    return f"#{red:02X}{green:02X}{blue:02X}"  # Format as a hexadecimal color
