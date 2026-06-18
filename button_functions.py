import tkinter as tk
from tkinter import ttk
from tkinter import colorchooser
from tkinter import messagebox

## variables ##
chosen_color = ((210, 180, 140), '#D2B48C')
default_color_array = ((0, 0, 0), (139, 69, 19), (255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 128, 0), (0, 0, 255), (238, 130, 238), (128, 128, 128), (255, 255, 255), (255, 215, 0), (192, 192, 192))

## button functions ##
def reset_band_colors(b1, b2, b3, b4, b5, b6):
    b1.config(bg=chosen_color[1])
    b2.config(bg=chosen_color[1])
    b3.config(bg=chosen_color[1])
    b4.config(bg=chosen_color[1])
    b5.config(bg=chosen_color[1])
    b6.config(bg=chosen_color[1])

def change_resistor_body_color(canvas, res_body):
    global chosen_color
    new_color = tk.colorchooser.askcolor(title="Choose Resistor Color")

    if new_color[1] is None:
        return
    
    temp_old = chosen_color
    chosen_color = new_color

    if chosen_color[0] in default_color_array:
        messagebox.showerror("Invalid Option", "Please select a different color for the resistor body.")
        chosen_color = temp_old
    else:
        canvas.itemconfig(res_body, fill=chosen_color[1])

def disable_button(button):
    button.config(state=tk.DISABLED)

# for band color selection
def get_colors_for_band(band_id):
    digit_colors = [
        "Black",
        "Brown",
        "Red",
        "Orange",
        "Yellow",
        "Green",
        "Blue",
        "Violet",
        "Gray",
        "White",
    ]

    multiplier_colors = [
        "Black",
        "Brown",
        "Red",
        "Orange",
        "Yellow",
        "Green",
        "Blue",
        "Violet",
        "Gray",
        "White",
        "Gold",
        "Silver",
    ]

    tolerance_colors = [
        "Brown",
        "Red",
        "Orange",
        "Yellow",
        "Green",
        "Blue",
        "Violet",
        "Gray",
        "Gold",
        "Silver",
    ]

    temp_colors = [
        "Black", 
        "Brown", 
        "Red", 
        "Orange", 
        "Yellow", 
        "Green", 
        "Blue", 
        "Violet", 
        "Gray"]

    # return appropriate list based on band ID
    if band_id in ("B1", "B2", "B3"):
        return digit_colors
    elif band_id == "B4":
        return multiplier_colors
    elif band_id == "B5":
        return tolerance_colors
    elif band_id == "B6":
        return temp_colors
    else:
        return digit_colors

state = {"active_band": None}

def on_band_click(clicked_button, band_id, dropdown):
    # update application states
    state["active_band"] = band_id

    # update underlying search list properties matching selected target band
    available_options = get_colors_for_band(band_id)
    dropdown.all_options = available_options
    dropdown["values"] = available_options
    dropdown.set("")

    # pull geometry properties from button layout
    x_pos = clicked_button.winfo_x()
    y_pos = clicked_button.winfo_y()
    btn_height = clicked_button.winfo_height()
    btn_width = clicked_button.winfo_width()

    # put dropdown frame below button edge
    dropdown.place(x=x_pos, y=y_pos + btn_height + 3, width=btn_width + 25)
    dropdown.focus_set()