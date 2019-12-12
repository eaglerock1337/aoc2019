from day12.jupiter import Jupiter, read_moons

TEST = [
    "<x=-1, y=0, z=2>\n",
    "<x=2, y=-10, z=-7>\n",
    "<x=4, y=-8, z=8>\n",
    "<x=3, y=5, z=-1>",
]

# Tests


def test_jupiter_create():
    expected = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
    object = Jupiter()
    assert isinstance(object, Jupiter)
    assert object.position == []
    assert object.velocity == expected
    assert object.moons == 0
    assert object.coords == 0
    assert object.steps == 0


def test_jupiter_import_data():
    expected = [
        [-1, 0, 2],
        [2, -10, -7],
        [4, -8, 8],
        [3, 5, -1],
    ]
    object = Jupiter()
    object.import_data(TEST)
    assert object.moons == 4
    assert object.coords == 3
    assert object.position == expected


def test_jupiter_step():
    pos = [
        [2, -1, 1],
        [3, -7, -4],
        [1, -7, 5],
        [2, 2, 0],
    ]
    vel = [
        [3, -1, -1],
        [1, 3, 3],
        [-3, 1, -3],
        [-1, -3, 1],
    ]
    object = Jupiter()
    object.import_data(TEST)
    object.step()
    assert object.steps == 1
    assert object.position == pos
    assert object.velocity == vel


def test_jupiter_multi_step():
    pos = [
        [2, 1, -3],
        [1, -8, 0],
        [3, -6, 1],
        [2, 0, 4],
    ]
    vel = [
        [-3, -2, 1],
        [-1, 1, 3],
        [3, 2, -3],
        [1, -1, -1],
    ]
    object = Jupiter()
    object.import_data(TEST)
    object.step()
    assert object.steps == 1
    object.step(1)
    assert object.steps == 2
    object.step(3)
    assert object.steps == 5
    object.step(0)
    assert object.steps == 5
    object.step(5)
    assert object.steps == 10
    assert object.position == pos
    assert object.velocity == vel


def test_read_moons():
    file = "test.txt"
    assert read_moons(file) == TEST