OPCODE_FUNC = {
    "01": "_opcode_1",
    "02": "_opcode_2",
    "03": "_opcode_3",
    "04": "_opcode_4",
    "05": "_opcode_5",
    "06": "_opcode_6",
    "07": "_opcode_7",
    "08": "_opcode_8",
    "09": "_opcode_9",
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
    "09": 2,
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
    "09": False,
}


class IntCode:
    """
    The class responsible for emulating the Intcode computer.
    Runs the intcode program for given opcode.
    Accepts the opcode as a list of opcode values.
    Optionally accepts kwarg input_list as a list of inputs for use with Opcode 3.
    """

    def __init__(self, opcode, input_list=[]):
        self.opcode = opcode.copy()
        self.length = len(opcode)
        self.opcode.extend([0] * 10000)
        self.position = 0
        self.relative = 0
        self.input_list = input_list.copy()
        self.input_list.reverse()  # Reversed so I can use pop() instead of writing a Queue
        self.output = []
        self.halt = False

    def patch(self, noun, verb):
        """
        Perform standard patching of opcode using two values replaced in positions 1 and 2.
        """
        self.opcode[1] = noun
        self.opcode[2] = verb

    def add_input(self, new_input):
        """
        Adds a single input to the running IntCode program.
        """
        self.input_list.insert(0, new_input)

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
        Opcode 3: Accept input from input_list
        params[0] - location to store
        """
        try:
            value = self.input_list.pop()
        except IndexError:
            self.halt = True
            return True
        self.opcode[params.pop()] = value
        return True

    def _opcode_4(self, params):
        """
        Opcode 4: Output value from location
        params[0] - location of value to output
        """
        self.output.append(self.opcode[params.pop()])
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

    def _opcode_9(self, params):
        """
        Opcode 9: Adjust Relative Base - Sets relative base value
        params[0] - amount (positive or negative) to adjust relative position
        """
        self.relative += self.opcode[params.pop()]
        return True

    def run(self):
        """
        Run the intcode program by parsing through the opcode list.
        """
        if self.halt:
            self.output = []
            self.halt = False

        while self.position < len(self.opcode):
            if self.opcode[self.position] == 99:
                return self.output

            string = str(self.opcode[self.position])
            if len(string) == 1:
                opcode = f"0{string}"
                instruction = []
            else:
                opcode = string[-2:]
                instruction = list(string[:-2])

            if opcode in OPCODE_FUNC:
                params = []

                for i in range(1, OPCODE_PARAMS[opcode]):
                    try:
                        mode = instruction.pop()
                    except IndexError:
                        mode = "0"

                    if mode == "0":
                        param_pos = self.opcode[self.position + i]
                        params.append(param_pos)

                    elif mode == "1":
                        if (
                            i == OPCODE_PARAMS[opcode] - 1
                            and LAST_VAL_FORCED_REF[opcode]
                        ):
                            print(
                                f"Invalid Opcode reference at {self.position}: Opcode {opcode} requires a location for its last value!"
                            )
                            return -1

                        params.append(self.position + i)

                    elif mode == "2":
                        param_pos = self.relative + self.opcode[self.position + i]
                        if param_pos < 0:
                            print(
                                f"Invalid Opcode reference at {self.position}: Relative reference less than zero!"
                            )
                            return -1
                        params.append(param_pos)

                    else:
                        print(
                            f"Invalid Opcode mode at {self.position}: {mode} is not supported!"
                        )
                        return -1

                if len(instruction) > 0:
                    print(
                        f"Invalid Opcode at {self.position}: {self.opcode[self.position]} has too many characters!"
                    )
                    return -1

                function = getattr(self, OPCODE_FUNC[opcode])
                advance = function(params)

                if self.relative < 0:
                    print("Error: Relative position cannot be below 0!")
                    return -1

                if self.halt:
                    return self.output

                if advance:
                    self.position += OPCODE_PARAMS[opcode]
            else:
                print(
                    f"Error: invalid opcode {opcode} at position {self.position}: {self.opcode[self.position]}"
                )
                return -1

    def get_value(self):
        return self.opcode[0]
