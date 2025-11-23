VOWELS = ["a", "e", "i", "o", "u"]


def remove_vowels(input_str: str) -> str:
    chars = [char for char in input_str if not is_vowel(char)]
    return "".join(chars)


def is_vowel(char: str) -> bool:
    return char.lower() in VOWELS
