from day4.passwords import Password, DatPassword, hack_the_planet


# Tests


def test_password_create():
    object = Password(1, 2, 3, 4, 5, 6)
    assert isinstance(object, Password)


def test_password_variables():
    a = 1
    b = 2
    c = 3
    d = 4
    e = 5
    f = 6
    result = 123456
    object = Password(a, b, c, d, e, f)
    assert isinstance(object, Password)
    assert object.a == a
    assert object.b == b
    assert object.c == c
    assert object.d == d
    assert object.e == e
    assert object.f == f
    assert object.number == result


def test_password_valid():
    a = 1
    b = 2
    c = 4
    d = 4
    e = 6
    f = 7
    object = Password(a, b, c, d, e, f)
    assert object.is_part1_valid()
    assert object.is_part2_valid()


def test_password_only_part1_valid():
    a = 1
    b = 2
    c = 4
    d = 4
    e = 4
    f = 7
    object = Password(a, b, c, d, e, f)
    assert object.is_part1_valid()
    assert not object.is_part2_valid()


def test_password_invalid_bad_number():
    a = 1
    b = 2
    c = 2
    d = 4
    e = 8
    f = 12
    object = Password(a, b, c, d, e, f)
    assert not object.is_part1_valid()
    assert not object.is_part2_valid()


def test_password_invalid_bad_order():
    a = 1
    b = 2
    c = 2
    d = 4
    e = 8
    f = 4
    object = Password(a, b, c, d, e, f)
    assert not object.is_part1_valid()
    assert not object.is_part2_valid()


def test_password_invalid_final_zero():
    a = 1
    b = 2
    c = 2
    d = 4
    e = 8
    f = 0
    object = Password(a, b, c, d, e, f)
    assert not object.is_part1_valid()
    assert not object.is_part2_valid()


def test_password_invalid_no_duplicate():
    a = 1
    b = 2
    c = 3
    d = 4
    e = 8
    f = 9
    object = Password(a, b, c, d, e, f)
    assert not object.is_part1_valid()
    assert not object.is_part2_valid()


def test_password_part2_true_matches():
    test1 = Password(1, 1, 2, 3, 4, 5)
    test2 = Password(1, 2, 2, 3, 4, 5)
    test3 = Password(1, 2, 3, 3, 4, 5)
    test4 = Password(1, 2, 3, 4, 4, 5)
    test5 = Password(1, 2, 3, 4, 5, 5)
    assert test1.is_part2_valid()
    assert test2.is_part2_valid()
    assert test3.is_part2_valid()
    assert test4.is_part2_valid()
    assert test5.is_part2_valid()


def test_password_get():
    a = 1
    b = 2
    c = 2
    d = 3
    e = 4
    f = 4
    result = 122344
    object = Password(a, b, c, d, e, f)
    assert object.get() == result


def test_dat_password_create():
    input = "123456-234567"
    object = DatPassword(input)
    assert isinstance(object, DatPassword)
    assert object.start.number == 123456
    assert object.end.number == 234567
    assert object.part1_results == []
    assert object.part2_results == []


def test_dat_password_invalid_input():
    input = "123456"
    object = DatPassword(input)
    object.run_test()
    assert object.start is None
    assert object.end is None


def test_dat_password_run():
    input = "123498-123556"
    object = DatPassword(input)
    object.run_test()
    assert object.part1_results == [123499, 123555, 123556]
    assert object.part2_results == [123499, 123556]


def test_dat_password_gets():
    input = "123498-123556"
    object = DatPassword(input)
    object.run_test()
    assert object.get_part1_number() == 3
    assert object.get_part2_number() == 2


def test_hack_the_planet():
    INPUT = "123498-123556"
    part1 = 3
    part2 = 2
    result1, result2 = hack_the_planet(INPUT)
    assert part1 == result1
    assert part2 == result2
