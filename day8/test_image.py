from day8.image import SpaceImage, read_image_file, paging_mr_herman, remember_the_alamo

TEST = "000033111233010133012033000133001233012223"
TEST2 = "0222112222120000"

# Tests


def test_spaceimage_create():
    object = SpaceImage(3, 2)
    assert isinstance(object, SpaceImage)


def test_spaceimage_values():
    object = SpaceImage(3, 2)
    assert object.width == 3
    assert object.height == 2
    assert object.image == []
    assert object.decoded == []


def test_spaceimage_import_data():
    data = "123456789012"
    expected = [["123", "456"], ["789", "012"]]
    object = SpaceImage(3, 2)
    assert object.import_data(data)
    assert object.image == expected


def test_spaceimage_fail_import_data_incomplete_line():
    data = "12345678"
    expected = [["123", "456"], []]
    object = SpaceImage(3, 2)
    assert not object.import_data(data)
    assert object.image == expected


def test_spaceimage_fail_import_data_missing_line():
    data = "123456789"
    expected = [["123", "456"], ["789"]]
    object = SpaceImage(3, 2)
    assert not object.import_data(data)
    assert object.image == expected


def test_spaceimage_get_layer_value_sum():
    object = SpaceImage(3, 2)
    assert object.import_data(TEST)
    assert object._get_layer_value_sum(0, "0") == 4
    assert object._get_layer_value_sum(1, "1") == 3
    assert object._get_layer_value_sum(2, "2") == 0
    assert object._get_layer_value_sum(6, "2") == 3


def test_spaceimage_find_min_layer():
    object = SpaceImage(3, 2)
    assert object.import_data(TEST)
    layer = object._find_min_layer("0")
    assert layer == 1
    layer = object._find_min_layer("1")
    assert layer == 0
    layer = object._find_min_layer("2")
    assert layer == 0
    layer = object._find_min_layer("3")
    assert layer == 6


def test_spaceimage_get_checksum():
    object = SpaceImage(3, 2)
    assert object.import_data(TEST)
    checksum = object.get_checksum()
    assert checksum == 3


def test_spaceimage_get_visible_pixel():
    object = SpaceImage(2, 2)
    assert object.import_data(TEST2)
    assert object._get_visible_pixel(0, 0) == "0"
    assert object._get_visible_pixel(0, 1) == "1"
    assert object._get_visible_pixel(1, 0) == "1"
    assert object._get_visible_pixel(1, 1) == "0"


def test_spaceimage_fail_get_visible_pixel():
    data = "2222212222122000"
    object = SpaceImage(2, 2)
    assert object.import_data(data)
    assert object._get_visible_pixel(0, 0) == -1


def test_spaceimage_decode():
    object = SpaceImage(2, 2)
    result = ["01", "10"]
    assert object.import_data(TEST2)
    assert object.decode()
    assert object.decoded == result


def test_spaceimage_fail_decode_missing_pixel():
    data = "2222212222122000"
    object = SpaceImage(2, 2)
    assert object.import_data(data)
    assert not object.decode()


def test_read_image_file():
    filename = "test.txt"
    result = read_image_file(filename)
    assert result == TEST


def test_paging_mr_herman():
    filename = "test.txt"
    width = 3
    height = 2
    checksum = paging_mr_herman(filename, width, height)
    assert checksum == 3


def test_paging_mr_herman_bad_file():
    filename = "test_bad.txt"
    width = 3
    height = 2
    checksum = paging_mr_herman(filename, width, height)
    assert checksum == -1


def test_remember_the_alamo():
    filename = "test2.txt"
    result = ["01", "10"]
    width = 2
    height = 2
    image = remember_the_alamo(filename, width, height)
    assert image == result


def test_remember_the_alamo_fail_import():
    filename = "test_bad.txt"
    width = 2
    height = 2
    image = remember_the_alamo(filename, width, height)
    assert image == -1


def test_remember_the_alamo_fail_decode():
    filename = "test2_bad.txt"
    width = 2
    height = 2
    image = remember_the_alamo(filename, width, height)
    assert image == -1
