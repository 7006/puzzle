import pytest
from _7 import *


@pytest.mark.parametrize(
    "output_nums, input_nums",
    [
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([], []),
        ([0, 5, 30, 10, 25, 15, 20], [20, 15, 25, 10, 30, 5, 0]),
    ],
)
def test_reverse_elements(output_nums: list[int], input_nums: list[int]) -> None:
    assert output_nums == reverse_elements(input_nums)
