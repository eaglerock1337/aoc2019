INPUT = "183564-657474"


class Password:
    """
    Basic class for handling a 6-digit password object and checking it for validity.
    Allows each digit to be handled separately.
    """

    def __init__(self, a, b, c, d, e, f):
        self.a = int(a)  # 100,000s digit
        self.b = int(b)  #  10,000s digit
        self.c = int(c)  #   1,000s digit
        self.d = int(d)  #     100s digit
        self.e = int(e)  #      10s digit
        self.f = int(f)  #       1s digit
        self.number = (
            self.a * 100000
            + self.b * 10000
            + self.c * 1000
            + self.d * 100
            + self.e * 10
            + self.f
        )

    def is_part1_valid(self):
        """
        Returns true if the password is valid, false if it is not.
        Valid numbers can only have incrementing numbers (0 not included) and must include at least 2 duplicate numbers.
        """
        if 0 <= self.a <= self.b <= self.c <= self.d <= self.e <= self.f <= 9:
            if (
                self.a == self.b
                or self.b == self.c
                or self.c == self.d
                or self.d == self.e
                or self.e == self.f
            ):
                return True
            else:
                return False
        else:
            return False

    def is_part2_valid(self):
        """
        Returns true if password is valid, false if it is not.
        Valid numbers are the same as in is_part1_valid() but also require even sets of duplicate numbers.
        I could've done this with recursion but I'm lazy.
        """
        if self.is_part1_valid():
            if self.a == self.b and self.b != self.c:
                return True

            if self.b == self.c and self.a != self.b and self.c != self.d:
                return True

            if self.c == self.d and self.b != self.c and self.d != self.e:
                return True

            if self.d == self.e and self.c != self.d and self.e != self.f:
                return True

            if self.e == self.f and self.d != self.e:
                return True

            return False
        else:
            return False

    def get(self):
        return self.number


class DatPassword:
    """
    Get Dat Password.
    Accepts an input string for determining the range of the test.

    When test is run, a list of valid passwords is stored in self.results.
    """

    def __init__(self, input):
        self._parse_input(input)
        self.part1_results = []
        self.part2_results = []

    def _parse_input(self, input):
        if len(input) == 13:
            self.start = Password(
                input[0], input[1], input[2], input[3], input[4], input[5]
            )
            self.end = Password(
                input[7], input[8], input[9], input[10], input[11], input[12]
            )
        else:
            print("Error: invalid input string!")
            self.start = None
            self.end = None

    def run_test(self):
        if self.start is None or self.end is None:
            print("Error: cannot run test...no start/end provided!")
            return

        for a in range(self.start.a, self.end.a + 1):
            for b in range(a, 10):
                for c in range(b, 10):
                    for d in range(c, 10):
                        for e in range(d, 10):
                            for f in range(e, 10):
                                test = Password(a, b, c, d, e, f)
                                if (
                                    test.is_part1_valid()
                                    and test.get() >= self.start.get()
                                    and test.get() <= self.end.get()
                                ):
                                    self.part1_results.append(test.get())
                                    if test.is_part2_valid():
                                        self.part2_results.append(test.get())

    def get_part1_number(self):
        return len(self.part1_results)

    def get_part2_number(self):
        return len(self.part2_results)


def hack_the_planet(input):
    """
    HACK THE PLANET!!! HAAAACK THE PLAAAANEEET!!!!
    YEAAAH! HACK THE PLANET! HACK THE PLANET!
    """
    zero_cool = DatPassword(input)
    print(f"Running test from {zero_cool.start.get()} to {zero_cool.end.get()}")
    zero_cool.run_test()
    print(f"A total of {zero_cool.get_part1_number()} part 1 passwords were found!")
    print(f"A total of {zero_cool.get_part2_number()} part 2 passwords were found!")

    return zero_cool.get_part1_number(), zero_cool.get_part2_number()


if __name__ == "__main__":
    hack_the_planet(INPUT)
