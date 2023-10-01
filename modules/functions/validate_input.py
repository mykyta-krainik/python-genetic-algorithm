def validate_input(input_data: str) -> bool:
    if input_data == "":
        return False

    try:
        float(input_data)
        return True
    except ValueError:
        return False
