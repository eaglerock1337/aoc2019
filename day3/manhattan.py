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
    with open(filename, "r") as plotfile:
        return plotfile.read().splitlines()


def convert_plot(plot):
    """
    Convert plot from a string to a list of instructions
    """
    plots = plot.split(',')
    instructions = []
    for i in plots:
        instructions.append( (str(i[0]), int(i[1:])) )
    return instructions


def plot_wire(plot):
    """
    Create a list of tuples with the XY coordinates of every point the wire is on.
    """
    coords = []
    position = [0, 0]
    directions = {
        "R": [1, 0],
        "L": [-1, 0],
        "U": [0, 1],
        "D": [0, -1]
    }
    instructions = convert_plot(plot)

    for direction, distance in instructions:
        for i in range(distance):
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
        results.append( (x, y, distance, travel) )
    return results


def dont_stop_believin():
    """
    He took a midnight train goin' AAAAAAAAAAAAAANNYWHEEEEEEEEEEEEEEEEEEERE
    """
    hansel, gretel = import_plots(PLOT_FILE)
    hansel_crumbs = plot_wire(hansel)   # What kind of a name is Hansel, anyway?
    gretel_crumbs = plot_wire(gretel)
    matches = get_intersections(hansel_crumbs, gretel_crumbs)

    part1_results = sorted(matches, key=itemgetter(2))
    part2_results = sorted(matches, key=itemgetter(3))
    part1_answer = part1_results[0]
    part2_answer = part2_results[0]

    print("Here's the results:")
    print(f"There were a total of {len(matches)} intersections.")
    print(f"The closest intersection was at the coordinates {part1_answer[0]}, {part1_answer[1]}.")
    print(f"Part 1 answer: The absolute Manhattan distance was {part1_answer[2]}!")
    print(f"The least traveled intersection was at the coordinates {part2_answer[0]}, {part2_answer[1]}.")
    print(f"Part 2 answer: The travelled Manhattan distance was {part2_answer[3]}!")


if __name__ == "__main__":
    dont_stop_believin()


"""""
Tests
"""""

def test_import_plots():
    plotfile = "test.txt"
    result1 = "R4,D3,L2,U1"
    result2 = "U1,R2,D2,R3"
    plot1, plot2 = import_plots(plotfile)
    assert plot1 == result1
    assert plot2 == result2


def test_convert_plot():
    plot = "R4,D3,L2,U1"
    result = [("R", 4), ("D", 3), ("L", 2), ("U", 1)]
    assert convert_plot(plot) == result


def test_plot_wire():
    plot = "R4,D3,L2,U1"
    result = [
        (1,  0), (2,  0), (3,  0), (4,  0),
        (4, -1), (4, -2), (4, -3),
        (3, -3), (2, -3),
        (2, -2)
    ]
    assert plot_wire(plot) == result


def test_get_intersections():
    plot1 = [ (1, 0), (2, 0), (3, 0), (4, 0), (4, -1), (4, -2), (4, -3), (3, -3), (2, -3), (2, -2) ]
    plot2 = [ (0, 1), (1, 1), (2, 1), (2, 0), (2, -1), (3, -1), (4, -1), (5, -1) ]
    result = [ (2, 0, 2, 6), (4, -1, 5, 12) ]
    assert get_intersections(plot1, plot2) == result