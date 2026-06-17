import tkinter as tk

def change_band_color(button):
    button.config(bg="red")

def reset_band_colors(b1, b2, b3, b4, b5, b6):
    b1.config(bg="#D2B48C")
    b2.config(bg="#D2B48C")
    b3.config(bg="#D2B48C")
    b4.config(bg="#D2B48C")
    b5.config(bg="#D2B48C")
    b6.config(bg="#D2B48C")

def disable_button(button):
    button.config(state=tk.DISABLED)