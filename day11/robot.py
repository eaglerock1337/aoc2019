import os

from .intcode import IntCode

GRID_SIZE = 100

ROBOT_FILE = "robot.txt"

DIRECTIONS = {
    0: (0, -1),
    1: (1, 0),
    2: (0, 1),
    3: (-1, 0),
}

COLORS = (".", "#")


class BobRoss:
    """
    Emergency Hull Painting Robot
    Supports Happy Little Trees
    """

    def __init__(self, program, gridsize=GRID_SIZE):
        self.direction = 0
        self.panels = []
        self.xpos = int(gridsize / 2) - 1
        self.ypos = int(gridsize / 2) - 1
        self.brain = IntCode(program)
        self.grid = [["." for x in range(gridsize)] for y in range(gridsize)]

    def prime(self):
        """
        Paint the current grid position white.
        """
        self.grid[self.ypos][self.xpos] = "#"

    def run(self):
        """
        Runs the robot.
        """
        while self.brain.halt or len(self.panels) == 0:
            color = COLORS.index(self.grid[self.ypos][self.xpos])
            self.brain.add_input(color)

            output = self.brain.run()

            if output == -1:
                print("Something went wrong with the robot!")
                return False

            newcolor, direction = output

            if tuple((self.xpos, self.ypos)) not in self.panels:
                self.panels.append((self.xpos, self.ypos))

            self.grid[self.ypos][self.xpos] = COLORS[newcolor]

            if direction == 0:
                if self.direction == 0:
                    self.direction = 3
                else:
                    self.direction -= 1

            if direction == 1:
                if self.direction == 3:
                    self.direction = 0
                else:
                    self.direction += 1

            self.xpos += DIRECTIONS[self.direction][0]
            self.ypos += DIRECTIONS[self.direction][1]

        return True

    def print(self):
        """
        Print out the grid of characters.
        """
        for y in range(len(self.grid)):
            row = ""
            for x in range(len(self.grid[0])):
                row += self.grid[y][x]
            print(row)


def read_opcode(filename):
    """
    Read in the opcode from a given filename and return as a list.
    Currently only reads in a single opcode from the file.
    """
    if os.path.basename(os.getcwd()) == "aoc2019":
        filename = os.path.join("day11", filename)

    with open(filename, "r") as opcode_file:
        opcode = opcode_file.readline()

    string_opcode = opcode.split(",")
    return [int(i) for i in string_opcode]


def happy_little_cloud(filename):
    """
    Let's build a happy little cloud.
    """
    program = read_opcode(filename)
    painter = BobRoss(program)
    painter.run()
    painted = len(painter.panels)
    print(f"Painted Panels: {painted}")
    print(f"X Position Range: {min(painter.panels)[0]} - {max(painter.panels)[0]}")
    print(f"Y Position Range: {min(painter.panels)[1]} - {max(painter.panels)[1]}")

    return painted


def happy_little_trees(filename, gridsize=GRID_SIZE):
    """
    Let's paint a happy little tree.
    """
    program = read_opcode(filename)
    painter = BobRoss(program, gridsize)
    painter.prime()
    painter.run()
    print("Identifier:")
    painter.print()


if __name__ == "__main__":
    happy_little_cloud(ROBOT_FILE)
    happy_little_trees(ROBOT_FILE)
