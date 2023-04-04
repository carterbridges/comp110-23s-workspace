"""Utility Functions."""

__author__ = "730563367"


def all(numbers: list[int], return_value: int) -> bool:
    """Function that shows whether or not all the ints in the list are the same as the given int."""
    if not numbers:
        return False
    idx = 0
    while idx < len(numbers):
        if numbers[idx] != return_value:
            return False
        idx += 1
    return True


def max(number: list[int]) -> int:
    """Finds the max number within a list."""
    if len(number) == 0:
        raise ValueError("max() arg is an empty List")
    indx: int = 1
    max_value: int = number[0]
    while indx < len(number):
        if max_value < number[indx]:
            max_value = number[indx]
        indx += 1
    return max_value


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Function showing is every element at every index is equal between list 1 and list 2."""
    if len(list1) == 0 and len(list2) == 0:
        return True
    if len(list1) != len(list2):
        return False
    index = 0
    while len(list1) == len(list2):
        if list1[index] != list2[index]:
            return False    
        if list1[index] == list2[index]:
            return True
        index += 1
    return True