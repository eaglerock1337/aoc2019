from day14.factory import (
    Reaction,
    NanoFactory,
    read_formulas,
    minecraft,
    satisfactory,
)

TEST = [
    "10 ORE => 10 A",
    "1 ORE => 1 B",
    "7 A, 1 B => 1 C",
    "7 A, 1 C => 1 D",
    "7 A, 1 D => 1 E",
    "7 A, 1 E => 1 FUEL",
]

TEST2 = [
    "9 ORE => 2 A",
    "8 ORE => 3 B",
    "7 ORE => 5 C",
    "3 A, 4 B => 1 AB",
    "5 B, 7 C => 1 BC",
    "4 C, 1 A => 1 CA",
    "2 AB, 3 BC, 4 CA => 1 FUEL",
]

# Tests


def test_reaction_create():
    ingredients = {"A": 5, "B": 10, "C": 15}
    object = Reaction("FUEL", 2, ingredients)
    assert isinstance(object, Reaction)
    assert object.name == "FUEL"
    assert object.amount == 2
    assert object.ingredients == ingredients


def test_nanofactory_create():
    object = NanoFactory()
    assert isinstance(object, NanoFactory)
    assert object.formulas == {}
    assert object.inventory == {}
    assert object.used_ore == 0


def test_nanofactory_import():
    object = NanoFactory()
    object.input_formulas(TEST)
    assert list(object.formulas.keys()) == ["A", "B", "C", "D", "E", "FUEL"]
    assert object.formulas["C"].amount == 1
    assert object.formulas["A"].ingredients == {"ORE": 10}


def test_nanofactory_add_inventory():
    object = NanoFactory()
    object._add_inventory("A", 10)
    assert object.inventory == {"A": 10}
    object._add_inventory("A", 5)
    assert object.inventory == {"A": 15}


def test_nanofactory_remove_inventory():
    object = NanoFactory()
    object._add_inventory("A", 25)
    object._remove_inventory("A", 10)
    assert object.inventory == {"A": 15}


def test_nanofactory_needed_inventory():
    object = NanoFactory()
    object.input_formulas(TEST)
    object._add_inventory("A", 25)
    object._add_inventory("B", 10)
    assert object._needed_inventory("A", 10) == 0
    assert object._needed_inventory("A", 30) == 5
    assert object._needed_inventory("A", 36) == 11
    assert object._needed_inventory("B", 15) == 5
    assert object._needed_inventory("C", 5) == 5


def test_nanofactory_get_inventory():
    object = NanoFactory()
    object.input_formulas(TEST)
    object._get_inventory("A", 45)
    assert object.inventory["A"] == 50
    assert object.used_ore == 50
    object._get_inventory("A", 5)
    assert object.inventory["A"] == 60
    assert object.used_ore == 60


def test_nanofactory_get_inventory_recursive():
    object = NanoFactory()
    object.input_formulas(TEST)
    object._get_inventory("FUEL", 1)
    assert object.inventory["FUEL"] == 1
    print(object.inventory)
    assert object.inventory["A"] == 2
    assert object.used_ore == 31


def test_nanofactory_calculate_fuel():
    object = NanoFactory()
    object.input_formulas(TEST)
    assert object.calculate_fuel(1) == 31
    object.reset()
    assert object.calculate_fuel(2) == 62
    object.reset()
    assert object.calculate_fuel(10) == 290


def test_nanofactory_calculate_fuel_2():
    object = NanoFactory()
    object.input_formulas(TEST2)
    for formula, reaction in object.formulas.items():
        print(f"{formula}: {reaction.amount} / {reaction.ingredients}")
    assert object.calculate_fuel(1) == 165


def test_calculate_total_fuel():
    filename = "test.txt"
    formulas = read_formulas(filename)
    object = NanoFactory()
    object.input_formulas(formulas)
    assert object.calculate_total_fuel() == 82892753


def test_read_formulas():
    filename = "test.txt"
    result = read_formulas(filename)
    assert len(result) == 9
    assert result[0] == "157 ORE => 5 NZVS"
    assert result[3] == "12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ"
    assert result[7] == "165 ORE => 2 GPVTF"


def test_minecraft():
    filename = "test.txt"
    assert minecraft(filename, 1) == 13312


def test_minecraft_2():
    filename = "test2.txt"
    assert minecraft(filename, 1) == 180697


def test_minecraft_3():
    filename = "test3.txt"
    assert minecraft(filename, 1) == 2210736


def test_satisfactory():
    filename = "test.txt"
    assert satisfactory(filename) == 82892753


def test_satisfactory_2():
    filename = "test2.txt"
    assert satisfactory(filename) == 5586022


def test_satisfactory_3():
    filename = "test3.txt"
    assert satisfactory(filename) == 460664
