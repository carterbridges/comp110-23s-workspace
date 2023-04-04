"""Dictionary Exercise 7."""

__author__ = "730563367"


def invert(dict1: dict[str, str]) -> dict[str, str]:
    """Invert function exercise 7."""
    inverted: dict[str, str] = {}
    for key in dict1:
        val = dict1[key]
        if val in inverted:
            raise KeyError("Error. This is not unique. ")
        inverted[val] = key
    return inverted


def favorite_color(name_color: dict[str, str]) -> str:
    """Favorite color function for exercise 7."""
    count = {}
    for key in name_color:
        color = name_color[key]
        if color in count:
            count[color] += 1
        else:
            count[color] = 1
    max = 0
    pop_color = ""
    for color in count:
        frequent = count[color]
        if frequent > max:
            max = frequent
            pop_color = color

    return pop_color


def count(list_1: list[str]) -> dict[str, int]:
    """Count function exercise 7."""
    my_dict: dict[str, int] = {}
    for item in list_1:
        if item in my_dict:
            my_dict[item] += 1
        else:
            my_dict[item] = 1
    return my_dict