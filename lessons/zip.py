"""Challenege Question."""

__author__ = "730563367"

def zip(list1: list[str], list2: list[int]) -> dict[str, int]:
    if len(list1) != len(list2) or len(list1) == 0:
        return dict()
    result: dict[str, int] = {}
    idx = 0
    for word in list1:
        result[word] = list2[idx]
        idx += 1
    return result
