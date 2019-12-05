import os


OPCODE_FILE = "opcode.txt"


class IntCode:
    """
    The class responsible for emulating the Intcode computer.
    Runs the intcode program for given opcode.
    """

    def __init__(self, opcode):
        self.opcode = opcode.copy()
        self.length = len(opcode)
        self.position = 0

    def _opcode_1(self):
        """
        Opcode 1: Add values
        opcode[position] = 1
        opcode[position + 1] = position of first value to add
        opcode[position + 2] = position of second value to add
        opcode[position + 3] = position to store added value

        This could be much more compact, but it's more readable this way.
        """
        val1_pos = self.opcode[self.position + 1]
        val2_pos = self.opcode[self.position + 2]
        sum_pos = self.opcode[self.position + 3]

        if val1_pos < self.length:
            value_1 = self.opcode[val1_pos]
        else:
            print("Invalid Opcode reference!")
            return

        if val2_pos < self.length:
            value_2 = self.opcode[val2_pos]
        else:
            print("Invalid Opcode reference!")
            return

        if sum_pos < self.length:
            self.opcode[sum_pos] = value_1 + value_2
        else:
            print("Invalid Opcode Reference!")

    def _opcode_2(self):
        """
        Opcode 2: Multiply values
        opcode[position] = 2
        opcode[position + 1] = position of first value to multiply
        opcode[position + 2] = position of second value to multiply
        opcode[position + 3] = position to store multiplied value

        This could be much more compact, but it's more readable this way.
        """
        val1_pos = self.opcode[self.position + 1]
        val2_pos = self.opcode[self.position + 2]
        product_pos = self.opcode[self.position + 3]

        if val1_pos < self.length:
            value_1 = self.opcode[val1_pos]
        else:
            print("Invalid Opcode reference!")
            return

        if val2_pos < self.length:
            value_2 = self.opcode[val2_pos]
        else:
            print("Invalid Opcode reference!")
            return

        if product_pos < self.length:
            self.opcode[product_pos] = value_1 * value_2
        else:
            print("Invalid Opcode reference!")

    def run(self):
        """
        Run the intcode program by parsing through the opcode list.
        """
        while self.position < self.length:
            if self.opcode[self.position] == 1:
                self._opcode_1()
                self.position += 4
            elif self.opcode[self.position] == 2:
                self._opcode_2()
                self.position += 4
            elif self.opcode[self.position] == 99:
                # print("Intcode program completed successfully.")
                return
            else:
                print(
                    f"Error: invalid opcode at position {self.position}: {self.opcode[self.position]}"
                )
                return

        print("Error: No more opcode values to read!")

    def get_value(self):
        return self.opcode[0]


def read_opcode(filename):
    """
    Read in the opcode from a given filename and return as a list.
    Currently only reads in a single opcode from the file.
    """
    if os.path.basename(os.getcwd()) == "aoc2019":
        filename = os.path.join("day2", filename)

    with open(filename, "r") as opcode_file:
        opcode = opcode_file.readline()

    string_opcode = opcode.split(",")
    return [int(i) for i in string_opcode]


def print_opcode(opcode):
    """
    Returns the opcode as it should be displayed (comma-separated).
    """
    full_opcode = ""

    for value in opcode:
        full_opcode += f"{value},"

    return full_opcode[:-1]


def patch_me(opcode, noun, verb):
    """
    Perform standard patching of opcode using two values replaced in positions 1 and 2.
    """
    new_opcode = opcode.copy()
    new_opcode[1] = noun
    new_opcode[2] = verb
    return new_opcode


def fly_like_an_eagle(file, noun, verb):
    """
    I'm gonna FLYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY like an eagle...
    To the sea...
    """
    opcode = read_opcode(file)
    print("Here is the original opcode:")
    print(print_opcode(opcode) + "\n")

    patched_opcode = patch_me(opcode, noun, verb)
    print("Here is the patched opcode:")
    print(print_opcode(patched_opcode) + "\n")

    print("Running program...")
    intcode = IntCode(patched_opcode)
    intcode.run()

    print("Result of Intcode:")
    print(print_opcode(intcode.opcode) + "\n")
    print(f"The value at position 0 is {intcode.get_value()}")

    return intcode.get_value()


def we_got_dodgson_here(file, target_output):
    """
    See, nobody cares...nice hat.
    """
    opcode = read_opcode(file)

    print(f"\nFinding target value {target_output}...")

    for val1 in range(1, 100):
        for val2 in range(1, 100):
            patch = patch_me(opcode, val1, val2)
            intcode = IntCode(patch)
            intcode.run()
            result = intcode.get_value()
            if result == target_output:
                print(f"Matched {target_output} with values {val1} and {val2}!")
                answer = 100 * val1 + val2
                print(f"The answer to the question is {answer}!")
                return answer


if __name__ == "__main__":
    fly_like_an_eagle(OPCODE_FILE, 12, 2)
    we_got_dodgson_here(OPCODE_FILE, 19690720)
