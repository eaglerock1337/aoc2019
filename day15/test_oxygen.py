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

# Tests


def test_repairdroid_create():
    blank = [[" " for x in range(100)] for y in range(100)]
    object = RepairDroid(TEST)
    assert object.map == blank
    assert object.software.opcode[: len(TEST)] == TEST
    assert object.startx == 50
    assert object.starty == 50
    assert object.steps == 0
    assert object.direction == "NORTH"

    object2 = RepairDroid(TEST, "WEST")
    assert object2.direction == "WEST"


def test_repairdroid_fail_create():
    with pytest.raises(TypeError, match=r".*direction input was invalid.*"):
        RepairDroid(TEST, "WEAST")


def test_read_opcode():
    string = "test.txt"
    result = read_opcode(string)
    assert TEST == result


def test_read_map():
    result = read_map("test_map.txt")
    assert result == TEST_MAP


def test_write_map():
    pass


def test_spongebob_squarepants():
    pass


def test_patrick_star():
    pass