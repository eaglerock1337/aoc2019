import os
import re

from math import ceil, floor

FORMULA_FILE = "formulas.txt"


class Reaction:
    """
    A reaction that will process materials/chemicals into another.
    """

    def __init__(self, formula, amount, ingredients):
        self.name = formula
        self.amount = amount
        self.ingredients = ingredients


class NanoFactory:
    """
    NanoFactory class responsible for processing ores into fuel.
    """

    def __init__(self):
        self.formulas = {}
        self.inventory = {}
        self.used_ore = 0
        self.total_ore = 1000000000000

    def input_formulas(self, formulas):
        """
        Input a list of formulas that define individual reactions
        that can be made by the NanoFactory.
        """
        num_digit = re.compile(r"(?:(\d+)\s(\w+))")

        for line in formulas:
            ingredients = {}
            results = num_digit.findall(line)
            formula_amount, formula = results.pop()

            for ingredient in results:
                amount, item = ingredient
                ingredients[item] = int(amount)

            self.formulas[formula] = Reaction(formula, int(formula_amount), ingredients)

    def _add_inventory(self, chemical, amount):
        """
        Add the specified amount of chemical to the inventory.
        """
        if chemical in self.inventory:
            self.inventory[chemical] += amount
        else:
            self.inventory[chemical] = amount

    def _remove_inventory(self, chemical, amount):
        """
        Remove the specified amount of chemical from the inventory.
        """
        self.inventory[chemical] -= amount

    def _needed_inventory(self, chemical, amount):
        """
        Calculate the needed inventory to satisfy the amount of chemical provided..
        """
        if chemical in self.inventory:
            if self.inventory[chemical] > amount:
                return 0
            else:
                return amount - self.inventory[chemical]
        else:
            return amount

    def _get_inventory(self, chemical, amount):
        """
        Recursive function to add the required ingredients for the specified
        chemical to the inventory. Will call itself recursively to add all
        chained sub-ingredients needed to tally the necessary ore. Will only
        add an amount that is a multiple that the formula is for.
        """
        reaction_amount = self.formulas[chemical].amount
        reactions = ceil(amount / reaction_amount)
        ingredients = self.formulas[chemical].ingredients

        for ingredient, subamount in ingredients.items():
            if ingredient == "ORE":
                self.used_ore += subamount * reactions
                self.total_ore -= subamount * reactions
            else:
                needed = self._needed_inventory(ingredient, subamount * reactions)
                if needed > 0:
                    self._get_inventory(ingredient, needed)
                self._remove_inventory(ingredient, subamount * reactions)

        self._add_inventory(chemical, reactions * reaction_amount)

    def calculate_fuel(self, amount):
        """
        Calculate the amount of ore necessary for the required
        amount of fuel.
        """
        self._get_inventory("FUEL", amount)
        return self.used_ore

    def calculate_total_fuel(self):
        """
        Calculate the amount of fuel that can be processed with the limited ore.
        """
        upper = 1000000000000
        lower = 1
        while True:
            target = int(floor((upper + lower) / 2))
            if target == lower:
                return lower

            self.reset()
            self.calculate_fuel(target)

            if self.total_ore < 0:
                upper = target
            else:
                lower = target

    def reset(self):
        """
        Reset the object for another use.
        """
        self.inventory = {}
        self.used_ore = 0
        self.total_ore = 1000000000000


def read_formulas(filename):
    """
    Read in the formulas from a given filename and return as a list.
    List will be formatted as follows: "1 A, 2 B, 3 C => 4 D"
    """
    if os.path.basename(os.getcwd()) == "aoc2019":
        filename = os.path.join("day14", filename)

    with open(filename, "r") as formula_file:
        return formula_file.read().splitlines()


def minecraft(filename, fuel):
    """
    Hello, my name is Peter, and welcome to my Let's Play for Minecraft.
    Today we're going to punch a crapload of trees and magically build
    a house, at least until a creeper comes by and fucks it up.
    """
    formulas = read_formulas(filename)
    creeper = NanoFactory()
    creeper.input_formulas(formulas)
    ore = creeper.calculate_fuel(fuel)

    print(f"The amount of ore required to produce {fuel} fuel: {ore}")
    return ore


def satisfactory(filename):
    """
    Let's mine some ore. Now, let's build a HUB. Now, let's exploit the
    entire planet for its resources, killing off any flora and fauna in
    the process, leaving only acres of factories and smoke! Yay!
    """
    formulas = read_formulas(filename)
    creeper = NanoFactory()
    creeper.input_formulas(formulas)
    fuel = creeper.calculate_total_fuel()

    print(f"The total amount of fuel you can make: {fuel}")
    return fuel


if __name__ == "__main__":
    minecraft(FORMULA_FILE, 1)
    satisfactory(FORMULA_FILE)
