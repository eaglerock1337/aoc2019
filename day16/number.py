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
            for _ in range(number):
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


def subjugate(number_list):
    """
    Return the result of the real signal, using the offset provided by the
    first 7 digits of the number. The number list should be passed in with the
    offset already applied and in reverse order.
    """
    sum = 0
    result = []
    for i in range(len(number_list)):
        sum += number_list[i]
        result.append(sum % 10)

    return result


def catenate(filename, repeat=1):
    """
    Read in the number from the provided filename and return as a list of numbers.
    """
    if os.path.basename(os.getcwd()) == "aoc2019":
        filename = os.path.join("day16", filename)

    with open(filename, "r") as number_file:
        line = number_file.readline()

    line = line.strip()
    signal = line * repeat
    return [int(x) for x in signal]


def illuminate(filename, phases):
    """
    Lights?
    I've changed that...Illuminate...Deluminate! You try it!
    (through gritted teeth) ...Illuminate...
    """
    number = catenate(filename)
    for _ in range(phases):
        number = iterate(number)

    answer = congregate(number[:8])
    print(f"The result after {phases} phases is: {answer}")
    return answer


def deluminate(filename, phases):
    """
    Excuse me sir, what seems to be your boggle?
    Mah boggle?
    """
    number = catenate(filename, 10000)
    offset = congregate(number[:7])
    result = number[offset:]
    result.reverse()

    for _ in range(phases):
        result = subjugate(result)

    result.reverse()
    answer = congregate(result[:8])
    print(f"The result of the real signal after {phases} phases is: {answer}")

    return answer


if __name__ == "__main__":
    illuminate(NUMBER_FILE, 100)
    deluminate(NUMBER_FILE, 100)
