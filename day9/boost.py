from intcode import IntCode

import os

BOOST_FILE = "boost.txt"


def read_opcode(filename):
    """
    Read in the opcode from a given filename and return as a list.
    Currently only reads in a single opcode from the file.
    """
    if os.path.basename(os.getcwd()) == "aoc2019":
        filename = os.path.join("day9", filename)

    with open(filename, "r") as opcode_file:
        opcode = opcode_file.readline()

    string_opcode = opcode.split(",")
    return [int(i) for i in string_opcode]


def thank_you_captain(filename, instruction):
    """
    Captain Riggs! Captain Murtaugh! Thank you Captain! Thank you Captain!
    Thank YOU, Captain! Thank YOU, Captain! Oh Captain, My Captain!
    ENOUGH WITH THE CAPTAIN SHIT! Now, get out of here!
    """
    boost = read_opcode(filename)
    computer = IntCode(boost, [instruction])

    output = computer.run()
    keycode = output.pop()

    print(f"BOOST Keycode: {keycode}")
    return keycode


if __name__ == "__main__":
    thank_you_captain(BOOST_FILE, 1)
    thank_you_captain(BOOST_FILE, 2)
