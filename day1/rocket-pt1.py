from math import floor


VALUEFILE = "values.txt"


def import_values(filename):
    """
    Import values from given filename and return a list of values.
    """
    with open(filename, "r") as valuefile:
        return valuefile.readlines()


def fuel_calc(value):
    """
    Calulate fuel need for given mass
    Formula: Take mass, divide by three, round down, and subtract 2.
    """
    return floor(value / 3) - 2


def do_the_mario():
    """
    SWING YOUR ARMS FROM SIDE TO SIDE
    """
    values = import_values(VALUEFILE)
    fuel_sum = 0

    for value in values:
        fuel_sum += fuel_calc(int(value))

    print(f"Fuel needed: {fuel_sum}")


if __name__ == "__main__":
    do_the_mario()