from day7.intcode import IntCode

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
    assert object.input_list == []


def test_intcode_values_input_list():
    opcode = [1, 9, 10, 3, 99]
    input_list = [1, 2, 3]
    object = IntCode(opcode, input_list)
    assert object.opcode == [1, 9, 10, 3, 99]
    assert object.length == 5
    assert object.position == 0
    assert object.input_list == [3, 2, 1]


def test_intcode_run():
    opcode = [99]
    object = IntCode(opcode)
    assert object.run() == []
    assert object.opcode == opcode


def test_opcode_1():
    opcode = [1, 0, 0, 0, 99]
    result_opcode = [2, 0, 0, 0, 99]
    object = IntCode(opcode)
    assert object.run() == []
    assert object.opcode == result_opcode


def test_opcode_1_bad_references():
    opcode1 = [1, 10, 0, 0, 99]
    opcode2 = [1, 0, 10, 0, 99]
    opcode3 = [1, 0, 0, 10, 99]
    object1 = IntCode(opcode1)
    assert object1.run() == -1
    assert object1.opcode == opcode1
    object2 = IntCode(opcode2)
    assert object2.run() == -1
    assert object2.opcode == opcode2
    object3 = IntCode(opcode3)
    assert object3.run() == -1
    assert object3.opcode == opcode3


def test_opcode_2_bad_references():
    opcode1 = [2, 10, 0, 0, 99]
    opcode2 = [2, 0, 10, 0, 99]
    opcode3 = [2, 0, 0, 10, 99]
    object1 = IntCode(opcode1)
    assert object1.run() == -1
    assert object1.opcode == opcode1
    object2 = IntCode(opcode2)
    assert object2.run() == -1
    assert object2.opcode == opcode2
    object3 = IntCode(opcode3)
    assert object3.run() == -1
    assert object3.opcode == opcode3


def test_opcode_2():
    opcode = [2, 3, 0, 3, 99]
    result_opcode = [2, 3, 0, 6, 99]
    object = IntCode(opcode)
    assert object.run() == []
    assert object.opcode == result_opcode


def test_opcode_3():
    opcode = [3, 3, 99, 0]
    result = [3, 3, 99, 42]
    input_list = [42]
    object = IntCode(opcode, input_list)
    assert object.run() == []
    assert object.opcode == result


def test_opcode_3_multiple_inputs():
    opcode = [3, 7, 3, 8, 3, 9, 99, 0, 0, 0]
    result = [3, 7, 3, 8, 3, 9, 99, 4, 2, 42]
    input_list = [4, 2, 42]
    object = IntCode(opcode, input_list)
    assert object.run() == []
    assert object.opcode == result


def test_opcode_3_not_enough_inputs():
    opcode = [3, 7, 3, 8, 3, 9, 99, 0, 0, 0]
    result = [3, 7, 3, 8, 3, 9, 99, 4, 2, 0]
    input_list = [4, 2]
    object = IntCode(opcode, input_list)
    assert object.run() == -1
    assert object.opcode == result


def test_opcode_4():
    opcode = [4, 3, 99, 42]
    result = [4, 3, 99, 42]
    object = IntCode(opcode)
    assert object.run() == [42]
    assert object.opcode == result


def test_opcode_5():
    opcode1 = [5, 10, 11, 99, 1102, 21, 2, 9, 99, 0, 0, 4]
    result1 = [5, 10, 11, 99, 1102, 21, 2, 9, 99, 0, 0, 4]
    opcode2 = [1105, 1, 4, 99, 1102, 21, 2, 9, 99, 0]
    result2 = [1105, 1, 4, 99, 1102, 21, 2, 9, 99, 42]
    object1 = IntCode(opcode1)
    object1.run()
    object2 = IntCode(opcode2)
    object2.run()
    assert object1.opcode == result1
    assert object2.opcode == result2


def test_opcode_6():
    opcode1 = [6, 10, 11, 99, 1102, 21, 2, 9, 99, 0, 0, 4]
    result1 = [6, 10, 11, 99, 1102, 21, 2, 9, 99, 42, 0, 4]
    opcode2 = [1106, 1, 4, 99, 1102, 21, 2, 9, 99, 0]
    result2 = [1106, 1, 4, 99, 1102, 21, 2, 9, 99, 0]
    object1 = IntCode(opcode1)
    object1.run()
    object2 = IntCode(opcode2)
    object2.run()
    assert object1.opcode == result1
    assert object2.opcode == result2


def test_opcode_7():
    opcode1 = [7, 6, 7, 5, 99, 42, 1, 2]
    result1 = [7, 6, 7, 5, 99, 1, 1, 2]
    opcode2 = [1107, 2, 1, 5, 99, 42]
    result2 = [1107, 2, 1, 5, 99, 0]
    opcode3 = [107, 2, 6, 5, 99, 42, 2]
    result3 = [107, 2, 6, 5, 99, 0, 2]
    object1 = IntCode(opcode1)
    object1.run()
    object2 = IntCode(opcode2)
    object2.run()
    object3 = IntCode(opcode3)
    object3.run()
    assert object1.opcode == result1
    assert object2.opcode == result2
    assert object3.opcode == result3


def test_opcode_8():
    opcode1 = [8, 6, 7, 5, 99, 42, 1, 2]
    result1 = [8, 6, 7, 5, 99, 0, 1, 2]
    opcode2 = [1108, 2, 1, 5, 99, 42]
    result2 = [1108, 2, 1, 5, 99, 0]
    opcode3 = [108, 2, 6, 5, 99, 42, 2]
    result3 = [108, 2, 6, 5, 99, 1, 2]
    object1 = IntCode(opcode1)
    object1.run()
    object2 = IntCode(opcode2)
    object2.run()
    object3 = IntCode(opcode3)
    object3.run()
    assert object1.opcode == result1
    assert object2.opcode == result2
    assert object3.opcode == result3


def test_mode_opcodes():
    opcode = [1002, 4, 3, 4, 33]
    result = [1002, 4, 3, 4, 99]
    object = IntCode(opcode)
    object.run()
    assert object.opcode == result


def test_invalid_opcode():
    opcode = [1, 0, 0, 3, 9]
    result = [1, 0, 0, 2, 9]
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


def test_invalid_last_opcode_mode():
    opcode = [11101, 5, 5, 99]
    result = [11101, 5, 5, 99]
    object = IntCode(opcode)
    object.run()
    assert object.opcode == result


def test_too_many_opcode_values():
    opcode = [101101, 5, 5, 4, 99, 0]
    result = [101101, 5, 5, 4, 99, 0]
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


def test_print_opcode():
    opcode = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
    string = "1,9,10,3,2,3,11,0,99,30,40,50"
    object = IntCode(opcode)
    result = object.print_opcode()
    assert string == result