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

# Tests

def test_read_formulas():
    string = "test.txt"
    result = read_formulas(string)
    assert len(result) == 9
    assert result[0] == "157 ORE => 5 NZVS"
    assert result[3] == "12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ"
    assert result[7] == "165 ORE => 2 GPVTF"

def test_minecraft():
    pass


def test_satisfactory():
    pass
