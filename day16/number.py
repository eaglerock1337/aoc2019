import os

NUMBER_FILE = "number.txt"
PHASE_PATTERN = [0, 1, 0, -1]

def generate(number):
    """
    Generate the phase pattern based on the provided number. Produce a list
    with the length of the amount provided.
    """
    while True:
        for phase in PHASE_PATTERN:
            for i in range(number):
                yield phase


def iterate(number):
    """
    Iterate over the provided number using the Flawed Frequency Transmission algorithm.
    """
    result = []
    for pos in range(len(number)):
        digit = 0
        gen = generate(pos + 1)
        next(gen)
        for num in number:
            digit += num * next(gen)
        result.append(int(abs(digit) % 10))

    return result


def congregate(number_list):
    """
    Return an integer from a number list.
    """
    string = ""
    for x in number_list:
        string += str(x)

    return int(string)


def catenate(filename):
    """
    Read in the number from the provided filename and return as a list of numbers.
    """
    if os.path.basename(os.getcwd()) == "aoc2019":
        filename = os.path.join("day16", filename)

    with open(filename, "r") as number_file:
        line = number_file.readline()
        
    line = line.strip()
    return [int(x) for x in line]


def illuminate(filename, phases):
    number = catenate(filename)
    for _ in range(phases):
        number = iterate(number)

    answer = congregate(number[:8])
    print(f"The result after {phases} phases is: {answer}")
    return answer


def deluminate():
    pass


if __name__ == "__main__":
    illuminate(NUMBER_FILE, 100)