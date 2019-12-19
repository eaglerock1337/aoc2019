from copy import deepcopy

import os

from intcode import IntCode

DROID_FILE = "droid.txt"

MAP_FILE = "map_save.txt"

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

OPPOSITE_DIR = {
    "NORTH": "SOUTH",
    "SOUTH": "NORTH",
    "EAST": "WEST",
    "WEST": "EAST",
}


class RepairDroid:
    """
    Repair Droid for repairing the faulty oxygen system.
    """

    def __init__(self, software, number, direction="NORTH"):
        self.map = [[" " for x in range(42)] for y in range(42)]
        self.software = IntCode(software)
        self.opcode = software
        self.number = number
        self.startx = 21
        self.starty = 21
        self.xpos = self.startx
        self.ypos = self.starty
        self.steps = 0
        if direction in DIRECTION:
            self.direction = direction
        else:
            raise TypeError("The direction input was invalid!")

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
            while (
                self.xpos != self.startx or self.ypos != self.starty
            ) or self.steps == 0:
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


class DroidManager:
    """
    Manage multiple Repair Droids for traversing multiple routes.
    """

    def __init__(self):
        self.droids = []
        self.oxygen_pos = -1
        self.least_steps = -1
        self.longest_time = -1

    def prime(self, program, map_data, direction):
        """
        Prime the first repair droid with the necessary data. Requires the
        opcode program, the map data, and the direction to start with.
        """
        self.droids.append(RepairDroid(program, 0))
        self.droids[0].load_map(map_data, 21, 21)
        self.droids[0].set_direction(direction)

    def find_path(self, droid):
        """
        Attempt to find the shortest and path between the entrance and the oxygen
        system. Will create clones of the droid if multiple pathways are split and
        track of any successful pathways and the closest path. Will also detect the
        time it takes to fill the room with oxygen.
        """
        while True:
            droid.software.add_input(DIR_INPUT[droid.direction])
            output = droid.software.run()
            code = output.pop()
            droid.steps += 1

            if code == 2:
                if self.least_steps == -1 or self.least_steps > droid.steps:
                    self.least_steps = droid.steps
                    self.oxygen_pos = (droid.xpos, droid.ypos)

            droid.xpos += DIRECTION[droid.direction][0]
            droid.ypos += DIRECTION[droid.direction][1]

            directions = DIRECTION.copy()
            directions.pop(OPPOSITE_DIR[droid.direction])
            valid_directions = []

            for look in directions:
                lookx = droid.xpos + DIRECTION[look][0]
                looky = droid.ypos + DIRECTION[look][1]
                if droid.map[looky][lookx] != "#":
                    valid_directions.append(look)

            if len(valid_directions) == 0:
                if self.longest_time < droid.steps:
                    self.longest_time = droid.steps + 1
                return
            elif len(valid_directions) == 1:
                droid.set_direction(valid_directions.pop())
            else:
                droid.set_direction(valid_directions.pop())
                for direction in valid_directions:
                    new_droid = RepairDroid(droid.opcode, len(self.droids))
                    new_droid.clone(droid)
                    new_droid.set_direction(direction)
                    self.droids.append(new_droid)
                    self.find_path(new_droid)


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
    droid = RepairDroid(program, 0)
    droid.trace_map()

    print("The map that was found:")
    map_data = droid.print_map()
    for line in map_data:
        print(line)

    return map_data


def patrick_star(programfile, mapfile, direction):
    """
    Is this the Krusty Krab?
    NO, THIS IS PATRICK.
    EAST? I THOUGHT YOU SAID WEAST!
    """
    program = read_opcode(programfile)
    map_data = read_map(mapfile)
    manager = DroidManager()
    manager.prime(program, map_data, direction)
    manager.find_path(manager.droids[0])
    print(f"Shortest Path: {manager.least_steps}")
    print(f"Oxygen Position: {manager.oxygen_pos}")

    return manager.least_steps, manager.oxygen_pos


def mr_krabs(programfile, mapfile, direction, coordinates):
    """
    Do you smell it? That smell. A kind of smelly smell.
    The smelly smell that smells...smelly.
    """
    program = read_opcode(programfile)
    map_data = read_map(mapfile)
    manager = DroidManager()
    manager.prime(program, map_data, direction)
    manager.droids[0].xpos = 34
    manager.droids[0].ypos = 35
    manager.find_path(manager.droids[0])
    print(f"Time to fill chamber: {manager.longest_time} minutes")

    return manager.longest_time


if __name__ == "__main__":
    spongebob_squarepants(DROID_FILE)
    patrick_star(DROID_FILE, MAP_FILE, "EAST")
    mr_krabs(DROID_FILE, MAP_FILE, "EAST", (34, 35))
