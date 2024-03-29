import os

from operator import itemgetter

"""
Advent of Code 2019
Day 3 Challenge

Find closest intersection of two wires along a grid, starting from the same point
Also using this as a thinly-veiled excuse to practice using PyTest
"""

PLOT_FILE = "input.txt"


def import_plots(filename):
    """
    Input lines of plots as strings
    """
    if os.path.basename(os.getcwd()) == "aoc2019":
        filename = os.path.join("day3", filename)

    with open(os.path.abspath(filename), "r") as plotfile:
        return plotfile.read().splitlines()


def convert_plot(plot):
    """
    Convert plot from a string to a list of instructions
    """
    plots = plot.split(",")
    instructions = []
    for i in plots:
        instructions.append((str(i[0]), int(i[1:])))
    return instructions


def plot_wire(plot):
    """
    Create a list of tuples with the XY coordinates of every point the wire is on.
    """
    coords = []
    position = [0, 0]
    directions = {"R": [1, 0], "L": [-1, 0], "U": [0, 1], "D": [0, -1]}
    instructions = convert_plot(plot)

    for direction, distance in instructions:
        for _ in range(distance):
            position = [a + b for a, b in zip(position, directions.get(direction))]
            coords.append(tuple(position))

    return coords


def get_intersections(plot1, plot2):
    """
    Get intersections between two plots and calculate Manhattan distance of the intersection
    """
    intersections = set(plot1).intersection(plot2)
    results = []
    for (x, y) in intersections:
        distance = abs(x) + abs(y)
        travel = plot1.index((x, y)) + plot2.index((x, y)) + 2
        results.append((x, y, distance, travel))
    return results


def dont_stop_believin(plotfile):
    """
    He took a midnight train goin' AAAAAAAAAAAAAANNYWHEEEEEEEEEEEEEEEEEEERE
    """
    hansel, gretel = import_plots(plotfile)
    hansel_crumbs = plot_wire(hansel)  # What kind of a name is Hansel, anyway?
    gretel_crumbs = plot_wire(gretel)
    matches = get_intersections(hansel_crumbs, gretel_crumbs)

    part1_results = sorted(matches, key=itemgetter(2))
    part2_results = sorted(matches, key=itemgetter(3))
    part1_answer = part1_results[0]
    part2_answer = part2_results[0]

    print("Here's the results:")
    print(f"There were a total of {len(matches)} intersections.")
    print(
        f"The closest intersection was at the coordinates {part1_answer[0]}, {part1_answer[1]}."
    )
    print(f"Part 1 answer: The absolute Manhattan distance was {part1_answer[2]}!")
    print(
        f"The least traveled intersection was at the coordinates {part2_answer[0]}, {part2_answer[1]}."
    )
    print(f"Part 2 answer: The travelled Manhattan distance was {part2_answer[3]}!")

    return part1_answer, part2_answer


if __name__ == "__main__":
    dont_stop_believin(PLOT_FILE)
