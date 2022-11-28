"""Tests for linked list utils."""

import pytest
from exercises.ex11.linked_list import Node, last, value_at, max, linkify, scale

__author__ = "730578568"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return its last data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3 


def test_value_at_inside_index() -> None:
    """This test will give back a int based on the index in the inside Node."""
    linked_list = Node(10, Node(20, Node(30, None))) 
    assert value_at(linked_list, 1) == 20


def test_value_at_outside_index() -> None:
    """This test will give back a IndexError as the index is going to be outside the Node."""
    with pytest.raises(IndexError):
        value_at(None, 1)


def test_max_normal_list() -> None:
    """This test will give back a regular max, out of the Node list."""
    linked_list = Node(10, Node(20, Node(30, None)))
    assert max(linked_list) == 30


def test_max_no_list() -> None:
    """This test will give back a ValueError because of the empty Node list."""
    with pytest.raises(ValueError):
        max(None)


def test_linkify_normal_list() -> None:
    """This test will give back a link of Nodes based on the parameters."""
    assert print(linkify([10, 20, 30])) == print("10 -> 20 -> 30 -> None")


def test_linkify_no_items() -> None:
    """This test will give back a return statement of None due to no items."""
    assert print(linkify([])) == print("None")


def test_scale_normal_list() -> None: 
    """This test will give back a scaled Nodes from the original Nodes."""
    assert print(scale(Node(1, Node(2, Node(3, None))), 2)) == print("2 -> 4 -> 6 -> None")


def test_scale_no_items() -> None:
    """This test will give back a return statement of None due to no Nodes."""
    assert scale(None, 1) is None