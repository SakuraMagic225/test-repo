import pytest

from src.calculator import add, divide, subtract


def test_add() -> None:
    assert add(1, 2) == 3


def test_subtract() -> None:
    assert subtract(5, 2) == 3


def test_divide() -> None:
    assert divide(6, 2) == 3