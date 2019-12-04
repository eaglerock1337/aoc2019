from day4.passwords import Password
from day4.passwords import DatPassword

# Tests

def test_password_create():
    a = 1
    b = 2
    c = 3
    d = 4
    e = 5
    f = 6
    result = 123456
    object = Password(a, b, c, d, e, f)
    assert object.a == a
    assert object.b == b
    assert object.c == c
    assert object.d == d
    assert object.e == e
    assert object.f == f
    assert object.number == result


def test_password_valid_1():
    a = 1
    b = 2
    c = 4
    d = 4
    e = 6
    f = 7
    object = Password(a, b, c, d, e, f)
    assert object.is_valid()


def test_password_valid_2():
    a = 2
    b = 2
    c = 4
    d = 4
    e = 4
    f = 7
    object = Password(a, b, c, d, e, f)
    assert object.is_valid()


def test_password_invalid_bad_number():
    a = 1
    b = 2
    c = 2
    d = 4
    e = 8
    f = 12
    object = Password(a, b, c, d, e, f)
    assert not object.is_valid()


def test_password_invalid_bad_order():
    a = 1
    b = 2
    c = 2
    d = 4
    e = 8
    f = 4
    object = Password(a, b, c, d, e, f)
    assert not object.is_valid()


def test_password_invalid_final_zero():
    a = 1
    b = 2
    c = 2
    d = 4
    e = 8
    f = 0
    object = Password(a, b, c, d, e, f)
    assert not object.is_valid()


def test_password_invalid_no_duplicate():
    a = 1
    b = 2
    c = 3
    d = 4
    e = 8
    f = 9
    object = Password(a, b, c, d, e, f)
    assert not object.is_valid()


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