"""EX04 - List Utility Function."""
__author__ = "730578568"

from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_empty() -> None:
    """Checks only_evens when list is empty."""
    list1: list[int] = []
    assert only_evens(list1) == []


def test_only_evens_evens() -> None:
    """Checks only_evens when list has a even number."""
    list1: list[int] = [1, 2, 3]
    assert only_evens(list1) == [2]


def test_only_evens_odds() -> None:
    """Checks only_evens when list are all odd numbers."""
    list1: list[int] = [1, 5, 3]
    assert only_evens(list1) == []


def test_concat() -> None:
    """Checks concat when list 1 and list 2 is empty."""
    list1: list[int] = []
    list2: list[int] = []
    assert concat(list1, list2) == []


def test_concat_both_list_have_stuff() -> None:
    """Checks concat when list 1 and list 2 have fulled listed."""
    list1: list[int] = [1, 2, 3]
    list2: list[int] = [4, 5, 6]
    assert concat(list1, list2) == [1, 2, 3, 4, 5, 6]


def test_concat_one_list_have_stuff_other_none() -> None:
    """Checks concat when list 1 have a list and list 2 is a empty list."""
    list1: list[int] = [1, 2, 3]
    list2: list[int] = []
    assert concat(list1, list2) == [1, 2, 3]


def test_sub() -> None:
    """Checks sub when the a_list is empty."""
    a_list: list[int] = []
    start = 0
    end = 4
    assert sub(a_list, start, end) == []


def test_sub_normal() -> None:
    """Checks sub when the a_list is filled in."""
    a_list: list[int] = [10, 20, 30, 40]
    start = 1
    end = 3
    assert sub(a_list, start, end) == [20, 30]


def test_sub_greater_start() -> None:
    """Checks sub when the a_list is filled in plus when start is greater than end."""
    a_list: list[int] = [10, 20]
    start = 5
    end = 1
    assert sub(a_list, start, end) == []


def test_sub_end_greater_than_length() -> None:
    """Checks sub when the a_list is filled in plus when end is greater than start, meaning it should return a_list."""
    a_list: list[int] = [10, 20]
    start = 0
    end = 50
    assert sub(a_list, start, end) == [10, 20]