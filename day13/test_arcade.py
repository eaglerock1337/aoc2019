from day13.intcode import IntCode
from day13.arcade import Arcade, read_opcode, noahs_arcade, pinball_wizard

TEST = [3, 10, 104, 1, 104, 1, 6, 10, 11, 99, 0, 0]

# Tests


def test_arcade_create():
    blank = [[0 for x in range(43)] for y in range(23)]
    object = Arcade(TEST)
    assert object.screen == blank
    assert object.software.opcode[: len(TEST)] == TEST
    assert object.ballpos == -1
    assert object.paddlepos == -1
    assert object.score == -1


def test_read_opcode():
    string = "test.txt"
    result = read_opcode(string)
    assert TEST == result


def test_noahs_arcade():
    filename = "arcade.txt"
    assert noahs_arcade(filename) == 363


def test_pinball_wizard():
    filename = "arcade.txt"
    assert pinball_wizard(filename) == 17159
