import os
import re

FORMULA_FILE = "formulas.txt"


class Reaction:
    """
    A reaction that will process materials/chemicals into another.
    """

    def __init__(self, formula, amount, ingredients):
        self.name = formula
        self.amount = amount
        self.ingredients = ingredients

    def get_requirements(self, amount):
        """
        Return the requirements needed for the specified amount of
        chemical. Will return rounded-up values to 
        """
        pass


class NanoFactory:
    """
    NanoFactory class responsible for processing ores into fuel.
    """

    def __init__(self):
        self.formulas = {}
        self.inventory = {}

    def input_formulas(self, formulas):
        """
        Input a list of formulas that define individual reactions
        that can be made by the NanoFactory.
        """
        num_digit = re.compile(r"(?:(\d+)\s(\w+))")

        for line in formulas:
            ingredients = {}
            results = num_digit.findall(line)
            amount, formula = results.pop()

            for ingredient in results:
                amount, item = ingredient
                ingredients[item] = int(amount)

            self.inventory[formula] = Reaction(formula, int(amount), ingredients)

    def _needed_inventory(self, chemical, amount):
        """
        Calculate the needed inventory to satisfy the amount of chemical.
        """
        pass

    def _add_inventory(self, chemical, amount):
        """
        Add the specified amount of chemical to the inventory.
        """
        pass

    def _remove_inventory(self, chemical, amount):
        """
        Remove the specified amount of chemical from the inventory.
        """
        pass

    def calculate_fuel(self, amount):
        """
        Calculate the amount of ore necessary for the required
        amount of fuel.
        """
        pass



def read_formulas(filename):
    """
    Read in the formulas from a given filename and return as a list.
    List will be formatted as follows: "1 A, 2 B, 3 C => 4 D"
    """
    if os.path.basename(os.getcwd()) == "aoc2019":
        filename = os.path.join("day14", filename)

    with open(filename, "r") as formula_file:
        return formula_file.read().splitlines()


def minecraft(filename):
    """
    Hello, my name is Peter, and welcome to my Let's Play for Minecraft.
    Today we're going to punch a crapload of trees and magically build
    a house, at least until a creeper comes by and fucks it up.
    """
    pass


def satisfactory(filename):
    """
    Let's mine some ore. Now, let's build a HUB. Now, let's exploit the
    entire planet for its resources, killing off any flora and fauna in
    the process, leaving only acres of factories and smoke! Yay!
    """
    pass


if __name__ == "__main__":
    minecraft(FORMULA_FILE)
    # satisfactory(FORMULA_FILE)
