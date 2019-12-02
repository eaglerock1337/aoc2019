OPCODE_FILE = "opcode.txt"


class IntCode:
    """
    The class responsible for emulating the Intcode computer.
    Runs the intcode program for given opcode.
    """

    def __init__(self, opcode):
        self.opcode = opcode
        self.length = len(opcode)
        self.position = 0
        self._run()

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

        value_1 = self.opcode[val1_pos]
        value_2 = self.opcode[val2_pos]
        self.opcode[sum_pos] = value_1 + value_2

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

        value_1 = self.opcode[val1_pos]
        value_2 = self.opcode[val2_pos]
        self.opcode[product_pos] = value_1 * value_2

    def _run(self):
        """
        Run the intcode program by parsing through the opcode list.
        """
        while self.position < self.length:
            if self.opcode[self.position] == 1:
                self._opcode_1()
            elif self.opcode[self.position] == 2:
                self._opcode_2()
            elif self.opcode[self.position] == 99:
                print("Intcode program completed successfully.")
                return
            else:
                print("Error: invalid opcode at position {self.position}: {self.opcode[self.position]}")

            self.position += 4

        print("Error: No more opcode values to read!")

    
def read_opcode(filename):
    """
    Read in the opcode from a given filename and return as a list.
    Currently only reads in a single opcode from the file.
    """
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


def patch_opcode(opcode, position, value):
    """
    Perform a manual patch of an opcode. Changes opcode[position] to the given value.
    """
    opcode[position] = value
    return opcode


def fly_like_an_eagle():
    """
    I'm gonna FLYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY like an eagle...
    To the sea...
    """
    opcode = read_opcode(OPCODE_FILE)
    print("Here is the original opcode:")
    print(print_opcode(opcode) + "\n")

    patched_opcode = patch_opcode(opcode,         1, 12)
    patched_opcode = patch_opcode(patched_opcode, 2, 2)

    print("Here is the patched opcode:")
    print(print_opcode(patched_opcode) + "\n")

    print("Running program...")
    run = IntCode(patched_opcode)

    print("Result of Intcode:")
    print(print_opcode(run.opcode) + "\n")
    print(f"The value at position 0 is {run.opcode[0]}")


if __name__ == "__main__":
    fly_like_an_eagle()