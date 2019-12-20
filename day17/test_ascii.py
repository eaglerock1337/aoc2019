from mock import patch

import pytest

from day17.intcode import IntCode
from day17.ascii import (
    ASCII,
    read_opcode,
)

TEST = [3, 10, 104, 1, 104, 1, 6, 10, 11, 99, 0, 0]

TEST_MAP = [
    [".", ".", "#", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", "#", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    ["#", "#", "#", "#", "#", "#", "#", ".", ".", ".", "#", "#", "#"],
    ["#", ".", "#", ".", ".", ".", "#", ".", ".", ".", "#", ".", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    [".", ".", "#", ".", ".", ".", "#", ".", ".", ".", "#", ".", "."],
    [".", ".", "#", "#", "#", "#", "#", ".", ".", ".", "^", ".", "."],
]

# Tests


def test_ascii_create():
    object = ASCII(TEST)
    assert isinstance(object, ASCII)
    assert object.program.opcode[: len(TEST)] == TEST
    assert object.map == []
    assert object.mapstring == ""
    assert object.intersections == []


def test_ascii_build_map():
    opcode = [104, 46, 104, 46, 104, 46, 104, 10, 104, 35, 104, 35, 104, 35, 104, 10, 104, 46, 104, 35, 104, 60, 99]
    object = ASCII(opcode)
    object.build_map()
    assert object.map == [[".", ".", "."], ["#", "#", "#"], [".", "#", "<"]]
    assert object.mapstring == "...\n###\n.#<"


def test_ascii_is_intersection():
    object = ASCII(TEST)
    object.map = TEST_MAP
    assert object._is_intersection(2, 2)
    assert not object._is_intersection(2, 3)
    assert not object._is_intersection(6, 2)


def test_ascii_get_intersections():
    object = ASCII(TEST)
    object.map = TEST_MAP
    object._get_intersections()
    assert object.intersections == [(2, 2), (2, 4), (6, 4), (10, 4)]


def test_ascii_align():
    object = ASCII(TEST)
    object.map = TEST_MAP
    assert object.align() == 76


def test_read_opcode():
    string = "test.txt"
    result = read_opcode(string)
    assert TEST == result
