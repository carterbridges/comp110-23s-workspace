"""Tests for dictionaries in exercise 7."""

__author__ = "730563367"

from dictionary import invert
from dictionary import favorite_color
from dictionary import count


def test_invert_edge():
    """Edge test for invert."""
    input_dict: dict[str, str] = {"Jordan": "Michael"}
    expected_output: dict[str, str] = {"Michael": "Jordan"}
    assert invert(input_dict) == expected_output


def test_invert_usecase_1():
    """Use case 1 for invert."""
    input_dict: dict[str, str] = {"hi": "hey", "carter": "cole"}
    expected_output: dict[str, str] = {"hey": "hi", "cole": "carter"}
    assert invert(input_dict) == expected_output


def test_invert_usecase_2():
    """Use case 2 for invert."""
    input_dict: dict[str, str] = {"horse": "cow", "man": "woman", "cell": "phone"}
    expected_output: dict[str, str] = {"cow": "horse", "woman": "man", "phone": "cell"}
    assert invert(input_dict) == expected_output


def test_favorite_color_edge():
    """Edge case for favorite color."""
    input_dict: dict[str, str] = {}
    expected_output: str = ""
    assert favorite_color(input_dict) == expected_output


def test_favorite_color_usecase1():
    """Use case 1 for favorite color."""
    input_dict: dict[str, str] = {"Carter": "blue", "Seth": "blue", "Andrew": "green", "Cole": "yellow"}
    expected_output: str = "blue"
    assert favorite_color(input_dict) == expected_output


def test_favorite_color_usecase2():
    """Use case 2 for favorite color."""
    input_dict: dict[str, str] = {"Carter": "yellow", "Seth": "blue", "Andrew": "red", "Cole": "yellow"}
    expected_output: str = "yellow"
    assert favorite_color(input_dict) == expected_output


def test_count_edge():
    """Edge case test for count."""
    input_list: list[str] = []
    expected_output: dict[str, int] = {}
    assert count(input_list) == expected_output


def test_count_usecase1():
    """Use case 1 for count."""
    input_list: list[str] = ["pear", "pickle", "pear", "peach", "pickle", "pear"]
    expected_output: dict[str, int] = {"pear": 3, "pickle": 2, "peach": 1}
    assert count(input_list) == expected_output


def test_count_usecase2():
    """Use case 2 for count."""
    input_list: list[str] = ["cake", "brownie", "cookie", "scone", "rice krispie"]
    expected_output: dict[str, int] = {"cake": 1, "brownie": 1, "cookie": 1, "scone": 1, "rice krispie": 1}
    assert count(input_list) == expected_output