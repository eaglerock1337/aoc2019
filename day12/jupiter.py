import os

from copy import deepcopy
from math import gcd
from re import compile


DATA_FILE = "moons.txt"


class Jupiter:
    """
    Simulator for tracking Jupiter's 4 largest moons and their orbits in respect to each other.
    """

    def __init__(self):
        self.position = []
        self.velocity = [[0 for x in range(3)] for y in range(4)]
        self.moons = 0
        self.coords = 0
        self.steps = 0

    def import_data(self, data):
        """
        Formats strings of moon data taken in as XYZ coordinates (e.g. "<x=1, y=-2, z=30>")
        """
        digits = compile(r"-?\d+")
        for line in data:
            numbers = digits.findall(line)
            self.position.append([int(num) for num in numbers])
        self.moons = len(self.position)
        self.coords = len(self.position[0])

    def step(self, steps=1):
        """
        Compute steps in the simulation. Takes an optional number of steps, defaulting to 1 step.
        """
        for _ in range(steps):
            self.steps += 1

            # Compute gravity
            for moon in range(self.moons):
                for coord in range(self.coords):
                    for othermoon in range(self.moons):
                        if self.position[othermoon][coord] > self.position[moon][coord]:
                            self.velocity[moon][coord] += 1
                        elif (
                            self.position[othermoon][coord] < self.position[moon][coord]
                        ):
                            self.velocity[moon][coord] -= 1

            # Apply velocity
            for moon in range(self.moons):
                for coord in range(self.coords):
                    self.position[moon][coord] += self.velocity[moon][coord]

    def step_coord(self, coord):
        """
        Step a single coordinate in time one step.
        """
        self.steps += 1

        # Compute gravity
        for moon in range(self.moons):
            for othermoon in range(self.moons):
                if self.position[othermoon][coord] > self.position[moon][coord]:
                    self.velocity[moon][coord] += 1
                elif self.position[othermoon][coord] < self.position[moon][coord]:
                    self.velocity[moon][coord] -= 1

        # Apply velocity
        for moon in range(self.moons):
            self.position[moon][coord] += self.velocity[moon][coord]

    def get_energy(self):
        """
        Return the total energy in the system (kinetic + potential energy).
        """
        total = 0
        for moon in range(self.moons):
            potential = 0
            kinetic = 0

            for coord in range(self.coords):
                potential += abs(self.position[moon][coord])
                kinetic += abs(self.velocity[moon][coord])

            total += potential * kinetic

        return total

    def _get_period(self, coord):
        """
        Get the period for a coordinate that it takes to reset to the original position.
        """
        self.steps = 0
        initial_pos = deepcopy(self.position)
        initial_vel = deepcopy(self.velocity)

        while True:
            self.step_coord(coord)
            if self.position == initial_pos and self.velocity == initial_vel:
                return self.steps

    def simulate(self):
        """
        Simulate the universe, and see how many steps are necessary to return to the initial state.
        """
        periods = []
        for coord in range(self.coords):
            periods.append(self._get_period(coord))

        x_per, y_per, z_per = periods

        xy_per = int(x_per * y_per / gcd(x_per, y_per))
        xyz_per = int(xy_per * z_per / gcd(xy_per, z_per))

        return xyz_per


def read_moons(filename):
    """
    Read in input file containing Jupiter's moons' starting points in XYZ format.
    Returns a list of lines in the format "<x=#, y=#, z=#>"
    """
    if os.path.basename(os.getcwd()) == "aoc2019":
        filename = os.path.join("day12", filename)

    with open(filename, "r") as moon_file:
        return moon_file.readlines()


def thats_no_moon(filename, steps):
    """
    That's no moon...it's a space station.
    """
    moon_data = read_moons(filename)
    jupiter = Jupiter()
    jupiter.import_data(moon_data)
    jupiter.step(steps)

    energy = jupiter.get_energy()
    print(f"Total Energy at Step {steps}: {energy}")

    return energy


def ricks_car_battery(filename):
    """
    Well, that sounds like slavery with extra steps.
    """
    moon_data = read_moons(filename)
    jupiter = Jupiter()
    jupiter.import_data(moon_data)
    steps = jupiter.simulate()

    print(f"It took a total of {steps} steps to return to the initial state.")

    return steps


if __name__ == "__main__":
    thats_no_moon(DATA_FILE, 1000)
    ricks_car_battery(DATA_FILE)
