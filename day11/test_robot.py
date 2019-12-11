from day11.intcode import IntCode
from day11.robot import (
    BobRoss,
    read_opcode,
    happy_little_cloud,
)

TEST = [3, 10, 104, 1, 104, 1, 6, 10, 11, 99, 0, 0]
TEST2 = [3, 10, 104, 1, 104, 0, 6, 10, 11, 99, 0, 0]
RESULT_GRID = [
        [".", ".", ".", "."],
        [".", "#", "#", "."],
        [".", "#", "#", "."],
        [".", ".", ".", "."],
    ]

# Tests

def test_bobross_create():
    grid = [
        [".", ".", ".", "."],
        [".", ".", ".", "."],
        [".", ".", ".", "."],
        [".", ".", ".", "."],
    ]
    object = BobRoss(TEST, 4)
    assert isinstance(object, BobRoss)
    assert object.direction == 0
    assert object.panels == []
    assert object.xpos == 1
    assert object.ypos == 1
    assert object.brain.opcode[: len(TEST)] == TEST
    assert object.grid == grid


def test_bobross_run():
    object = BobRoss(TEST, 4)
    assert object.run()
    assert object.xpos == 2
    assert object.ypos == 1
    assert object.panels == [(1, 1), (2, 1), (2, 2), (1, 2)]
    assert object.grid == RESULT_GRID


def test_bobross_run_2():
    object = BobRoss(TEST2, 4)
    assert object.run()
    assert object.xpos == 0
    assert object.ypos == 1
    assert object.panels == [(1, 1), (0, 1), (0, 2), (1, 2)]


def test_bobross_run_fail():
    opcode = [11, 99]
    object = BobRoss(opcode, 4)
    assert not object.run()


def test_read_opcode():
    string = "test.txt"
    result = read_opcode(string)
    assert TEST == result


def test_happy_little_cloud():
    filename = "test.txt"
    assert happy_little_cloud(filename) == 4
