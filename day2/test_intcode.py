from day2.intcode import (
    IntCode,
    read_opcode,
    print_opcode,
    patch_me,
    fly_like_an_eagle,
    we_got_dodgson_here,
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


def test_invalid_opcode():
    opcode = [1, 0, 0, 3, 3]
    result = [1, 0, 0, 2, 3]
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


def test_read_opcode():
    string = "test.txt"
    opcode = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
    result = read_opcode(string)
    assert opcode == result


def test_print_opcode():
    opcode = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
    string = "1,9,10,3,2,3,11,0,99,30,40,50"
    result = print_opcode(opcode)
    assert string == result


def test_patch_me():
    noun = 12
    verb = 2
    opcode = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
    expected = [1, 12, 2, 3, 2, 3, 11, 0, 99, 30, 40, 50]
    result = patch_me(opcode, noun, verb)
    assert expected == result


def test_fly_like_an_eagle():
    filename = "test.txt"
    noun = 9
    verb = 10
    answer = 3500
    result = fly_like_an_eagle(filename, noun, verb)
    assert answer == result


def test_we_got_dodgson_here():
    filename = "opcode.txt"
    target = 4138658
    answer = 1202
    result = we_got_dodgson_here(filename, target)
    assert answer == result
