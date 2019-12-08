from itertools import permutations

from intcode import IntCode

import os

PROGRAM_FILE = "software.txt"
PHASES = [0, 1, 2, 3, 4]
FEEDBACK_PHASES = [5, 6, 7, 8, 9]


class Amplifier:
    """
    Defines a single amplifier for use in in the Thruster circuit.
    """

    def __init__(self, software):
        self.software = software
        self.phase = -1
        self.primed = False

    def prime(self, phase=""):
        """
        Primes the Amplifier by resetting the software and setting the phase.
        """
        self.phase = phase if phase != "" else self.phase
        self.program = IntCode(self.software, [self.phase])
        self.primed = True

    def run(self, instruction):
        """
        Runs the Amplifier software with the provided instruction and returns the output.
        """
        if not self.primed:
            print("Error: Amplifier was not primed!")
            return -1

        self.program.add_input(instruction)
        output = self.program.run()
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
        self.feedback_phases = FEEDBACK_PHASES

    def get_best_output(self):
        """
        Return the phase configuration that returns the best output.
        """
        best_output = 0
        best_phases = []

        for phases in permutations(self.phases):
            instruction = 0

            for amp, phase in zip(self.amps, phases):
                amp.prime(phase)
                instruction = amp.run(instruction)

            if instruction > best_output:
                best_output = instruction
                best_phases = list(phases)

        return best_output, best_phases

    def get_best_feedback_output(self):
        """
        Return the phase configuration that returns the best output in feedback mode.
        """
        best_output = 0
        best_phases = []

        for phases in permutations(self.feedback_phases):
            instruction = 0

            for amp, phase in zip(self.amps, phases):
                amp.prime(phase)

            loop = True
            while loop:
                for amp in self.amps:
                    instruction = amp.run(instruction)
                    if not amp.program.halt:
                        loop = False

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


def this_is_spinal_tap(filename):
    """
    All of these...go...to...eleven!
    Is it any louder?
    Well, it's one louder, isn't it?
    """
    program = read_opcode(filename)
    thrusters = Thrusters(program)
    output, phases = thrusters.get_best_feedback_output()
    print(f"The best feedback output is {output}")
    print(f"The phase list is {phases}!")

    return output


if __name__ == "__main__":
    ramming_speed(PROGRAM_FILE)
    this_is_spinal_tap(PROGRAM_FILE)
