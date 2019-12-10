from day10.asteroidmap import AsteroidMap, read_mapfile, all_your_base

TEST = [
    ".#..#",
    ".....",
    "#####",
    "....#",
    "...##",
]

TEST_FILE = [
    "......#.#.",
    "#..#.#....",
    "..#######.",
    ".#.#.###..",
    ".#..#.....",
    "..#....#.#",
    "#..#....#.",
    ".##.#..###",
    "##...#..#.",
    ".#....####",
]


def test_asteroidmap_create():
    object = AsteroidMap()
    assert isinstance(object, AsteroidMap)
    assert object.asteroid == ()
    assert object.best_location == (-1, -1)
    assert object.best_visibility == -1


def test_asteroidmap_import_map():
    result = (
        (False, True, False, False, True),
        (False, False, False, False, False),
        (True, True, True, True, True),
        (False, False, False, False, True),
        (False, False, False, True, True),
    )
    object = AsteroidMap()
    assert object.import_map(TEST)
    assert object.asteroid == result


def test_asteroidmap_fail_import_map():
    map_data = ["#..", ".#.", "*.."]
    object = AsteroidMap()
    assert not object.import_map(map_data)


def test_asteroidmap_is_visible():
    object = AsteroidMap()
    assert object.import_map(TEST)
    assert object._is_visible(2, 2, 1, 0)
    assert not object._is_visible(2, 2, 0, 2)
    assert object._is_visible(3, 2, 1, 0)
    assert object._is_visible(4, 0, 4, 2)
    assert not object._is_visible(4, 0, 4, 4)
    assert not object._is_visible(3, 2, 3, 2)


def test_asteroidmap_get_visible():
    object = AsteroidMap()
    assert object.import_map(TEST)
    assert object._get_visible(1, 0) == 7
    assert object._get_visible(4, 0) == 7
    assert object._get_visible(0, 2) == 6
    assert object._get_visible(1, 2) == 7
    assert object._get_visible(2, 2) == 7
    assert object._get_visible(3, 2) == 7
    assert object._get_visible(4, 2) == 5
    assert object._get_visible(4, 3) == 7
    assert object._get_visible(3, 4) == 8
    assert object._get_visible(4, 4) == 7


def test_asteroidmap_find_new_base():
    object = AsteroidMap()
    assert object.import_map(TEST)
    assert object.find_new_base() == 8
    assert object.best_visibility == 8
    assert object.best_location == (3, 4)

def test_read_mapfile():
    filename = "test.txt"
    result = read_mapfile(filename)
    assert TEST_FILE == result


def test_asteroidmap_all_your_base_1():
    filename = "test.txt"
    vis, loc = all_your_base(filename)
    assert vis == 33
    assert loc == (5, 8)


def test_asteroidmap_all_your_base_2():
    filename = "test2.txt"
    vis, loc = all_your_base(filename)
    assert vis == 35
    assert loc == (1, 2)


def test_asteroidmap_all_your_base_3():
    filename = "test3.txt"
    vis, loc = all_your_base(filename)
    assert vis == 41
    assert loc == (6, 3)


def test_asteroidmap_all_your_base_4():
    filename = "test4.txt"
    vis, loc = all_your_base(filename)
    assert vis == 210
    assert loc == (11, 13)