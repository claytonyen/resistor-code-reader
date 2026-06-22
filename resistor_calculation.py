import button_functions as bF

## initialize color data for resistor bands ##
class bandColor:
    def __init__(self, rgb, hex_code, first_digit, second_digit, third_digit, multiplier, tolerance):
        self.rgb = rgb
        self.hex_code = hex_code
        self.first_digit = first_digit
        self.second_digit = second_digit
        self.third_digit = third_digit
        self.multiplier = multiplier
        self.tolerance = tolerance

black_band = bandColor((0, 0, 0), "#000000", 0, 0, 0, 1, None)
brown_band = bandColor((139, 69, 19), "#8B4513", 1, 1, 1, 10, 1)
red_band = bandColor((255, 0, 0), "#FF0000", 2, 2, 2, 100, 2)
orange_band = bandColor((255, 136, 0), "#FF8800", 3, 3, 3, 1e3, 3)
yellow_band = bandColor((255, 255, 0), "#FFFF00", 4, 4, 4, 1e4, 4)
green_band = bandColor((0, 128, 0), "#008000", 5, 5, 5, 1e5, 0.5)
blue_band = bandColor((0, 0, 255), "#0000FF", 6, 6, 6, 1e6, 0.25)
violet_band = bandColor((238, 130, 238), "#A22AA2", 7, 7, 7, 1e7, 0.1)
gray_band = bandColor((128, 128, 128), "#808080", 8, 8, 8, 1e8, 0.05)
white_band = bandColor((255, 255, 255), "#FFFFFF", 9, 9, 9, 1e9, None)
gold_band = bandColor((239, 191, 4), "#EFBF04", None, None, None, 0.1, 5)
silver_band = bandColor((192, 192, 192), "#C0C0C0", None, None, None, 0.01, 10)
default_band = bandColor((210,180,140), "#D2B48C",None, None, None, None, None)

