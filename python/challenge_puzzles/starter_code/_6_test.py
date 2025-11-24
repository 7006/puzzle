import pytest
from _6 import *


@pytest.mark.parametrize(
    "output_strs, input_strs",
    [
        (["fish", "elephant"], ["cat", "dog", "fish", "elephant"]),
        ([], ["q", "w", "e", "r", "t", "y"]),
        (["qq", "ww", "ee", "rr", "yy"], ["qq", "ww", "ee", "rr", "t", "yy"]),
    ],
)
def test_filter_even_length_strings(
    output_strs: list[str], input_strs: list[str]
) -> None:
    assert output_strs == filter_even_length_strings(input_strs)
