import os

from re import compile


# string = each line
# digits = compile(r"-?\d+")
# digits.findall(string)

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
                        elif self.position[othermoon][coord] < self.position[moon][coord]:
                            self.velocity[moon][coord] -= 1 

            # Apply velocity
            for moon in range(self.moons):
                for coord in range(self.coords):
                    self.position[moon][coord] += self.velocity[moon][coord]


def read_moons(filename):
    """
    Read in input file containing Jupiter's moons' starting points in XYZ format.
    Returns a list of lines in the format "<x=#, y=#, z=#>"
    """
    if os.path.basename(os.getcwd()) == "aoc2019":
        filename = os.path.join("day12", filename)

    with open(filename, "r") as moon_file:
        return moon_file.readlines()


if __name__ == "__main__":
    pass