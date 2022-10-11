"""EX07 - Dictionary Functions."""
__author__ = "730578568"


def invert(orig_dictionary: dict[str, str]) -> dict[str, str]:
    """This function inverts the original dictionary."""
    invertdictionary: dict[str, str] = {} 
    for key in orig_dictionary:
        for x in invertdictionary:
            if x == orig_dictionary[key]:
                raise KeyError("there are multiple keys that look the same")
        invertdictionary[orig_dictionary[key]] = key 
    return invertdictionary


def favorite_color(dict1: dict[str, str]) -> str:
    """This function finds the favorite color of the dictionary."""
    fav_count_dict: dict[str, int] = {}
    for key in dict1:
        if dict1[key] in fav_count_dict:
            fav_count_dict[dict1[key]] += 1
        else: 
            fav_count_dict[dict1[key]] = 1
    counter: int = 0
    fav_color: str = ""
    for x in fav_count_dict:
        current_value: int = fav_count_dict[x]
        if current_value > counter:
            counter = current_value
            fav_color = x
    return fav_color


def count(list1: list[str]) -> dict[str, int]:
    """This function counts the variables in list and display it as a dictionary."""
    counterdictionary: dict[str, int] = {}
    for key in list1:
        if key in counterdictionary:
            counterdictionary[key] += 1
        else:
            counterdictionary[key] = 1
    return counterdictionary