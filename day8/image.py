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

    def import_data(self, data):
        """
        Import image data in Space Image Format
        """
        chunks = [data[i:i+self.width] for i in range(0, len(data), self.width)]
        
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
        sum = 0
        for row in self.image[layer]:
            for char in row:
                if char == value:
                    sum += 1

        return sum

    def _find_min_layer(self, value):
        min_layer = -1
        min_sum = -1
        for layer in range(len(self.image)):
            sum = self._get_layer_value_sum(layer, value)
            if sum < min_sum or layer == 0:
                min_layer = layer
                min_sum = sum

        return min_layer

    def get_checksum(self):
        layer = self._find_min_layer('0')
        ones = self._get_layer_value_sum(layer, '1')
        twos = self._get_layer_value_sum(layer, '2')
        return ones * twos


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
    PAGING MR. HERMAN! MR HERMAN!
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


if __name__ == "__main__":
    paging_mr_herman(IMAGEFILE, WIDTH, HEIGHT)
