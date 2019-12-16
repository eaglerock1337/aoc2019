from copy import deepcopy

import os

from intcode import IntCode

DROID_FILE = "droid.txt"

DIRECTION = {
    "NORTH": (0, -1),
    "SOUTH": (0, 1),
    "EAST": (1, 0),
    "WEST": (-1, 0),
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
        self.map = [[" " for x in range(42)] for y in range(42)]
        self.software = IntCode(software)
        self.opcode = software
        self.startx = 21
        self.starty = 21
        self.xpos = self.startx
        self.ypos = self.starty
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
        self.startx = droid.startx
        self.starty = droid.starty
        self.xpos = droid.xpos
        self.ypos = droid.ypos
        self.steps = droid.steps
        self.direction = droid.direction
        self.software = IntCode(droid.software.opcode)
        self.software.position = droid.software.position
        self.software.relative = droid.software.relative
        self.software.input_list = droid.software.input_list.copy()
        self.software.output = droid.software.output
        self.software.halt = droid.software.halt
        self.opcode = droid.opcode

    def reset(self):
        """
        Reset to factory image. Do not pass GO, do not collect $200.
        """
        self.software = IntCode(self.opcode)
        self.xpos = self.startx
        self.ypos = self.starty
        self.steps = 0
        self.direction = "NORTH"

    def set_direction(self, direction):
        """
        Force the direction of the bot to the specified direction.
        """
        if direction in DIRECTION:
            self.direction = direction
            return True
        else:
            print(f"Invalid direction: {direction}")
            return False

    def turn_left(self):
        """
        Turn the bot left compared to its current direction.
        Yes, this is a very lazy implementation.
        """
        if self.direction == "NORTH":
            self.direction = "WEST"
        elif self.direction == "WEST":
            self.direction = "SOUTH"
        elif self.direction == "SOUTH":
            self.direction = "EAST"
        else:
            self.direction = "NORTH"

    def turn_right(self):
        """
        Turn the bot right compared to its current direction.
        Yes, this is a very lazy impmlementation
        """
        if self.direction == "NORTH":
            self.direction = "EAST"
        elif self.direction == "EAST":
            self.direction = "SOUTH"
        elif self.direction == "SOUTH":
            self.direction = "WEST"
        else:
            self.direction = "NORTH"

    def load_map(self, maplist, startx, starty):
        """
        Input the map from the printable string format. Requires the startx and starty position as well.
        """
        self.map = []
        for line in range(len(maplist)):
            self.map.append([])
            for char in maplist[line]:
                self.map[line].append(char)
        self.startx = startx
        self.starty = starty
        self.xpos = self.startx
        self.ypos = self.starty

    def print_map(self):
        """
        Output the map as a printable or saveable list.
        """
        printed = []
        for row in self.map:
            printed.append("".join(row))

        return printed

    def trace_map(self):
        """
        Trace the map of the room by hugging the right wall until the
        droid returns to the starting coodinates.
        """
        VALID_PATHS = []
        for direction, instruction in DIR_INPUT.items():
            self.software.add_input(instruction)
            output = self.software.run()
            code = output.pop()

            target_xpos = self.xpos + DIRECTION[direction][0]
            target_ypos = self.ypos + DIRECTION[direction][1]

            if code == 0:
                self.map[target_ypos][target_xpos] = "#"
            elif code >= 1:
                VALID_PATHS.append(direction)
                if code == 1:
                    self.map[target_ypos][target_xpos] = "."
            self.reset()

        print(f"Found the following paths: {VALID_PATHS}")

        for path in VALID_PATHS:
            self.set_direction(path)
            while (self.xpos != self.startx or self.ypos != self.starty) or self.steps == 0:
                self.software.add_input(DIR_INPUT[self.direction])
                output = self.software.run()
                code = output.pop()

                if code == 0:
                    wall_xpos = self.xpos + DIRECTION[self.direction][0]
                    wall_ypos = self.ypos + DIRECTION[self.direction][1]
                    self.map[wall_ypos][wall_xpos] = "#"
                    self.turn_left()
                else:
                    self.xpos += DIRECTION[self.direction][0]
                    self.ypos += DIRECTION[self.direction][1]
                    self.steps += 1
                    if code == 1:
                        self.map[self.ypos][self.xpos] = "."
                    else:
                        self.map[self.ypos][self.xpos] = "O"
                    self.turn_right()

            self.reset()

        self.map[self.starty][self.startx] = "S"


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
    program = read_opcode(filename)
    droid = RepairDroid(program)
    droid.trace_map()

    print("The map that was found:")
    map_data = droid.print_map()
    for line in map_data:
        print(line)

    return map_data


def route_finder(droid):
    """
    """
    pass


def squidward_tentacles(programfile, mapfile):
    """
    """
    program = read_opcode(programfile)
    map_data = read_map(mapfile)
    droid_template = RepairDroid(program)
    droid_template.load_map(map_data, 21, 21)
    



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
