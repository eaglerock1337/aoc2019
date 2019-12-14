from intcode import IntCode

import os

ARCADE_FILE = "arcade.txt"


class Arcade:
    """
    Arcade cabinet simulator running Intcode software.
    """

    def __init__(self, software):
        self.screen = [[0 for x in range(43)] for y in range(23)]
        self.software = IntCode(software)
        self.ballpos = -1
        self.paddlepos = -1
        self.score = -1

    def run(self):
        """
        Runs the arcade software and processes the output accordingly.
        """
        output = self.software.run()
        output.reverse()

        while len(output) > 0:
            x = output.pop()
            y = output.pop()
            tile = output.pop()
            self.screen[y][x] = tile

    def count_blocks(self):
        """
        Count the number of blocks in the list.
        """
        count = 0
        for row in self.screen:
            count += row.count(2)

        return count

    def print_screen(self):
        """
        Print the current screen.
        """
        for row in self.screen:
            print("".join(map(str, row)))

    def insert_quarter(self):
        """
        Inserts a quarter in order to play the game.
        """
        self.software.opcode[0] = 2

    def play_to_win(self):
        """
        Play the game to win. Provides joystick inputs based on the ball position.
        """
        while self.software.halt or self.ballpos == -1:
            output = self.software.run()
            output.reverse()

            while len(output) > 0:
                x = output.pop()
                y = output.pop()
                tile = output.pop()

                if x == -1 and y == 0:
                    self.score = tile
                else:
                    self.screen[y][x] = tile
                    if tile == 3:
                        self.paddlepos = x
                    elif tile == 4:
                        self.ballpos = x

            if self.ballpos > self.paddlepos:
                self.software.add_input(1)
            elif self.ballpos < self.paddlepos:
                self.software.add_input(-1)
            else:
                self.software.add_input(0)


def read_opcode(filename):
    """
    Read in the opcode from a given filename and return as a list.
    Currently only reads in a single opcode from the file.
    """
    if os.path.basename(os.getcwd()) == "aoc2019":
        filename = os.path.join("day13", filename)

    with open(filename, "r") as opcode_file:
        opcode = opcode_file.readline()

    string_opcode = opcode.split(",")
    return [int(i) for i in string_opcode]


def noahs_arcade(filename):
    """
    Come bust a move where the games are played.
    It's chill, it's fresh, it's Noah's Arcade.
    What do you think of that?
    """
    software = read_opcode(filename)
    game = Arcade(software)
    game.run()
    print("Here's the screen:")
    game.print_screen()
    count = game.count_blocks()

    print(f"\nThe number of blocks is: {count}")
    return count


def pinball_wizard(filename):
    """
    He plays by intuition, the digit counters fall.
    That deaf, dumb, and blind kid sure plays a mean pinball!
    """
    software = read_opcode(filename)
    game = Arcade(software)
    print("Inserting quarter and playing to win...")
    game.insert_quarter()
    game.play_to_win()

    print(f"The final score is: {game.score}")
    return game.score


if __name__ == "__main__":
    noahs_arcade(ARCADE_FILE)
    pinball_wizard(ARCADE_FILE)
