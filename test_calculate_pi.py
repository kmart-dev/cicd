import pytest
from calculate_pi import calculate_pi

def test_calculate_pi():
    """
    Test to ensure the first three digits of pi are 3.14.
    """
    result = calculate_pi()
    assert str(result).startswith("3.14"), "Pi calculation did not start with 3.14"
