import os


IMAGEFILE = "image.txt"
WIDTH = 25
HEIGHT = 6


class SpaceImage:
    """
    The class for defining the Space Image Format.
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.image = []
        self.decoded = []

    def import_data(self, data):
        """
        Import image data in Space Image Format
        """
        chunks = [data[i : i + self.width] for i in range(0, len(data), self.width)]

        layer = 0
        self.image.append([])

        for chunk in chunks:
            if len(self.image[layer]) == self.height:
                layer += 1
                self.image.append([])

            if len(chunk) != self.width:
                print("Error: Not enough data to fill line!")
                return False

            self.image[layer].append(chunk)

        if len(self.image[-1]) != self.height:
            print("Error: Last layer does not have the right height!")
            return False

        return True

    def _get_layer_value_sum(self, layer, value):
        """
        Sum the number of instance the provided value appears in the provided layer.
        """
        sum = 0
        for row in self.image[layer]:
            for char in row:
                if char == value:
                    sum += 1

        return sum

    def _find_min_layer(self, value):
        """
        Find the layer with the minimum sum of the provided value.
        """
        min_layer = -1
        min_sum = -1
        for layer in range(len(self.image)):
            sum = self._get_layer_value_sum(layer, value)
            if sum < min_sum or layer == 0:
                min_layer = layer
                min_sum = sum

        return min_layer

    def get_checksum(self):
        """
        Get a checksum of the provided image.
        Checksum is found by finding the layer with the minimum number of '0's,
        then multiplying the sum of the '1' and the '2's in that layer.
        """
        layer = self._find_min_layer("0")
        ones = self._get_layer_value_sum(layer, "1")
        twos = self._get_layer_value_sum(layer, "2")
        return ones * twos

    def _get_visible_pixel(self, xpos, ypos):
        """
        Determine the visible pixel for the provided XY coordinate in the image.
        Returns either a '0' (black) or a '1' (white), as '2' is transparent and
        will display the layer(s) below until an opaque pixel is found.
        """
        for layer in range(len(self.image)):
            layer_pixel = self.image[layer][ypos][xpos]
            if layer_pixel != "2":
                return layer_pixel

        print(f"Error: XY position {xpos},{ypos} does not have a visible pixel!")
        return -1

    def decode(self):
        """
        Decodes the image and stores it in self.decoded.
        """
        for ypos in range(self.height):
            string = ""
            for xpos in range(self.width):
                pixel = self._get_visible_pixel(xpos, ypos)

                if pixel == -1:
                    print(f"Error: Could not decode: image is missing a visible pixel!")
                    return False

                string += pixel

            self.decoded.append(string)

        return True


def read_image_file(filename):
    """
    Read an image file and return as a variable
    """
    if os.path.basename(os.getcwd()) == "aoc2019":
        filename = os.path.join("day8", filename)

    with open(filename, "r") as valuefile:
        return valuefile.readline()


def paging_mr_herman(filename, width, height):
    """
    PAGING MR. HERMAN! MR. HERMAN!
    YOU HAVE A TELEPHONE CALL AT THE FRONT DESK!
    """
    image_data = read_image_file(filename)
    image = SpaceImage(width, height)

    if not image.import_data(image_data):
        print("Error: Could not import data!")
        return -1

    checksum = image.get_checksum()
    print(f"Checksum: {checksum}")

    return checksum


def remember_the_alamo(filename, width, height):
    """
    Hey kid, what's your name? I can't remember!
    Where you from? ...I can't remember.
    Can't you remember anything? I remember...the Alamo.
    YEEEEEEEEEEEEEEEEEEEEEEEEEHAW!!!!!!!!!!!!!!!!!!!
    """
    image_data = read_image_file(filename)
    image = SpaceImage(width, height)

    if not image.import_data(image_data):
        print("Error: Could not import data!")
        return -1

    if not image.decode():
        print("Failed to decode image!")
        return -1

    print("Decoded image:")
    for line in image.decoded:
        print(line)

    return image.decoded


if __name__ == "__main__":
    paging_mr_herman(IMAGEFILE, WIDTH, HEIGHT)
    remember_the_alamo(IMAGEFILE, WIDTH, HEIGHT)
