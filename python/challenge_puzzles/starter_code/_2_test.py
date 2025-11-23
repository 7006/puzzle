import pytest
from _2 import *


@pytest.mark.parametrize(
    "num_sum, num_one, num_two",
    [
        (40, 20, 20),
        (None, 20, 30),
        (None, 20, 100),
    ],
)
def test_sum_if_less_than_fifty(
    num_sum: int | None, num_one: int, num_two: int
) -> None:
    assert num_sum == sum_if_less_than_fifty(num_one, num_two)
