"""EX04 - List Utility Function."""
__author__ = "730578568"

from utils import only_evens


def test_only_evens_empty() -> None:
    list1: list[int] = []
    assert only_evens(list1) == []


def test_only_evens_evens() -> None:
    list1: list[int] = [1,2,3]
    assert only_evens(list1) == [2]

def test_only_evens_odds() -> None:
    list1: list[int] = [1,5,3]
    assert only_evens(list1) == []

from utils import concat


def test_concat() -> None:
    list1: list[int] = []
    list2: list[int] = []
    assert concat(list1, list2) == []

def test_concat_both_list_have_stuff() -> None:
    list1: list[int] = [1,2,3]
    list2: list[int] = [4,5,6]
    assert concat(list1, list2) == [1,2,3,4,5,6]


def test_concat_one_list_have_stuff_other_none() -> None:
    list1: list[int] = [1,2,3]
    list2: list[int] = []
    assert concat(list1, list2) == [1,2,3]

from utils import sub


def test_sub() -> None:
    a_list: list[int] = []
    start = 0
    end = 4
    assert sub(a_list, start, end) == []


def test_sub() -> None:
    a_list: list[int] = [10, 20, 30, 40]
    start = 1
    end = 3
    assert sub(a_list, start, end) == [20, 30]


def test_sub() -> None:
    a_list: list[int] = [10, 1]
    start = 5
    end = 1
    assert sub(a_list, start, end) == []