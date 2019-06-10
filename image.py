from PIL import Image

ASCII_STRING = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"


class JPG:
    def __init__(self, path):
        img = Image.open("./dataset/" + path + ".jpg")  # converts image to 8-bit greyscale
        img.thumbnail((70, 70))
        data = list(img.getdata())  # convert image data to a list of integers
        # create a list of lists with pixel rows
        self.pixels = [data[offset: offset + img.width] for offset in range(0, len(data), img.width)]

        self.intensity_matrix = None
        self.converted_matrix = None

    def __str__(self):
        ret = ''
        for row in self.converted_matrix:
            ret += ''.join(value + value + value for value in row) + "\n"
        return ret

    def get_intensity_matrix(self):
        intensity_matrix = []
        for row in self.pixels:
            intensity_row = []
            for p in row:
                intensity = (p[0] + p[1] + p[2] / 3.0)
                intensity_row.append(intensity)

            intensity_matrix.append(intensity_row)

        self.intensity_matrix = intensity_matrix

    def normalize(self):
        normalized_intensity_matrix = []
        max_pixel = max(map(max, self.intensity_matrix))
        min_pixel = min(map(min, self.intensity_matrix))
        for row in self.intensity_matrix:
            rescaled_row = []
            for pixel in row:
                rescaled_row.append(255 * (pixel - min_pixel) / float(max_pixel - min_pixel))
            normalized_intensity_matrix.append(rescaled_row)

        self.intensity_matrix = normalized_intensity_matrix

    def convert_to_ascii(self):
        self.get_intensity_matrix()
        self.normalize()

        ascii_matrix = []
        for row in self.intensity_matrix:
            ascii_row = []
            for pixel in row:
                ascii_row.append(ASCII_STRING[int(pixel / 255 * len(ASCII_STRING)) - 1])
            ascii_matrix.append(ascii_row)

        self.converted_matrix = ascii_matrix

