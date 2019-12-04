from day1.rocket import(
    import_values,
    fuel_calc,
    fuel_recurse_calc,
    do_the_mario
)

# Tests


def test_import_values():
    testfile = "test.txt"
    result = ["12\n", "14\n", "1969\n", "100756"]
    test = import_values(testfile)
    assert result == test


def test_fuel_calc():
    mass = 1969
    fuel = 654
    result = fuel_calc(mass)
    assert fuel == result


def test_fuel_recurse_calc():
    mass = 1969
    fuel = 966
    result = fuel_recurse_calc(mass)
    assert fuel == result


def test_do_the_mario():
    testfile = "test.txt"
    fuel_sum = 2 + 2 + 654 + 33583
    fuel_recurse_sum = 2 + 2 + 966 + 50346
    fuel_result, fuel_recurse_result = do_the_mario(testfile)
    assert fuel_sum == fuel_result
    assert fuel_recurse_sum == fuel_recurse_result