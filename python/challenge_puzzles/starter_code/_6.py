def filter_even_length_strings(input_strs: list[str]) -> list[str]:
    return [i for i in input_strs if len(i) % 2 == 0]
