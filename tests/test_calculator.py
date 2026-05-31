import pytest

from src.calculator import add, divide, subtract, multiply


def test_add() -> None:
    assert add(1, 2) == 3


def test_subtract() -> None:
    assert subtract(5, 2) == 3

def test_multiply() -> None:
    assert multiply(3, 4) == 12

def test_divide() -> None:
    assert divide(6, 2) == 3