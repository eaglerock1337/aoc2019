import os

from math import gcd


MAP_FILE = "map.txt"


class AsteroidMap:
    """
    Class for handling the Asteroid Map and all calcuations needed.
    """
    def __init__(self):
        self.asteroid = ()
        self.best_location = (-1, -1)
        self.best_visibility = -1

    def import_map(self, map_data):
        """
        Import the map data from a list of strings and populate map tuple.
        """
        maplist = []
        for line in map_data:
            mapline = []

            for character in line:
                if character == "#":
                    mapline.append(True)
                elif character == ".":
                    mapline.append(False)
                else:
                    print("Error importing mapfile: invalid character!")
                    return False

            maplist.append(tuple(mapline))

        self.asteroid = tuple(maplist)
        return True

    def _is_visible(self, basex, basey, x, y):
        """
        Return whether or not the asteroid at the XY coordinate is visible from
        the base XY coordinates.
        """
        xmove = 1 if basex < x else -1
        ymove = 1 if basey < y else -1
        xdiff = abs(basex - x)
        ydiff = abs(basey - y)

        if xdiff == ydiff == 0:
            return False    # Seeing yourself doesn't count

        divisor = gcd(xdiff, ydiff)
        if divisor == 1:
            return True

        for step in range(1, divisor):
            xpos = basex + int(xdiff / divisor * step * xmove)
            ypos = basey + int(ydiff / divisor * step * ymove)
            if self.asteroid[ypos][xpos]:
                return False

        return True

    def _get_visible(self, basex, basey):
        """
        Get the number of visible asteroids from the provided XY coordinates.
        """
        visible = 0
        for xpos in range(len(self.asteroid[0])):
            for ypos in range(len(self.asteroid)):
                if self.asteroid[ypos][xpos]:
                    if self._is_visible(basex, basey, xpos, ypos):
                        visible += 1

        return visible

    def find_new_base(self):
        """
        Find a new base by determining the asteroid with the most visibility.
        Returns the best visibility and populates variables with the best visibility
        and the XY coordinates of the location.
        """
        for xpos in range(len(self.asteroid[0])):
            for ypos in range(len(self.asteroid)):
                if self.asteroid[ypos][xpos]:
                    visible = self._get_visible(xpos, ypos)
                    if visible > self.best_visibility:
                        self.best_location = (xpos, ypos)
                        self.best_visibility = visible

        return self.best_visibility


def read_mapfile(filename):
    """
    Read in the opcode from a given filename and return as a list.
    Currently only reads in a single opcode from the file.
    """
    if os.path.basename(os.getcwd()) == "aoc2019":
        filename = os.path.join("day10", filename)

    with open(filename, "r") as map_file:
        return  map_file.read().splitlines()


def all_your_base(filename):
    """
    How are you gentlemen !!
    All your base are belong to us.
    You are on the way to destruction.
    WHAT YOU SAY !!
    """
    map_data = read_mapfile(filename)
    move_zig = AsteroidMap()
    move_zig.import_map(map_data)
    best = move_zig.find_new_base()
    print(f"Best visibility: {best}")
    print(f"Best location: {move_zig.best_location}")

    return best, move_zig.best_location


if __name__ == "__main__":
    all_your_base(MAP_FILE)