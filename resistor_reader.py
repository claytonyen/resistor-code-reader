import tkinter as tk
from tkinter import ttk
import button_functions as bF
import dropdown_behavior as dB


root = tk.Tk()
root.option_add("*TCombobox*Listbox*Font", ("Arial", 11))
root.title("Resistor Color Code Reader")
root.geometry("600x700")

style = ttk.Style()
style.theme_use("default")
style.configure(
    "BigArrow.TCombobox",
    arrowsize=20,  # dropdown arrow size
    arrowcolor="black",  # dropdown arrow color
    background="#E1E1E1",  # bg shade of arrow block
    fieldbackground="#D3D3D3",  # bg color of text typing box
    font=("Arial", 11),  # text
)


## initialize color data for resistor bands ##
class bandColor:
    def __init__(self, hex_code, first_digit, second_digit, third_digit, multiplier, tolerance):
        self.hex_code = hex_code
        self.first_digit = first_digit
        self.second_digit = second_digit
        self.third_digit = third_digit
        self.multiplier = multiplier
        self.tolerance = tolerance

black_band = bandColor("#000000", 0, 0, 0, 1, None)
brown_band = bandColor("#8B4513", 1, 1, 1, 10, 1)
red_band = bandColor("#FF0000", 2, 2, 2, 100, 2)
orange_band = bandColor("#FFA500", 3, 3, 3, 1e3, 3)
yellow_band = bandColor("#FFFF00", 4, 4, 4, 1e4, 4)
green_band = bandColor("#008000", 5, 5, 5, 1e5, 0.5)
blue_band = bandColor("#0000FF", 6, 6, 6, 1e6, 0.25)
violet_band = bandColor("#A22AA2", 7, 7, 7, 1e7, 0.1)
gray_band = bandColor("#808080", 8, 8, 8, 1e8, 0.05)
white_band = bandColor("#FFFFFF", 9, 9, 9, 1e9, None)
gold_band = bandColor("#FFD700", None, None, None, 0.1, 5)
silver_band = bandColor("#C0C0C0", None, None, None, 0.01, 10)
default_band = bandColor("#D2B48C", None, None, None, None, None)

## canvas ##
canvas = tk.Canvas(root, width=600, height=700, bg="#D3D3D3")
canvas.pack()


## create visual resistor ##
# box for resistor
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
res_poly = canvas.create_polygon(res_points, fill="#D2B48C", outline="#000000", width=1, smooth=True)


## 4, 5, or 6 band resistor color code buttons ##
button_4_band = tk.Button(root, text="4 Band", bd=2, highlightthickness=2, highlightbackground="#000000")
button_4_band.place(x=50, y=625, width=150, height=50)
button_5_band = tk.Button(root, text="5 Band", bd=2, highlightthickness=2, highlightbackground="#000000")
button_5_band.place(x=225, y=625, width=150, height=50)
button_6_band = tk.Button(root, text="6 Band", bd=2, highlightthickness=2, highlightbackground="#000000")
button_6_band.place(x=400, y=625, width=150, height=50)


## reset button ##
reset_button = tk.Button(root, text="Reset",
    bd=2, bg="#FF3838",
    highlightthickness=2, highlightbackground="#000000",
    command=lambda: bF.reset_band_colors(button_1, button_2, button_3, button_4, button_5, button_6))
reset_button.place(x=500, y=287.5, width=62.5, height=25)


## change resistor body color ##
button_res_color = tk.Button(root, text="Change Resistor Color",
    bd=2, bg="#FFFFFF",
    highlightthickness=2, highlightbackground="#000000",
    command=lambda: bF.change_resistor_body_color(canvas, res_poly))
button_res_color.place(x=325, y=287.5, width=150, height=25)

## change resistor band colors ##
# initialize dropdown
dropdown = dB.EnhancedDropdown(root, options=[], style="BigArrow.TCombobox")

# process color selection from dropdown
dropdown.bind(
    "<<ComboboxSelected>>",
    lambda e: dB.handle_color_selection(e, dropdown, bF.state, update_button_color),
)
# process enter key
dropdown.bind(
    "<Return>",
    lambda e: dB.handle_color_selection(e, dropdown, bF.state, update_button_color),
)

# button locations
button_1 = tk.Button(root, text="1",
    bd=1, bg="#D2B48C",
    command=lambda: bF.on_band_click(button_1, "B1", dropdown),
)
button_1.place(x=100, y=76, width=37.5, height=149)

button_2 = tk.Button(root, text="2",
    bd=1, bg="#D2B48C",
    command=lambda: bF.on_band_click(button_2, "B2", dropdown),
)
button_2.place(x=175, y=98, width=37.5, height=105)

button_3 = tk.Button(root, text="3",
    bd=1, bg="#D2B48C",
    command=lambda: bF.on_band_click(button_3, "B3", dropdown),
)
button_3.place(x=225, y=101, width=37.5, height=99)

button_4 = tk.Button(root, text="4",
    bd=1, bg="#D2B48C",
    command=lambda: bF.on_band_click(button_4, "B4", dropdown),
)
button_4.place(x=275, y=101, width=37.5, height=99)

button_5 = tk.Button(root, text="T\nO\nL",
    bd=1, bg="#D2B48C",
    command=lambda: bF.on_band_click(button_5, "B5", dropdown),
)
button_5.place(x=387.5, y=98, width=37.5, height=105)

button_6 = tk.Button(
    root, text="T\nC\nR",
    bd=1, bg="#D2B48C",
    command=lambda: bF.on_band_click(button_6, "B6", dropdown),
)
button_6.place(x=462.5, y=76, width=37.5, height=149)

def update_button_color(band_id, color_name):
    # mapping band IDs and button variables
    button_mapping = {
        "B1": button_1,
        "B2": button_2,
        "B3": button_3,
        "B4": button_4,
        "B5": button_5,
        "B6": button_6,
    }

    # color string mapping to hex codes
    color_map = {
        "Black": black_band.hex_code,
        "Brown": brown_band.hex_code,
        "Red": red_band.hex_code,
        "Orange": orange_band.hex_code,
        "Yellow": yellow_band.hex_code,
        "Green": green_band.hex_code,
        "Blue": blue_band.hex_code,
        "Violet": violet_band.hex_code,
        "Gray": gray_band.hex_code,
        "White": white_band.hex_code,
        "Gold": gold_band.hex_code,
        "Silver": silver_band.hex_code,
    }

    # find the correct button and correct color
    target_button = button_mapping.get(band_id)
    target_color = color_map.get(color_name)

    if target_button:
        # update the background color of the button dynamically
        target_button.config(bg=target_color)

        # adjust text color for readability against dark backgrounds
        if color_name in ("Black", "Blue", "Brown", "Red"):
            target_button.config(fg="white")
        else:
            target_button.config(fg="black")


root.mainloop()