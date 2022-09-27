"""EX04 - List Utility Function."""
__author__ = "730578568"


def only_evens(list1: list[int]) -> list[int]:
    """This function finds the even numbers of the list the user puts in."""
    i: int = 0
    list2: list[int] = list()
    while i < len(list1):
        if list1[i] % 2 == 0:
            list2.append(list1[i])
        i += 1
    return list2


def concat(list1: list[int], list2: list[int]) -> list[int]:
    """This function adds all the elements of the first list with all the elements of the second list."""
    i: int = 0
    list3: list[int] = list()
    while i < len(list1):
        list3.append(list1[i])
        i += 1
    i = 0
    while i < len(list2):
        list3.append(list2[i])
        i += 1
    return list3


def sub(a_list: list[int], start: int, end: int) -> list[int]:
    """This function returns from start to end indexes, but not including end."""
    i: int = start 
    b_list: list[int] = []
    if start < 0:
        i = 0
    if start >= len(a_list):
        return b_list
    if end > len(a_list):
        end = len(a_list)
    if end == start:
        return a_list
    if end < 0 or end <= 0:
        return []
    if len(a_list) == 0:
        return []
    while i < end:
        b_list.append(a_list[i])
        i += 1
    return b_list