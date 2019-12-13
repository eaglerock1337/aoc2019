from day13.intcode import IntCode
from day13.arcade import (
    read_opcode
)


# Tests

def test_read_opcode():
    string = "test.txt"
    result = read_opcode(string)
    assert TEST == result
