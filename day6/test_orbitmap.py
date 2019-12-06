from day6.orbitmap import Body, OrbitMap, read_map_file, neil_degrasse_tyson

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
