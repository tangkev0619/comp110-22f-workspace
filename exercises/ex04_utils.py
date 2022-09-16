"""EX04 - List Utility Function."""
__author__ = "730578568"


def all(list1: list[int], random: int) -> bool:
    """This function is used to check whether or not if the given number matches with the list for all."""
    if len(list1) == 0:
        return False
    i: int = 0
    while i < len(list1):
        if list1[i] != random:
            return False
        i += 1
    return True 


def max(input: list[int]) -> int:
    """This function is used to check the integers that the user puts in and see which is the max integer of the other numbers."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty list")
    i: int = 0
    valone: int = input[0]
    while i < len(input):
        if valone < input[i]:
            valone = input[i] 
        i += 1
    return valone 


def is_equal(input1: list[int], input2: list[int]) -> bool:
    """This function is used to check if both list are equal to each other if not it wil return False, if correct it will return True."""
    if len(input1) != len(input2):
        return False
    i: int = 0
    while i < len(input1):
        if input1[i] != input2[i]:
            return False
        i += 1
    return True