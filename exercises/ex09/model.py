"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt


__author__ = "730578568"


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)

    def distance(self, z: Point) -> float:
        """This function tells us the distance between two different points."""
        y_difference: float = z.y - self.y
        x_difference: float = z.x - self.x
        distance: float = sqrt(y_difference**2 + x_difference**2)
        return distance


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    # Part 1) Define a method named `tick` with no parameters.
    # Its purpose is to reassign the object's location attribute
    # the result of adding the self object's location with its
    # direction. Hint: Look at the add method.
    def tick(self) -> None:
        """This function checks whether the cell is sick based on the constant infected and if the cell is sick after the recovery time is up the cell is immune."""
        self.location = self.location.add(self.direction)
        if self.sickness >= constants.INFECTED:
            self.sickness += 1
        if self.sickness == constants.RECOVERY_PERIOD:
            self.sickness = constants.IMMUNE
        
    def color(self) -> str:
        """Return the color representation of a cell."""
        if self.is_vulnerable():
            return "gray"
        elif self.is_infected():
            return "red"
        elif self.is_immune():
            return "blue"
        return ""
    
    def contract_disease(self) -> None:
        """This function tells us how many of the dots contracted the diseases."""
        self.sickness = constants.INFECTED

    def is_vulnerable(self) -> bool:
        """This function tells us how many of the dots are vulnerable to the diseases."""
        if self.sickness == constants.VULNERABLE:
            return True
        else:
            return False

    def is_infected(self) -> bool:
        """This function tells us how many of the dots are infected with the diseases."""
        if self.sickness >= constants.INFECTED:
            return True
        else:
            return False

    def contact_with(self, touch_cell: Cell) -> None:
        """This function checks the contact between infected and uninfected cells."""
        if self.is_vulnerable() and touch_cell.is_infected():
            self.contract_disease()
        elif self.is_infected() and touch_cell.is_vulnerable():
            touch_cell.contract_disease()
    
    def immunize(self) -> None:
        """This function tells us how many cells are immune to the diseases after they contract it."""
        self.sickness = constants.IMMUNE
    
    def is_immune(self) -> bool:
        """This function tells us how many of the dots are immune to the diseases."""
        if self.sickness == constants.IMMUNE:
            return True
        else:
            return False

    
class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0
    
    def __init__(self, cells: int, speed: float, number_of_ic: int, num_of_immune_cells: int = 0):
        """Initialize the cells with random locations and directions."""
        if number_of_ic >= cells or number_of_ic <= 0:
            raise ValueError('error')
        if num_of_immune_cells + number_of_ic >= cells or num_of_immune_cells < 0:
            raise ValueError(" ")
        self.population = []
        for _ in range(0, cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            if number_of_ic > 0:
                cell.sickness = constants.INFECTED
                number_of_ic -= 1
            elif num_of_immune_cells > 0:
                cell.sickness = constants.IMMUNE
                num_of_immune_cells -= 1
            self.population.append(cell) 
           
    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        elif cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0
        elif cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0 
        elif cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0

    def check_contacts(self) -> None:
        """This function check the contacts between infected and uninfected cells based on location and population."""
        count: int = 1
        for i in self.population:
            for x in range(count, len(self.population)):
                if i.location.distance(self.population[x].location) < constants.CELL_RADIUS:
                    i.contact_with(self.population[x])
            count += 1
        
    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        for i in self.population:
            if i.sickness >= constants.INFECTED:
                return False
        return True 