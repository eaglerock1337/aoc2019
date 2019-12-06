import os
import sys


MAPFILE = "input.txt"


class Body:
    """
    Class for defining a celestial body in the Universal Orbit Map.
    """

    def __init__(self, name):
        self.name = name
        self.parent = ""
        self.satellites = []

    def set_parent(self, body):
        """
        Set the parent body that this Body orbits around.
        """
        if self.parent == "":
            self.parent = body
            return True
        else:
            print(
                f"Cannot add parent {body} to {self.name}: already has parent {self.parent}!"
            )
            return False

    def add_satellite(self, body):
        """
        Add a direct orbit to the Body's satellite list.
        """
        if body in self.satellites:
            print(f"Cannot add {body} to {self.name} satellite list: Already in list!")
            return False

        self.satellites.append(body)
        return True

    def no_of_satellites(self):
        """
        Return the number of satellites for this Body.
        """
        return len(self.satellites)


class OrbitMap:
    """
    Class for defining the Universal Orbit Map.
    """

    def __init__(self):
        self.bodies = {}

    def add_orbit(self, orbit):
        """
        Add a single orbit to the map, creating the Body objects if necessary.
        """
        try:
            parent, satellite = orbit.split(")")
        except ValueError:
            print(f"Error: Improper orbit string: {orbit}")
            return False

        missing_bodies = (x for x in [parent, satellite] if x not in self.bodies)

        for body in missing_bodies:
            self.bodies[body] = Body(body)

        if not self.bodies[parent].add_satellite(satellite):
            return False

        if not self.bodies[satellite].set_parent(parent):
            return False

        return True

    def load_map_data(self, data):
        """
        Bulk load map data from a list of orbits.
        """
        for line in data:
            if not self.add_orbit(line):
                print(f"Error loading map data: String {line} returned errors!")
                return False

        return True

    def get_orbits(self, body):
        """
        Return the number of direct and indirect orbits for the provided body.
        """
        total_orbits = 0

        if self.bodies[body].parent == "":
            return total_orbits
        else:
            return self.get_orbits(self.bodies[body].parent) + 1

    def get_checksum(self):
        """
        Return the checksum for the Orbit Map, as defined by the total of direct
        and indirect orbits around the center of mass.
        """
        if "COM" not in self.bodies:
            print("Checksum Error: COM is not in the list of bodies!")
            return -1

        total_orbits = 0

        for body in self.bodies:
            total_orbits += self.get_orbits(body)

        return total_orbits

    def validate_orbits(self):
        """
        Validate the map list to ensure a proper Orbit Map was created.
        """
        if "COM" not in self.bodies:
            print("Validate Error: COM is not in the list of bodies!")
            return False

        for body in self.bodies:
            if self.bodies[body].parent == "" and body != "COM":
                print(f"Validate Error: {body} is missing its parent body!")
                return False

        return True


def read_map_file(filename):
    """
    Read map data from the supplied filename.
    """
    if os.path.basename(os.getcwd()) == "aoc2019":
        filename = os.path.join("day6", filename)

    with open(filename, "r") as map_file:
        return map_file.read().splitlines()


def neil_degrasse_tyson(input_file):
    """
    IMMA TAKE YOU ON A JOURNEY ON MY SHIP OF THE IMAGINATION.
    PLUTO ISN'T A PLANET, BITCH! GET OVER IT!
    OH, YOU DON'T AGREE? YOU KNOW BETTER THAN SCIENCE, BITCH?
    WATCH OUT GUYS, WE'RE DEALING WITH A BADASS OVER HERE!
    """
    map_data = read_map_file(input_file)
    orbit_map = OrbitMap()
    orbit_map.load_map_data(map_data)

    if not orbit_map.validate_orbits():
        print(f"Data was not properly validated!")
        return -1

    result = orbit_map.get_checksum()
    print(f"Orbit map loaded successfully! Checksum: {result}")

    return result


if __name__ == "__main__":
    neil_degrasse_tyson(MAPFILE)
