import tkinter as tk
from buttonFunctions import *

root = tk.Tk()
root.title("Resistor Color Code Reader")
root.geometry("600x700")

## initialize color data for resistor bands ##
class bandColor:
    def __init__(self, color, hex_code, first_digit, second_digit, third_digit, multiplier, tolerance):
        self.color = color
        self.hex_code = hex_code
        self.first_digit = first_digit
        self.second_digit = second_digit
        self.third_digit = third_digit
        self.multiplier = multiplier
        self.tolerance = tolerance

black = bandColor("black", "#000000", 0, 0, 0, 1, None)
brown = bandColor("brown", "#8B4513", 1, 1, 1, 10, 1)
red = bandColor("red", "#FF0000", 2, 2, 2, 100, 2)
orange = bandColor("orange", "#FFA500", 3, 3, 3, 1e3, 3)
yellow = bandColor("yellow", "#FFFF00", 4, 4, 4, 1e4, 4)
green = bandColor("green", "#008000", 5, 5, 5, 1e5, 0.5)
blue = bandColor("blue", "#0000FF", 6, 6, 6, 1e6, 0.25)
violet = bandColor("violet", "#EE82EE", 7, 7, 7, 1e7, 0.1)
gray = bandColor("gray", "#808080", 8, 8, 8, 1e8, 0.05)
white = bandColor("white", "#FFFFFF", 9, 9, 9, 1e9, None)
gold = bandColor("gold", "#FFD700", None, None, None, 0.1, 5)
silver = bandColor("silver", "#C0C0C0", None, None, None, 0.01, 10)


## canvas ##
canvas = tk.Canvas(root, width=600, height=700, bg="#D3D3D3")
canvas.pack()


## create visual resistor ##
# box for res
canvas.create_rectangle(25, 25, 575, 275, fill="#f0f0f0", outline="#000000", width=2)

# resistor body
res_points = [175, 100, 
              425, 100, 
              450, 75, 
              525, 75, 
              550, 150, 
              525, 225, 
              450, 225, 
              425, 200,
              175, 200,
              150, 225,
              75, 225,
              50, 150,
              75, 75,
              150, 75]
canvas.create_polygon(res_points, fill="#D2B48C", outline="#000000", width=1, smooth=True)

## 4, 5, or 6 band resistor color codes ##
button_4_band = tk.Button(root, text="4 Band", bd=2, highlightthickness=2, highlightbackground="#000000")
button_4_band.place(x=50, y=300, width=150, height=50)
button_5_band = tk.Button(root, text="5 Band", bd=2, highlightthickness=2, highlightbackground="#000000")
button_5_band.place(x=225, y=300, width=150, height=50)
button_6_band = tk.Button(root, text="6 Band", bd=2, highlightthickness=2, highlightbackground="#000000")
button_6_band.place(x=400, y=300, width=150, height=50)


## color band buttons ##
b1_color = "#D2B48C"
b2_color = "#D2B48C"
b3_color = "#D2B48C"
b4_color = "#D2B48C"
b5_color = "#D2B48C"

button_1 = tk.Button(root, text="B1", bd=1, bg=b1_color, command=lambda: change_band_color(button_1))
button_1.place(x=100, y=76, width=37.5, height=149)
button_3 = tk.Button(root, text="B3", bd=1, bg=b3_color)
button_3.place(x=225, y=101, width=37.5, height=99)
button_4 = tk.Button(root, text="B4", bd=1, bg=b4_color)
button_4.place(x=275, y=101, width=37.5, height=99)
button_6 = tk.Button(root, text="B6", bd=1, bg=b5_color)
button_6.place(x=462.5, y=76, width=37.5, height=149)
button_2 = tk.Button(root, text="B2", bd=1, bg=b2_color)
button_2.place(x=175, y=98, width=37.5, height=105)
button_5 = tk.Button(root, text="B5", bd=1, bg=b5_color)
button_5.place(x=387.5, y=98, width=37.5, height=105)

root.mainloop()