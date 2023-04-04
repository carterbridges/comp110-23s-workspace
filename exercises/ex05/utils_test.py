"""Units tests."""

__author__ = "730563367"


from utils import only_evens, sub, concat


def test_only_evens() -> None:
    """Test of only_evens."""
    assert only_evens([]) == []


def test_only_evens1() -> None:
    """Test of only_evens1."""
    assert only_evens([1, 2, 3, 4, 5]) == [2, 4]


def test_only_evens2() -> None:
    """Test of only_evens2."""
    assert only_evens([1, 3, 5, 7, 10]) == [10]


def test_sub() -> None:
    """Test of subs."""
    assert sub([1, 3, 5, 7], 0, 4) == [1, 3, 5, 7]


def test_sub1() -> None:
    """Test of subs1."""
    assert sub([1, 3, 5, 7], 1, 3) == [3, 5]


def test_sub2() -> None:
    """Test of subs2."""
    assert sub([], 2, 4) == []


def test_concat() -> None:
    """Test of concat."""
    assert concat([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]


def test_concat1() -> None:
    """Test of concat1."""
    assert concat([], []) == []


def test_concat2() -> None:
    """Test of concat2."""
    assert concat([1, 5, 9], [2, 6, 10]) == [1, 5, 9, 2, 6, 10]