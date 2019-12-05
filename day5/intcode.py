import os

OPCODE_FILE = "opcode.txt"
OPCODE_FUNC = {
    '01': '_opcode_1',
    '02': '_opcode_2',
    '03': '_opcode_3',
    '04': '_opcode_4'
}
OPCODE_PARAMS = {
    '01': 3,
    '02': 3,
    '03': 1,
    '04': 1
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
        params[0] - first number to add
        params[1] - second number to add
        params[2] - location to store sum
        """
        num1, num2, result = params
        self.opcode[result] = num1 + num2

    def _opcode_2(self, params):
        """
        Opcode 2: Multiply two numbers
        params[0] - first number to multiply
        params[1] - second number to multiply
        params[2] - location to store product
        """
        num1, num2, result = params
        self.opcode[result] = num1 * num2

    def _opcode_3(self, params):
        """
        Opcode 3: Accept input from user
        params[0] - location to store
        """
        value = int(input("Please enter a value: "))
        self.opcode[params.pop()] = value

    def _opcode_4(self, params):
        """
        Opcode 4: Output value from location
        params[0] - location of value to output
        """
        print(f"OUTPUT: {self.opcode[params.pop()]}")

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

                for i in range(1, OPCODE_PARAMS[opcode]):
                    try:
                        mode = instruction.pop() 
                    except IndexError:
                        mode = '0'
                    
                    if mode == '0':
                        param_pos = self.opcode[self.position + i]
                        if param_pos < self.length:
                            params.append(self.opcode[param_pos])
                        else:
                            print(f"Invalid Opcode reference at {self.position}: {param_pos} is out of range!")
                            return

                    elif mode == '1':
                        if self.position + i < self.length:
                            params.append(self.opcode[self.position + i])
                        else:
                            print(f"Ran out of opcode values at {self.position}: {self.position + i} is out of range!")
                            return
                
                if len(instruction) > 0:
                    print(f"Invalid Opcode at {self.position}: {self.opcode[self.position]} has too many characters!")
                    return

                if self.position + OPCODE_PARAMS[opcode] < self.length:
                    last_param_pos = self.opcode[self.position + OPCODE_PARAMS[opcode]]
                    if last_param_pos < self.length:
                        params.append(last_param_pos)
                    else:
                        print(f"Invalid Opcode reference at {self.position}: storage location {last_param_pos} is out of range!")
                        return
                else:
                    print(f"Invalid Opcode at {self.position}: ran out of values!")
                    return

                function=getattr(self, OPCODE_FUNC[opcode])
                function(params)
                self.position += OPCODE_PARAMS[opcode] + 1
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
    opcode = read_opcode(filename)

    print(f"Running TEST program...")
    computer = IntCode(opcode)
    computer.run()


if __name__ == "__main__":
    find_pebkac_error(OPCODE_FILE)
