import pytest
from _1 import *


@pytest.mark.parametrize(
    "output_strs, input_strs",
    [
        (["apple", "banana", "date"], ["apple", "banana", "cherry", "date"]),
        ([], []),
        ([], ["bbbb", "cccc"]),
    ],
)
def test_filter_strings_containing_a(
    output_strs: list[str], input_strs: list[str]
) -> None:
    assert filter_strings_containing_a(input_strs) == output_strs
