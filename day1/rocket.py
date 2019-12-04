import os

from math import floor


VALUEFILE = "values.txt"


def import_values(filename):
    """
    Import values from given filename and return a list of values.
    """
    if os.path.basename(os.getcwd()) == "aoc2019":
        filename = os.path.join("day1", filename)

    with open(filename, "r") as valuefile:
        return valuefile.readlines()


def fuel_calc(value):
    """
    Calculate fuel need for given mass
    Formula: Take mass, divide by three, round down, and subtract 2.
    """
    return floor(value / 3) - 2


def fuel_recurse_calc(value):
    """
    Calculate fuel need for given mass, including mass of fuel needed
    Formula: Calculate fuel for given mass, then recurse for mass of
        fuel needed. Recurse until value is zero or negative.
    """
    needed_fuel = fuel_calc(value)
    if needed_fuel >= 0:
        return needed_fuel + fuel_recurse_calc(needed_fuel)
    else:
        return 0


def do_the_mario(valuefile):
    """
    SWING YOUR ARMS FROM SIDE TO SIDE
    """
    values = import_values(valuefile)
    fuel_sum = 0
    fuel_recurse_sum = 0

    for value in values:
        fuel_sum += fuel_calc(int(value))
        fuel_recurse_sum += fuel_recurse_calc(int(value))

    print("========== Part One Answer ==========")
    print(f"Fuel needed: {fuel_sum}\n")
    print("========== Part Two Answer ==========")
    print(f"Fuel needed: {fuel_recurse_sum}")

    return fuel_sum, fuel_recurse_sum


if __name__ == "__main__":
    do_the_mario(VALUEFILE)
