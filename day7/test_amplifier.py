import mock

from day7.intcode import IntCode
from day7.amplifier import (
    Amplifier,
    Thrusters,
    read_opcode,
    ramming_speed,
    this_is_spinal_tap,
)

TEST1 = [3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0]
# fmt: off
TEST2 = [3, 23, 3, 24, 1002, 24, 10, 24, 1002, 23, -1, 23, 101, 5, 23, 23, 1,
         24, 23, 23, 4, 23, 99, 0, 0]
TEST3 = [3, 31, 3, 32, 1002, 32, 10, 32, 1001, 31, -2, 31, 1007, 31, 0, 33,
         1002, 33, 7, 33, 1, 33, 31, 31, 1, 32, 31, 31, 4, 31, 99, 0, 0, 0]

FEEDBACK_TEST1 = [3, 26, 1001, 26, -4, 26, 3, 27, 1002, 27, 2, 27, 1, 27, 26,
                  27, 4, 27, 1001, 28, -1, 28, 1005, 28, 6, 99, 0, 0, 5]
FEEDBACK_TEST2 = [3, 52, 1001, 52, -5, 52, 3, 53, 1, 52, 56, 54, 1007, 54, 5,
                  55, 1005, 55, 26, 1001, 54, -5, 54, 1105, 1, 12, 1, 53, 54,
                  53, 1008, 54, 0, 55, 1001, 55, 1, 55, 2, 53, 55, 53, 4, 53,
                  1001, 56, -1, 56, 1005, 56, 6, 99, 0, 0, 0, 0, 10]
# fmt: on

# Tests


def test_amplifier_create():
    object = Amplifier(TEST1)
    assert isinstance(object, Amplifier)


def test_amplifier_values():
    object = Amplifier(TEST1)
    assert object.software == TEST1
    assert object.phase == -1
    assert not object.primed


def test_amplifier_prime():
    object = Amplifier(TEST1)
    object.prime(1)
    assert object.phase == 1
    assert object.program.input_list == [1]
    assert object.primed


def test_amplifier_run():
    program = [3, 11, 3, 12, 2, 11, 12, 13, 4, 13, 99, 0, 0, 0]
    object = Amplifier(program)
    object.prime(2)
    assert object.run(2) == 4
    object.prime()
    assert object.run(4) == 8
    object.prime(3)
    assert object.run(2) == 6
    object.prime()
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


def test_thrusters_feedback_run_1():
    object = Thrusters(FEEDBACK_TEST1)
    output, phases = object.get_best_feedback_output()
    assert output == 139629729
    assert phases == [9, 8, 7, 6, 5]


def test_thrusters_feedback_run_2():
    object = Thrusters(FEEDBACK_TEST2)
    output, phases = object.get_best_feedback_output()
    assert output == 18216
    assert phases == [9, 7, 8, 5, 6]


def test_read_opcode():
    string = "test.txt"
    opcode = [3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0]
    result = read_opcode(string)
    assert opcode == result


def test_ramming_speed():
    string = "test.txt"
    expected = 43210
    result = ramming_speed(string)
    assert expected == result


def test_this_is_spinal_tap():
    string = "test2.txt"
    expected = 139629729
    result = this_is_spinal_tap(string)
    assert expected == result
