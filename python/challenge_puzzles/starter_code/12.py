def string_to_ascii(input_str: str) -> list[int]:
    pass


print(string_to_ascii("Programming puzzles!"))
print(string_to_ascii(""))
print(string_to_ascii("aA"))


# Bonus Solution
def ascii_to_string(input_ascii_codes: list[int]) -> str:
    pass


print(
    ascii_to_string(
        [
            80,
            114,
            111,
            103,
            114,
            97,
            109,
            109,
            105,
            110,
            103,
            32,
            112,
            117,
            122,
            122,
            108,
            101,
            115,
            33,
        ]
    )
)
print(ascii_to_string([]))
print(ascii_to_string([97, 65]))
