from day6.orbitmap import (
    Body,
    OrbitMap,
    read_map_file,
    neil_degrasse_tyson,
    kerbal_space_program,
)

DATA = [
    "COM)B",
    "B)C",
    "C)D",
    "D)E",
    "E)F",
    "B)G",
    "G)H",
    "D)I",
    "E)J",
    "J)K",
    "K)L",
]

XFER_DATA = DATA.copy()
XFER_DATA.extend(["K)YOU", "I)SAN"])

# Tests


def test_body_create():
    object = Body("A")
    assert isinstance(object, Body)


def test_body_variables():
    object = Body("A")
    assert object.name == "A"
    assert object.parent == ""
    assert len(object.satellites) == 0


def test_body_set_parent():
    object = Body("A")
    assert object.set_parent("B")
    assert object.parent == "B"


def test_body_fail_set_parent():
    object = Body("A")
    assert object.set_parent("B")
    assert not object.set_parent("C")
    assert object.parent == "B"


def test_body_add_satellite():
    object = Body("A")
    assert object.add_satellite("B")
    assert object.satellites == ["B"]


def test_body_fail_add_satellite():
    object = Body("A")
    assert object.add_satellite("B")
    assert not object.add_satellite("B")
    assert object.satellites == ["B"]


def test_body_no_of_satellites():
    object = Body("A")
    object.add_satellite("B")
    object.add_satellite("C")
    assert object.no_of_satellites() == 2


def test_orbitmap_create():
    object = OrbitMap()
    assert isinstance(object, OrbitMap)


def test_orbitmap_variables():
    object = OrbitMap()
    assert object.bodies == {}


def test_orbitmap_add_orbit():
    object = OrbitMap()
    assert object.add_orbit("A)B")
    assert object.add_orbit("B)C")
    assert list(object.bodies.keys()) == ["A", "B", "C"]


def test_orbitmap_fail_add_orbit_bad_string():
    object = OrbitMap()
    assert not object.add_orbit("A(B")
    assert not object.add_orbit("A")
    assert not object.add_orbit("A)B)C")


def test_orbitmap_fail_add_orbit_bad_parent():
    object = OrbitMap()
    assert object.add_orbit("A)B")
    assert not object.add_orbit("A)B")


def test_orbitmap_fail_add_orbit_bad_satellite():
    object = OrbitMap()
    assert object.add_orbit("A)B")
    assert not object.add_orbit("C)B")


def test_orbitmap_load_map_data():
    data = ["A)B", "B)C", "C)D"]
    object = OrbitMap()
    assert object.load_map_data(data)
    assert list(object.bodies.keys()) == ["A", "B", "C", "D"]


def test_orbitmap_fail_load_map_data_bad_line():
    data = ["A)B", "B)C", "B)C", "C)D"]
    object = OrbitMap()
    assert not object.load_map_data(data)
    assert list(object.bodies.keys()) == ["A", "B", "C"]


def test_orbitmap_get_orbits():
    object = OrbitMap()
    assert object.add_orbit("A)B")
    assert object.add_orbit("B)C")
    assert object.get_orbits("A") == 0
    assert object.get_orbits("B") == 1
    assert object.get_orbits("C") == 2


def test_orbitmap_get_checksum():
    object = OrbitMap()
    assert object.load_map_data(DATA)
    assert object.get_checksum() == 42


def test_orbitmap_fail_get_checksum():
    data = ["A)B", "B)C", "C)D"]
    object = OrbitMap()
    assert object.load_map_data(data)
    assert object.get_checksum() == -1


def test_orbitmap_validate_orbits():
    object = OrbitMap()
    assert object.load_map_data(DATA)
    assert object.validate_orbits()


def test_orbitmap_fail_validate_orbits_no_com():
    data = ["A)B", "B)C", "C)D"]
    object = OrbitMap()
    assert object.load_map_data(data)
    assert not object.validate_orbits()


def test_orbitmap_fail_validate_orbits_missing_parent():
    data = ["COM)A", "A)B", "B)C", "C)D", "E)F"]
    object = OrbitMap()
    assert object.load_map_data(data)
    assert not object.validate_orbits()


def test_orbitmap_get_all_orbits():
    data = ["A)B", "B)C", "C)D"]
    object = OrbitMap()
    assert object.load_map_data(data)
    assert object._get_all_orbits("A") == []
    assert object._get_all_orbits("B") == ["A"]
    assert object._get_all_orbits("C") == ["B", "A"]
    assert object._get_all_orbits("D") == ["C", "B", "A"]


def test_orbitmap_get_common_parent():
    data = ["A)B", "B)C", "C)D", "D)E", "B)F", "F)G"]
    object = OrbitMap()
    assert object.load_map_data(data)
    assert object._get_common_parent("E", "G") == "B"


def test_orbitmap_fail_get_common_parent_missing_satellite():
    data = ["A)B", "B)C", "C)D", "D)E", "B)F", "F)G", "H)I"]
    object = OrbitMap()
    assert object.load_map_data(data)
    assert object._get_common_parent("E", "J") == -1


def test_orbitmap_fail_get_common_parent_missing_parent():
    data = ["A)B", "B)C", "C)D", "D)E", "B)F", "F)G", "H)I"]
    object = OrbitMap()
    assert object.load_map_data(data)
    assert object._get_common_parent("E", "H") == -1


def test_orbitmap_fail_get_common_parent_no_common_parent():
    data = ["A)B", "B)C", "C)D", "D)E", "B)F", "F)G", "H)I"]
    object = OrbitMap()
    assert object.load_map_data(data)
    assert object._get_common_parent("E", "I") == -1


def test_orbitmap_calc_parent_transfer():
    data = ["A)B", "B)C", "C)D", "D)E", "B)F", "F)G"]
    object = OrbitMap()
    assert object.load_map_data(data)
    assert object._calc_parent_transfer("E", "B") == 2
    assert object._calc_parent_transfer("G", "B") == 1
    assert object._calc_parent_transfer("C", "B") == 0


def test_orbitmap_calc_transfer():
    object = OrbitMap()
    assert object.load_map_data(XFER_DATA)
    assert object.calc_transfer("YOU", "SAN") == 4


def test_orbitmap_fail_calc_transfer_no_common_parent():
    data = ["A)B", "B)C", "C)D", "D)E", "B)F", "F)G", "H)I"]
    object = OrbitMap()
    assert object.load_map_data(data)
    assert object.calc_transfer("E", "I") == -1


def test_read_map_file():
    map_file = "test.txt"
    expected = [
        "COM)B",
        "B)C",
        "C)D",
        "D)E",
        "E)F",
        "B)G",
        "G)H",
        "D)I",
        "E)J",
        "J)K",
        "K)L",
    ]
    result = read_map_file(map_file)
    assert expected == result


def test_neil_degrasse_tyson():
    map_file = "test.txt"
    result = neil_degrasse_tyson(map_file)
    assert result == 42


def test_neil_degrasse_tyson_fail_bad_checksum():
    map_file = "test_bad.txt"
    result = neil_degrasse_tyson(map_file)
    assert result == -1


def test_kerbal_space_program():
    map_file = "test_transfer.txt"
    result = kerbal_space_program(map_file)
    assert result == 4


def test_kerbal_space_program_fail_bad_checksum():
    map_file = "test_bad.txt"
    result = kerbal_space_program(map_file)
    assert result == -1


def test_kerbal_space_program_fail_calc_transfer():
    map_file = "test_transfer_bad.txt"
    result = kerbal_space_program(map_file)
    assert result == -1
