"""Building list utility functions."""

__author__ = "730563367"


def only_evens(numbers: list[int]) -> list[int]:
    """Only return even numbers in a list."""
    result: list[int] = []
    for index in numbers:
        if index % 2 == 0:
            result.append(index)
    return result


def concat(num: list[int], num2: list[int]) -> list[int]:
    """Shows all elements from first list with elements from second list."""
    real_list = num + num2
    return real_list


def sub(a_list: list[int], start: int, end: int) -> list[int]:
    """List which is a subset of the given list, between the specified start index and the end index - 1."""
    modified_list = a_list[start:end]
    return modified_list