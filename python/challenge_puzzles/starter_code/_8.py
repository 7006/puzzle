def filter_type_str(input_list: list[str | int]) -> list[str]:
    return [i for i in input_list if isinstance(i, str)]
