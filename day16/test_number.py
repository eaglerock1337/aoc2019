from itertools import islice

from day16.number import (
    generate,
    iterate,
    congregate,
    subjugate,
    catenate,
    illuminate,
    deluminate,
)

TEST = [1, 2, 3, 4, 5, 6, 7, 8]

# Tests


def test_generate():
    assert list(islice(generate(1), 10)) == [0, 1, 0, -1, 0, 1, 0, -1, 0, 1]
    assert list(islice(generate(2), 6)) == [0, 0, 1, 1, 0, 0]
    assert list(islice(generate(3), 8)) == [0, 0, 0, 1, 1, 1, 0, 0]
    assert list(islice(generate(10), 5)) == [0, 0, 0, 0, 0]


def test_iterate():
    result = [4, 8, 2, 2, 6, 1, 5, 8]
    number = iterate(TEST)
    assert number == result


def test_iterate_and_congregate():
    number = iterate(TEST)
    assert congregate(number) == 48226158
    number = iterate(number)
    assert congregate(number) == 34040438
    number = iterate(number)
    assert congregate(number) == 3415518
    number = iterate(number)
    assert congregate(number) == 1029498


def test_subjugate():
    number = subjugate(TEST)
    assert congregate(number) == 13605186


def test_catenate():
    filename = "test.txt"
    result = catenate(filename)
    assert result == TEST


def test_illuminate():
    filename = "test2.txt"
    assert illuminate(filename, 100) == 24176176


def test_illuminate_2():
    filename = "test3.txt"
    assert illuminate(filename, 100) == 73745418


def test_illuminate_3():
    filename = "test4.txt"
    assert illuminate(filename, 100) == 52432133


def test_deluminate():
    filename = "test5.txt"
    assert deluminate(filename, 100) == 84462026


def test_deluminate_2():
    filename = "test6.txt"
    assert deluminate(filename, 100) == 78725270


def test_deluminate_3():
    filename = "test7.txt"
    assert deluminate(filename, 100) == 53553731
