import tkinter as tk
from tkinter import colorchooser

## variables ##
chosen_color = ((210, 180, 140), "#D2B48C")

def change_band_color(button):
    button.config(bg="red")

def reset_band_colors(b1, b2, b3, b4, b5, b6):
    b1.config(bg=chosen_color[1])
    b2.config(bg=chosen_color[1])
    b3.config(bg=chosen_color[1])
    b4.config(bg=chosen_color[1])
    b5.config(bg=chosen_color[1])
    b6.config(bg=chosen_color[1])

def change_resistor_color(canvas, res_body):
    global chosen_color
    chosen_color = tk.colorchooser.askcolor(title="Choose Resistor Color")
    print(chosen_color)
    canvas.itemconfig(res_body, fill=chosen_color[1])

def disable_button(button):
    button.config(state=tk.DISABLED)