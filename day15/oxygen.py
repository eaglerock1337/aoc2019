from copy import deepcopy

import os

from intcode import IntCode

DROID_FILE = "droid.txt"

DIRECTION = {
    "NORTH": (0, -1),
    "SOUTH": (0, 1),
    "EAST": (-1, 0),
    "WEST": (1, 0),
}

DIR_INPUT = {
    "NORTH": 1,
    "SOUTH": 2,
    "WEST": 3,
    "EAST": 4,
}

class RepairDroid:
    """
    Repair Droid for repairing the faulty oxygen system.
    """

    def __init__(self, software, direction="NORTH"):
        self.map = [[" " for x in range(100)] for y in range(100)]
        self.software = IntCode(software)
        self.startx = 50
        self.starty = 50
        self.steps = 0
        if direction in DIRECTION:
            self.direction = direction
        else:
            raise TypeError('The direction input was invalid!')

    def clone(self, droid):
        """
        Clone an existing Repair Droid and its current running state.
        """
        if not isinstance(droid, RepairDroid):
            print("You did not pass in a repair droid!")
            return False

        self.map = deepcopy(droid.map)

    def load_map(self, maplist):
        """
        Input the map from the printable string format.
        """
        self.map = []
        for line in maplist:
            self.map.append([])
            for char in line:
                self.map[line].append(char)

    def print_map(self):
        """
        Output the map as a printable or saveable list.
        """
        printed = []
        for row in range(len(self.map)):
            printed.append("".join(row))

        return printed


def read_opcode(filename):
    """
    Read in the opcode from a given filename and return as a list.
    Currently only reads in a single opcode from the file.
    """
    if os.path.basename(os.getcwd()) == "aoc2019":
        filename = os.path.join("day15", filename)

    with open(filename, "r") as opcode_file:
        opcode = opcode_file.readline()

    string_opcode = opcode.split(",")
    return [int(i) for i in string_opcode]


def read_map(filename):
    """
    Read in the map file from a given filename and return as a list.
    """
    if os.path.basename(os.getcwd()) == "aoc2019":
        filename = os.path.join("day15", filename)

    with open(filename, "r") as map_file:
        return map_file.read().splitlines()


def write_map(map_list, filename):
    """
    Write the map file to a given filename from the given map list.
    """
    if os.path.basename(os.getcwd()) == "aoc2019":
        filename = os.path.join("day15", filename)

    with open(filename, "w") as map_file:
        for line in map_list:
            map_file.write(f"{line}\n")

def spongebob_squarepants(filename):
    """
    YUO LIEK KRABBY PATTIES, DON'T YOU SQUIDWARD??????
    """
    pass

def patrick_star(filename):
    """
    Is this the Krusty Krab?
    NO, THIS IS PATRICK.
    EAST? I THOUGHT YOU SAID WEAST!
    """
    pass

if __name__ == "__main__":
    spongebob_squarepants(DROID_FILE)
    # patrick_star(DROID_FILE)
