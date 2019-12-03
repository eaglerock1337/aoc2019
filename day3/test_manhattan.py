from day3 import manhattan

# Tests

def test_import_plots():
    plotfile = "test.txt"
    result1 = "R4,D3,L2,U1"
    result2 = "U1,R2,D2,R3"
    plot1, plot2 = manhattan.import_plots(plotfile)
    assert plot1 == result1
    assert plot2 == result2


def test_convert_plot():
    plot = "R4,D3,L2,U1"
    result = [("R", 4), ("D", 3), ("L", 2), ("U", 1)]
    assert manhattan.convert_plot(plot) == result


def test_plot_wire():
    plot = "R4,D3,L2,U1"
    result = [
        (1, 0),
        (2, 0),
        (3, 0),
        (4, 0),
        (4, -1),
        (4, -2),
        (4, -3),
        (3, -3),
        (2, -3),
        (2, -2),
    ]
    assert manhattan.plot_wire(plot) == result


def test_get_intersections():
    plot1 = [
        (1, 0),
        (2, 0),
        (3, 0),
        (4, 0),
        (4, -1),
        (4, -2),
        (4, -3),
        (3, -3),
        (2, -3),
        (2, -2),
    ]
    plot2 = [(0, 1), (1, 1), (2, 1), (2, 0), (2, -1), (3, -1), (4, -1), (5, -1)]
    result = [(2, 0, 2, 6), (4, -1, 5, 12)]
    assert manhattan.get_intersections(plot1, plot2) == result


def test_dont_stop_believin():
    PLOT_FILE = "test.txt"
    part1_answer, part2_answer = manhattan.dont_stop_believin(PLOT_FILE)
    assert part1_answer[2] == 2
    assert part2_answer[3] == 6
