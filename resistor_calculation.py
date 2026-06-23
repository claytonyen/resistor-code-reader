import button_functions as bF
import tkinter as tk

## initialize color data for resistor bands ##
class bandColor:
    def __init__(self, hex_code, first_digit, second_digit, third_digit, multiplier, tolerance, tempcoeff, power):
        self.hex_code = hex_code
        self.first_digit = first_digit
        self.second_digit = second_digit
        self.third_digit = third_digit
        self.multiplier = multiplier
        self.tolerance = tolerance
        self.tempcoeff = tempcoeff
        self.power = power

black_band = bandColor("#000000", 0, 0, 0, 1, None, 250, 0)
brown_band = bandColor("#8B4513", 1, 1, 1, 10, 1, 100, 1)
red_band = bandColor("#FF0000", 2, 2, 2, 1e2, 2, 50, 2)
orange_band = bandColor("#FF8800", 3, 3, 3, 1e3, 3, 15, 3)
yellow_band = bandColor("#FFFF00", 4, 4, 4, 1e4, 4, 25, 4)
green_band = bandColor("#008000", 5, 5, 5, 1e5, 0.5, 20, 5)
blue_band = bandColor("#0000FF", 6, 6, 6, 1e6, 0.25, 10, 6)
violet_band = bandColor("#A22AA2", 7, 7, 7, 1e7, 0.1, 5, 7)
gray_band = bandColor("#808080", 8, 8, 8, 1e8, 0.05, 1, 8)
white_band = bandColor("#FFFFFF", 9, 9, 9, 1e9, None, None, 9)
gold_band = bandColor("#EFBF04", None, None, None, 0.1, 5, None, -1)
silver_band = bandColor("#C0C0C0", None, None, None, 0.01, 10, None, -2)
