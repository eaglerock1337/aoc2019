import mock

from day5.intcode import (
    IntCode,
    read_opcode,
    find_pebkac_error
)

# Tests
def test_intcode_create():
    opcode = [1, 9, 10, 3, 99]
    object = IntCode(opcode)
    assert isinstance(object, IntCode)
    

def test_intcode_values():
    opcode = [1, 9, 10, 3, 99]
    object = IntCode(opcode)
    assert object.opcode == [1, 9, 10, 3, 99]
    assert object.length == 5
    assert object.position == 0


def test_intcode_run():
    opcode = [99]
    object = IntCode(opcode)
    object.run()
    assert object.opcode == opcode


def test_opcode_1():
    opcode = [1, 0, 0, 0, 99]
    result_opcode = [2, 0, 0, 0, 99]
    object = IntCode(opcode)
    object.run()
    assert object.opcode == result_opcode


def test_opcode_1_bad_references():
    opcode1 = [1, 10, 0, 0, 99]
    opcode2 = [1, 0, 10, 0, 99]
    opcode3 = [1, 0, 0, 10, 99]
    object1 = IntCode(opcode1)
    object1.run()
    assert object1.opcode == opcode1
    object2 = IntCode(opcode2)
    object2.run()
    assert object2.opcode == opcode2
    object3 = IntCode(opcode3)
    object3.run()
    assert object3.opcode == opcode3


def test_opcode_2_bad_references():
    opcode1 = [2, 10, 0, 0, 99]
    opcode2 = [2, 0, 10, 0, 99]
    opcode3 = [2, 0, 0, 10, 99]
    object1 = IntCode(opcode1)
    object1.run()
    assert object1.opcode == opcode1
    object2 = IntCode(opcode2)
    object2.run()
    assert object2.opcode == opcode2
    object3 = IntCode(opcode3)
    object3.run()
    assert object3.opcode == opcode3


def test_opcode_2():
    opcode = [2, 3, 0, 3, 99]
    result_opcode = [2, 3, 0, 6, 99]
    object = IntCode(opcode)
    object.run()
    assert object.opcode == result_opcode
    

def test_opcode_3():
    opcode = [3, 3, 99, 0]
    result = [3, 3, 99, 42]
    with mock.patch('builtins.input', return_value=42):
        object = IntCode(opcode)
        object.run()
        assert object.opcode == result
        

def test_opcode_4(capsys):
    opcode = [4, 3, 99, 42]
    result = [4, 3, 99, 42]
    object = IntCode(opcode)
    object.run()
    captured = capsys.readouterr()
    assert captured.out == "OUTPUT: 42\n"
    assert object.opcode == result


def test_mode_opcodes():
    opcode = [1002,4,3,4,33]
    result = [1002,4,3,4,99]
    object = IntCode(opcode)
    object.run()
    assert object.opcode == result


def test_invalid_opcode():
    opcode = [1, 0, 0, 3, 8]
    result = [1, 0, 0, 2, 8]
    object = IntCode(opcode)
    object.run()
    assert object.opcode == result


def test_not_enough_opcode_values():
    opcode = [1, 0, 0]
    result = [1, 0, 0]
    object = IntCode(opcode)
    object.run()
    assert object.opcode == result


def test_run_out_of_opcode_values():
    opcode = [1101, 5]
    result = [1101, 5]
    object = IntCode(opcode)
    object.run()
    assert object.opcode == result


def test_too_many_opcode_values():
    opcode = [11101, 5, 5, 99, 0]
    result = [11101, 5, 5, 99, 0]
    object = IntCode(opcode)
    object.run()
    assert object.opcode == result

    
def test_invalid_opcode_position():
    opcode = [1, 0, 0, 3]
    result = [1, 0, 0, 2]
    object = IntCode(opcode)
    object.run()
    assert object.opcode == result


def test_get_value():
    opcode = [1, 5, 6, 0, 99, 5, 8]
    result = 13
    object = IntCode(opcode)
    object.run()
    assert object.get_value() == result


def test_patch():
    noun = 12
    verb = 2
    opcode = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
    expected = [1, 12, 2, 3, 2, 3, 11, 0, 99, 30, 40, 50]
    object = IntCode(opcode)
    object.patch(noun, verb)
    result = object.opcode
    assert expected == result


def test_read_opcode():
    string = "test.txt"
    opcode = [1101, 10, 11, 11, 102, 2, 11, 12, 4, 12, 99, 0, 0]
    result = read_opcode(string)
    assert opcode == result


def test_print_opcode():
    opcode = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
    string = "1,9,10,3,2,3,11,0,99,30,40,50"
    object = IntCode(opcode)
    result = object.print_opcode()
    assert string == result


def test_find_pebkac_error(capsys):
    filename = "test.txt"
    find_pebkac_error(filename)
    captured = capsys.readouterr()
    assert captured.out == "Running TEST program...\nOUTPUT: 42\n"
