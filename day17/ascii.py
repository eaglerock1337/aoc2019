import os

from intcode import IntCode

ASCII_FILE = "ascii.txt"

ASCII_ROUTINE = [
    "A,B,A,C,B,C,B,C,A,C",
    "R,12,L,6,R,12",
    "L,8,L,6,L,10",
    "R,12,L,10,L,6,R,10",
]


class ASCII:
    """
    Aft Scaffolding Control and Information Interface
    """

    def __init__(self, software):
        self.program = IntCode(software)
        self.map = []
        self.mapstring = ""
        self.intersections = []

    def build_map(self):
        """
        Builds a map from the ASCII output of the IntCode program. Assigns
        results to a map of characters as well as a single string.
        """
        output = self.program.run()
        while output[-1] == 10:
            output.pop()

        output.reverse()
        self.map.append([])
        maprow = 0

        while len(output) > 0:
            char = chr(output.pop())
            self.mapstring += char

            if char == "\n":
                self.map.append([])
                maprow += 1
            else:
                self.map[maprow].append(char)
    
    def _is_intersection(self, xpos, ypos):
        """
        Check the neighbors of the XY position and return the number of
        neighbors that are a scaffold space.
        """
        results = 0
        for xshift, yshift in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            if self.map[ypos + yshift][xpos + xshift] in ["#", "<", ">", "^", "v"]:
                results += 1

        if results == 4:
            return True
        else:
            return False

    def _get_intersections(self):
        """
        Detect all the intersections on the map and populate the list with
        tuples of the XY intersections.
        """
        for ypos in range(1, len(self.map) - 1):
            for xpos in range(1, len(self.map[0]) - 1):
                if self.map[ypos][xpos] == "#":
                    if self._is_intersection(xpos, ypos):
                        self.intersections.append((xpos, ypos))

    def align(self):
        """
        Return the alignment parameter sum.
        """
        self._get_intersections()

        print(self.mapstring)

        sum = 0
        for x, y in self.intersections:
            sum += x * y

        return sum

    def notify(self, routine):
        """
        Primes the robot to perform the notification routine. Sets the initial
        opcode bit, primes the input, and prepares for the run. The run will
        return the amount of dust collected during the routine, which will
        be returned by the function.
        """
        self.program.opcode[0] = 2
        output = self.program.run()

        for line in routine:
            for char in line:
                self.program.add_input(ord(char))
            self.program.add_input(10)

        self.program.add_input(ord("n"))
        self.program.add_input(10)

        output = self.program.run()    
        result = output.pop()
        return result


def read_opcode(filename):
    """
    Read in the opcode from a given filename and return as a list.
    Currently only reads in a single opcode from the file.
    """
    if os.path.basename(os.getcwd()) == "aoc2019":
        filename = os.path.join("day17", filename)

    with open(filename, "r") as opcode_file:
        opcode = opcode_file.readline()

    string_opcode = opcode.split(",")
    return [int(i) for i in string_opcode]


def wayne(filename):
    """
    I'd have to say...asphinctersayswhat?
    ...What?
    Exactly.
    """
    software = read_opcode(filename)
    robot = ASCII(software)
    robot.build_map()
    answer = robot.align()

    print(f"The alignment sum is: {answer}")
    return answer


def garth(filename, routine):
    """
    Did you ever find Bugs Bunny attractive when
    he put on a dress and played a girl bunny?
    """
    software = read_opcode(filename)
    robot = ASCII(software)
    dust = robot.notify(routine)

    print(f"The amount of dust collected is: {dust}")
    return dust


if __name__ == "__main__":
    wayne(ASCII_FILE)
    garth(ASCII_FILE, ASCII_ROUTINE)