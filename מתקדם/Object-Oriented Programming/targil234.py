
class Pixel:

    def __init__(self, x = 0, y = 0, red = 0, green = 0, blue = 0):
        self._x = x
        self._y = y
        self._red = red
        self._green = green
        self._blue = blue


    def set_coords(self, x, y):
        self._x = x
        self._y = y

    def set_grayscale(self):
        avg = (self._red + self._green + self._blue) / 3
        self._red = self._green = self._blue = avg

    def print_pixel_info(self):
        prime_color = ""
        if self._red == 0 and self._green == 0 and self._blue > 50:
            prime_color = "Blue"
        elif self._red == 0 and self._green > 50 and self._blue == 0:
            prime_color = "Green"
        elif self._red > 50 and self._green == 0 and self._blue == 0:
            prime_color = "Red"
        print("X: {}, Y: {}, Color: ({},{},{}) {}".format(self._x, self._y, self._red, self._green, self._blue, prime_color))


def main():
    p = Pixel(5, 6, 250)
    p.print_pixel_info()
    p.set_grayscale()
    p.print_pixel_info()





if __name__ == "__main__":
    main()