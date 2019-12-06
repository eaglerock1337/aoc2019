import os

OPCODE_FILE = "opcode.txt"
OPCODE_FUNC = {
    "01": "_opcode_1",
    "02": "_opcode_2",
    "03": "_opcode_3",
    "04": "_opcode_4",
    "05": "_opcode_5",
    "06": "_opcode_6",
    "07": "_opcode_7",
    "08": "_opcode_8",
}
# fmt: off
OPCODE_PARAMS = {
    "01": 4,
    "02": 4,
    "03": 2,
    "04": 2,
    "05": 3,
    "06": 3,
    "07": 4,
    "08": 4,
}
# fmt: on
LAST_VAL_FORCED_REF = {
    "01": True,
    "02": True,
    "03": True,
    "04": False,
    "05": False,
    "06": False,
    "07": True,
    "08": True,
}


class IntCode:
    """
    The class responsible for emulating the Intcode computer.
    Runs the intcode program for given opcode.
    """

    def __init__(self, opcode):
        self.opcode = opcode.copy()
        self.length = len(opcode)
        self.position = 0

    def patch(self, noun, verb):
        """
        Perform standard patching of opcode using two values replaced in positions 1 and 2.
        """
        self.opcode[1] = noun
        self.opcode[2] = verb

    def _opcode_1(self, params):
        """
        Opcode 1: Add two numbers
        params[0] - location of first number to add
        params[1] - location of second number to add
        params[2] - location to store sum
        """
        num1, num2, result = params
        self.opcode[result] = self.opcode[num1] + self.opcode[num2]
        return True

    def _opcode_2(self, params):
        """
        Opcode 2: Multiply two numbers
        params[0] - location of first number to multiply
        params[1] - location of second number to multiply
        params[2] - location to store product
        """
        num1, num2, result = params
        self.opcode[result] = self.opcode[num1] * self.opcode[num2]
        return True

    def _opcode_3(self, params):
        """
        Opcode 3: Accept input from user
        params[0] - location to store
        """
        value = int(input("Please enter a value: "))
        self.opcode[params.pop()] = value
        return True

    def _opcode_4(self, params):
        """
        Opcode 4: Output value from location
        params[0] - location of value to output
        """
        print(f"OUTPUT: {self.opcode[params.pop()]}")
        return True

    def _opcode_5(self, params):
        """
        Opcode 5: Jump if true - Sets instruction pointer if value is true
        params[0] - location of boolean paramter (zero is false, nonzero is true)
        params[1] - location of instruction pointer to change to if true
        """
        boolean, pointer = params
        if self.opcode[boolean] == 0:
            return True
        else:
            self.position = self.opcode[pointer]
            return False

    def _opcode_6(self, params):
        """
        Opcode 6: Jump if false - Sets instruction pointer if value is false
        params[0] - location of boolean paramter (zero is false, nonzero is true)
        params[1] - location of instruction pointer to change to if false
        """
        boolean, pointer = params
        if self.opcode[boolean] == 0:
            self.position = self.opcode[pointer]
            return False
        else:
            return True

    def _opcode_7(self, params):
        """
        Opcode 7: Less than - Stores 1 if first value is less than the second, 0 otherwise
        params[0] - location of first value to be compared
        params[1] - location of second value to be compared
        params[2] - location to store 1 if first value is less than second, 0 otherwise
        """
        val1, val2, boolean = params
        if self.opcode[val1] < self.opcode[val2]:
            self.opcode[boolean] = 1
        else:
            self.opcode[boolean] = 0
        return True

    def _opcode_8(self, params):
        """
        Opcode 8: Equals - Stores 1 if first value is equal to the second, 0 otherwise
        params[0] - location of first value to be compared
        params[1] - location of second value to be compared
        params[2] - location to store 1 if first value is equal to the second, 0 otherwise
        """
        val1, val2, boolean = params
        if self.opcode[val1] == self.opcode[val2]:
            self.opcode[boolean] = 1
        else:
            self.opcode[boolean] = 0
        return True

    def run(self):
        """
        Run the intcode program by parsing through the opcode list.
        """
        while self.position < self.length:
            if self.opcode[self.position] == 99:
                return

            string = str(self.opcode[self.position])
            if len(string) == 1:
                opcode = f"0{string}"
                instruction = []
            else:
                opcode = string[-2:]
                instruction = list(string[:-2])

            if opcode in OPCODE_FUNC:
                params = []

                if self.position + OPCODE_PARAMS[opcode] > self.length:
                    print(
                        f"Invalid Opcode reference at {self.position}: Opcode string has run out of values!"
                    )
                    return

                for i in range(1, OPCODE_PARAMS[opcode]):
                    try:
                        mode = instruction.pop()
                    except IndexError:
                        mode = "0"

                    if mode == "0":
                        param_pos = self.opcode[self.position + i]
                        if param_pos < self.length:
                            params.append(param_pos)
                        else:
                            print(
                                f"Invalid Opcode reference at {self.position}: {param_pos} is out of range!"
                            )
                            return

                    elif mode == "1":
                        if (
                            i == OPCODE_PARAMS[opcode] - 1
                            and LAST_VAL_FORCED_REF[opcode]
                        ):
                            print(
                                f"Invalid Opcode reference at {self.position}: Opcode {opcode} requires a location for its last value!"
                            )
                            return

                        params.append(self.position + i)

                if len(instruction) > 0:
                    print(
                        f"Invalid Opcode at {self.position}: {self.opcode[self.position]} has too many characters!"
                    )
                    return

                function = getattr(self, OPCODE_FUNC[opcode])
                advance = function(params)
                if advance:
                    self.position += OPCODE_PARAMS[opcode]
            else:
                print(
                    f"Error: invalid opcode {opcode} at position {self.position}: {self.opcode[self.position]}"
                )
                return

        print("Error: No more opcode values to read!")

    def get_value(self):
        return self.opcode[0]

    def print_opcode(self):
        """
        Returns the opcode as it should be displayed (comma-separated).
        """
        full_opcode = ""

        for value in self.opcode:
            full_opcode += f"{value},"

        return full_opcode[:-1]


def read_opcode(filename):
    """
    Read in the opcode from a given filename and return as a list.
    Currently only reads in a single opcode from the file.
    """
    if os.path.basename(os.getcwd()) == "aoc2019":
        filename = os.path.join("day5", filename)

    with open(filename, "r") as opcode_file:
        opcode = opcode_file.readline()

    string_opcode = opcode.split(",")
    return [int(i) for i in string_opcode]


def find_pebkac_error(filename):
    """
    Problem exists between keyboard and chair.
    """
    opcode = read_opcode(filename)

    print(f"Running TEST program...")
    computer = IntCode(opcode)
    computer.run()


if __name__ == "__main__":
    find_pebkac_error(OPCODE_FILE)
