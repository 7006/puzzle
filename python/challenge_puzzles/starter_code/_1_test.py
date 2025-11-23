import pytest
from _1 import *


@pytest.mark.parametrize(
    "input_strs, output_strs",
    [
        (["apple", "banana", "cherry", "date"], ["apple", "banana", "date"]),
        ([], []),
        (["bbbb", "cccc"], []),
    ],
)
def test_filter_strings_containing_a(
    input_strs: list[str], output_strs: list[str]
) -> None:
    assert filter_strings_containing_a(input_strs) == output_strs
