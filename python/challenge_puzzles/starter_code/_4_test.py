import pytest
from _4 import *


@pytest.mark.parametrize(
    "input_str, output_str",
    [
        ("Hll, Wrld!", "Hello, World!"),
        ("", "aeiouAEIOU"),
        ("zzxxxccvvvbbnnmmmLLKKJJHH", "zzxxxccvvvbbnnmmmLLKKJJHH"),
    ],
)
def test_remove_vowels(input_str: str, output_str: str) -> None:
    assert remove_vowels(input_str) == output_str
