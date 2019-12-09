import mock

from day9.intcode import IntCode
from day9.boost import (
    read_opcode,
    thank_you_captain,
)

# Tests


def test_read_opcode():
    string = "test.txt"
    opcode = [1101, 10, 11, 11, 102, 2, 11, 12, 4, 12, 99, 0, 0]
    result = read_opcode(string)
    assert opcode == result


def test_thank_you_captain():
    filename = "test.txt"
    result = thank_you_captain(filename, 1)
    assert result == 42
