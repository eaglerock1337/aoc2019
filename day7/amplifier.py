from itertools import permutations

from intcode import IntCode

import os

PROGRAM_FILE = "software.txt"
PHASES = [0, 1, 2, 3, 4]

class Amplifier:
    """
    Defines a single amplifier for use in in the Thruster circuit.
    """
    def __init__(self, software):
        self.software = software
        self.phase = -1

    def set_phase(self, phase):
        """
        Sets the Phase Setting for the Amplifier
        """
        self.phase = phase

    def run(self, instruction):
        """
        Runs the Amplifier software with the provided instruction and returns the output.
        """
        if self.phase == -1:
            print("Error: No phase setting was provided!")
            return -1

        program = IntCode(self.software, [self.phase, instruction])
        output = program.run()
        return output.pop()


class Thrusters:
    """
    Thrusters class that uses 5 Amplifiers to provide an output to the Thrusters.
    """
    def __init__(self, software):
        self.amps = []
        for _ in range(5):
            self.amps.append(Amplifier(software))
        self.phases = PHASES

    def get_best_output(self):
        """
        Return the phase configuration that returns the best output.
        """
        best_output = 0
        best_phases = []

        for phases in permutations(self.phases):
            instruction = 0

            for amp, phase in zip(self.amps, phases):
                amp.set_phase(phase)
                instruction = amp.run(instruction)

            if instruction > best_output:
                best_output = instruction
                best_phases = list(phases)

        return best_output, best_phases


def read_opcode(filename):
    """
    Read in the opcode from a given filename and return as a list.
    Currently only reads in a single opcode from the file.
    """
    if os.path.basename(os.getcwd()) == "aoc2019":
        filename = os.path.join("day7", filename)

    with open(filename, "r") as opcode_file:
        opcode = opcode_file.readline()

    string_opcode = opcode.split(",")
    return [int(i) for i in string_opcode]


def ramming_speed(filename):
    """
    Ash: RAMMING SPEED!
    This...is my BOOM STICK!
    """
    program = read_opcode(filename)
    thrusters = Thrusters(program)
    output, phases = thrusters.get_best_output()
    print(f"The best output is {output}")
    print(f"The phase list is {phases}!")

    return output


if __name__ == "__main__":
    ramming_speed(PROGRAM_FILE)