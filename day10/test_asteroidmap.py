from day10.asteroidmap import AsteroidMap, read_mapfile, all_your_base, dr_evil

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
    assert object.basex == -1
    assert object.basey == -1
    assert object.best_visibility == -1
    assert object.vaporized == []


def test_asteroidmap_import_map():
    result = [
        [False, True, False, False, True],
        [False, False, False, False, False],
        [True, True, True, True, True],
        [False, False, False, False, True],
        [False, False, False, True, True],
    ]
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
    assert object.basex == 3
    assert object.basey == 4


def test_asteroidmap_scan_for_target():
    object = AsteroidMap()
    assert object.import_map(TEST)
    assert object.find_new_base() == 8
    targets = object._scan_for_target()
    assert targets == [(3, 2), (4, 0), (4, 2), (4, 3), (4, 4), (0, 2), (1, 2), (2, 2)]


def test_asteroidmap_vaporize():
    result = [(3, 2), (4, 0), (4, 2), (4, 3), (4, 4), (0, 2), (1, 2), (2, 2), (1, 0)]
    object = AsteroidMap()
    assert object.import_map(TEST)
    assert object.find_new_base() == 8
    assert object.vaporize()
    assert object.vaporized == result


def test_asteroidmap_fail_vaporize():
    object = AsteroidMap()
    assert object.import_map(TEST)
    assert not object.vaporize()


def test_asteroidmap_vaporize_validate():
    testfile = "test4.txt"
    map_data = read_mapfile(testfile)
    object = AsteroidMap()
    assert object.import_map(map_data)
    assert object.find_new_base()
    assert object.vaporize()
    assert object.get_vaporized(1) == (11, 12)
    assert object.get_vaporized(2) == (12, 1)
    assert object.get_vaporized(3) == (12, 2)
    assert object.get_vaporized(10) == (12, 8)
    assert object.get_vaporized(20) == (16, 0)
    assert object.get_vaporized(50) == (16, 9)
    assert object.get_vaporized(100) == (10, 16)
    assert object.get_vaporized(199) == (9, 6)
    assert object.get_vaporized(200) == (8, 2)
    assert object.get_vaporized(201) == (10, 9)
    assert object.get_vaporized(299) == (11, 1)
    assert len(object.vaporized) == 299


def test_read_mapfile():
    filename = "test.txt"
    result = read_mapfile(filename)
    assert TEST_FILE == result


def test_all_your_base_1():
    filename = "test.txt"
    vis, loc = all_your_base(filename)
    assert vis == 33
    assert loc == (5, 8)


def test_all_your_base_2():
    filename = "test2.txt"
    vis, loc = all_your_base(filename)
    assert vis == 35
    assert loc == (1, 2)


def test_all_your_base_3():
    filename = "test3.txt"
    vis, loc = all_your_base(filename)
    assert vis == 41
    assert loc == (6, 3)


def test_all_your_base_4():
    filename = "test4.txt"
    vis, loc = all_your_base(filename)
    assert vis == 210
    assert loc == (11, 13)


def test_dr_evil():
    filename = "test4.txt"
    answer = dr_evil(filename)
    assert answer == 802
