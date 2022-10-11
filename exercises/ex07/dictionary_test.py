"""EX07 - Dictionary Functions Test."""
__author__ = "730578568"

from exercises.ex07.dictionary import favorite_color, invert, count


def test_invert_empty() -> None:
    """Checks invert when dict is empty."""
    dict1: dict[str, str] = {}
    assert invert(dict1) == {}


def test_invert_one_item() -> None:
    """Checks invert when dict has regular keys and values."""
    dict1: dict[str, str] = {"Chicken": "Beef"}
    assert invert(dict1) == {"Beef": "Chicken"}


def test_invert_multiple_items() -> None:
    """Checks invert when dict has the same keys but differnt values."""
    dict1: dict[str, str] = {"Gym": "No Gym", "Swole": "No Swole", "Muscles": "No Muscles"}
    assert invert(dict1) == {"No Gym": "Gym", "No Swole": "Swole", "No Muscles": "Muscles"}


def test_favorite_color_empty() -> None:
    """Checks favorite color when dict is empty."""
    dict1: dict[str, str] = {}
    assert favorite_color(dict1) == ""


def test_favorite_color_one_item() -> None:
    """Checks favorite color when dict has one item."""
    dict1: dict[str, str] = {"Kevin": "yellow"}
    assert favorite_color(dict1) == "yellow"


def test_favorite_color_multiple_items() -> None:
    """Checks favorite color when dict has multiple items."""
    dict1: dict[str, str] = {"Joe": "yellow", "Alex": "brown", "Kevin": "blue", "Lucas": "blue"}
    assert favorite_color(dict1) == "blue"


def test_count_empty() -> None:
    """Checks count when the list is empty."""
    list1: list[str] = []
    assert count(list1) == {}


def test_count_one_item() -> None:
    """Checks count when list has one item."""
    list1: list[str] = ["bean"]
    assert count(list1) == {"bean": 1}


def test_counter_multiple_items() -> None:
    """Checks count when list has multiple items."""
    list1: list[str] = ["bean", "lean", "green", "bean"]
    assert count(list1) == {"bean": 2, "lean": 1, "green": 1}