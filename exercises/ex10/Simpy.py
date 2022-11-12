"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730578568"


class Simpy:
    """This is class Simpy."""
    values: list[float]

    def __init__(self, ones: list[float]) -> None:
        """This function's purpose is to initialize the values attribute of the newly constructed Simpy object to the argument passed in."""
        self.values = ones 

    def __repr__(self) -> str:
        """This function's purpose is to print ones."""
        return f"Simpy({self.values})"

    def fill(self, x: float, y: int) -> None:
        """This function fills Simpy's values with a specific number of repeating values."""
        result: list[float] = []
        for i in range(y):
            result.append(x)
        self.values = result

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """This function's purpose is to fill in the values attribute with range of values, like the range built-in function, but in terms of floats."""
        result: list[float] = []
        if start < stop:
            while start < stop:
                result.append(start)
                start += step
        else:
            while start > stop:
                result.append(start)
                start += step
        self.values = result

    def sum(self) -> float:
        """This functions purpose is to sum what's in the self.values."""
        return sum(self.values)
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """This function's purpose is to add together different floats together."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float): 
            for item in self.values: 
                result.values.append(item + rhs)
        else: 
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.values.append(self.values[i] + rhs.values[i])
        return result

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """This function's purpose is to take the power of different floats and see what they are together."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float): 
            for item in self.values: 
                result.values.append(item ** rhs)
        else: 
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.values.append(self.values[i] ** rhs.values[i])
        return result

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """This function's purpose is to see if the variables or floats are equal to each other."""
        result: list[bool] = []
        if isinstance(rhs, float): 
            for item in self.values: 
                result.append(item == rhs)
        else: 
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.append(self.values[i] == rhs.values[i])
        return result
    
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """This function's purpose is to see if the variables or float are greater than each other."""
        result: list[bool] = []
        if isinstance(rhs, float): 
            for item in self.values: 
                result.append(item > rhs)
        else: 
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.append(self.values[i] > rhs.values[i])
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """This function overloads the subscription notation to filter with a mask."""
        result: Simpy = Simpy([])
        if isinstance(rhs, int):
            return self.values[rhs]
        else: 
            for i in range(len(self.values)):
                if rhs[i] is True:
                    result.values.append(self.values[i])
        return result 