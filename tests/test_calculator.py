from src.app.calculator import add, divide
import pytest


def test_add_positive():
    assert add(5, 5) == 10


def test_divide_normal():
    assert divide(5, 5) == 1


def test_add_negative():
    assert add(-5, -5) == -10


def test_fail_add():
    assert add(-5, -5) == 10