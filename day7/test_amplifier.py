import mock

from day7.intcode import IntCode
from day7.amplifier import Amplifier, Thrusters, read_opcode, ramming_speed

TEST1 = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
TEST2 = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]
TEST3 = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]

# Tests

def test_amplifier_create():
    object = Amplifier(TEST1)
    assert isinstance(object, Amplifier)


def test_amplifier_values():
    object = Amplifier(TEST1)
    assert object.software == TEST1
    assert object.phase == -1


def test_amplifier_set_phase():
    object = Amplifier(TEST1)
    object.set_phase(1)
    assert object.phase == 1


def test_amplifier_run():
    program = [3, 11, 3, 12, 2, 11, 12, 13, 4, 13, 99, 0, 0, 0]
    object = Amplifier(program)
    object.set_phase(2)
    assert object.run(2) == 4
    assert object.run(4) == 8
    object.set_phase(3)
    assert object.run(2) == 6
    assert object.run(4) == 12


def test_amplifier_fail_no_phase():
    program = [3, 11, 3, 12, 2, 11, 12, 13, 4, 13, 99, 0, 0, 0]
    object = Amplifier(program)
    assert object.run(2) == -1


def test_thrusters_create():
    object = Thrusters(TEST1)
    assert isinstance(object, Thrusters)


def test_thrusters_values():
    object = Thrusters(TEST1)
    for value in object.amps:
        assert isinstance(value, Amplifier)
        assert value.software == TEST1
    assert object.phases == [0, 1, 2, 3, 4]


def test_thrusters_run_1():
    object = Thrusters(TEST1)
    output, phases = object.get_best_output()
    assert output == 43210
    assert phases == [4, 3, 2, 1, 0]


def test_thrusters_run_2():
    object = Thrusters(TEST2)
    output, phases = object.get_best_output()
    assert output == 54321
    assert phases == [0, 1, 2, 3, 4]


def test_thrusters_run_3():
    object = Thrusters(TEST3)
    output, phases = object.get_best_output()
    assert output == 65210
    assert phases == [1, 0, 4, 3, 2]


def test_read_opcode():
    string = "test.txt"
    opcode = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
    result = read_opcode(string)
    assert opcode == result


def test_ramming_speed():
    string = "test.txt"
    expected = 43210
    result = ramming_speed(string)
    assert expected == result