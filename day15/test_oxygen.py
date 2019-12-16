import pytest

from day15.intcode import IntCode
from day15.oxygen import (
    RepairDroid,
    read_opcode,
    read_map,
    write_map,
    spongebob_squarepants,
    patrick_star
)

TEST = [3, 10, 104, 1, 104, 1, 6, 10, 11, 99, 0, 0]

TEST_MAP = [
    " #### ",
    "#....#",
    "#.##.#",
    "#.O#.#",
    " #...#",
    "  ### ",
]

TEST_MAP_STRING = " #### \n#....#\n#.##.#\n#.O#.#\n #...#\n  ### \n"

# Tests


def test_repairdroid_create():
    blank = [[" " for x in range(100)] for y in range(100)]
    object = RepairDroid(TEST)
    assert object.map == blank
    assert object.software.opcode[: len(TEST)] == TEST
    assert object.opcode == TEST
    assert object.startx == 50
    assert object.starty == 50
    assert object.xpos == 50
    assert object.ypos == 50
    assert object.steps == 0
    assert object.direction == "NORTH"

    object2 = RepairDroid(TEST, "WEST")
    assert object2.direction == "WEST"


def test_repairdroid_fail_create():
    with pytest.raises(TypeError, match=r".*direction input was invalid.*"):
        RepairDroid(TEST, "WEAST")


def test_repairdroid_clone():
    object1 = RepairDroid(TEST)
    object1.load_map(TEST_MAP, 3, 1)
    object1.software.halt = True
    object2 = RepairDroid(TEST)
    object2.clone(object1)
    assert object2.map[0][0] == " "
    assert object2.map[1][3] == "."
    assert object2.map[3][2] == "O"
    assert object2.map[3][3] == "#"
    assert object2.startx == 3
    assert object2.starty == 1
    assert object2.xpos == 3
    assert object2.ypos == 1
    assert object2.software.halt


def test_repairdroid_fail_clone():
    object = RepairDroid(TEST)
    assert not object.clone(TEST_MAP)


def test_repairdroid_reset():
    object = RepairDroid(TEST)
    object.xpos = 4
    object.ypos = 20
    object.steps = 420
    object.reset()
    assert object.xpos == 50
    assert object.ypos == 50
    assert object.steps == 0


def test_repairdroid_set_direction():
    object = RepairDroid(TEST)
    assert object.set_direction("SOUTH")
    assert object.direction == "SOUTH"


def test_repairdroid_fail_set_direction():
    object = RepairDroid(TEST)
    assert not object.set_direction("WEAST")
    assert object.direction == "NORTH"


def test_repairdroid_turn_left():
    object = RepairDroid(TEST)
    object.turn_left()
    assert object.direction == "WEST"
    object.turn_left()
    assert object.direction == "SOUTH"
    object.turn_left()
    assert object.direction == "EAST"
    object.turn_left()
    assert object.direction == "NORTH"


def test_repairdroid_turn_right():
    object = RepairDroid(TEST)
    object.turn_right()
    assert object.direction == "EAST"
    object.turn_right()
    assert object.direction == "SOUTH"
    object.turn_right()
    assert object.direction == "WEST"
    object.turn_right()
    assert object.direction == "NORTH"


def test_repairdroid_load_map():
    object = RepairDroid(TEST)
    object.load_map(TEST_MAP, 3, 1)
    assert object.map[0][0] == " "
    assert object.map[1][3] == "."
    assert object.map[3][2] == "O"
    assert object.map[3][3] == "#"
    assert object.startx == 3
    assert object.starty == 1
    assert object.xpos == 3
    assert object.ypos == 1


def test_repairdroid_print_map():
    object = RepairDroid(TEST)
    object.load_map(TEST_MAP, 3, 1)
    assert object.print_map() == TEST_MAP


def test_read_opcode():
    string = "test.txt"
    result = read_opcode(string)
    assert TEST == result


def test_read_map():
    result = read_map("test_map.txt")
    assert result == TEST_MAP


def test_write_map(tmp_path):
    tmpfile = tmp_path / "tmp.txt"
    write_map(TEST_MAP, tmpfile)
    assert tmpfile.read_text() == TEST_MAP_STRING


def test_spongebob_squarepants():
    pass


def test_patrick_star():
    pass