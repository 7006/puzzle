import pytest
from _4 import *


@pytest.mark.parametrize(
    "output_str, input_str",
    [
        ("Hll, Wrld!", "Hello, World!"),
        ("", "aeiouAEIOU"),
        ("zzxxxccvvvbbnnmmmLLKKJJHH", "zzxxxccvvvbbnnmmmLLKKJJHH"),
    ],
)
def test_remove_vowels(output_str: str, input_str: str) -> None:
    assert output_str == remove_vowels(input_str)
