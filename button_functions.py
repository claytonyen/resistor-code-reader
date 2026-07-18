import tkinter as tk
from tkinter import ttk
from tkinter import colorchooser
from tkinter import messagebox


## variables ##
chosen_color = ((210, 180, 140), '#D2B48C')
band_color_array = ((0, 0, 0), 
                    (139, 69, 19), 
                    (255, 0, 0), 
                    (255, 136, 0), 
                    (255, 255, 0), 
                    (0, 128, 0), 
                    (0, 0, 255), 
                    (238, 130, 238), 
                    (128, 128, 128), 
                    (255, 255, 255), 
                    (239, 191, 4), 
                    (192, 192, 192))

## button functions ##

# changes all band colors to resistor body color
def bg_lum(rgb):
    relative_luminance = (.3*rgb[0] + .587*rgb[1] + .114*rgb[2])/255 # calculate relative luminance, normalize to 0-1
    if relative_luminance < 0.47:    # threshold for dark bgs
        return True
    return False

def reset_band_colors(b1, b2, b3, b4, b5, b6):
    b1.config(bg=chosen_color[1])
    b2.config(bg=chosen_color[1])
    b3.config(bg=chosen_color[1])
    b4.config(bg=chosen_color[1])
    b5.config(bg=chosen_color[1])
    b6.config(bg=chosen_color[1])

# color dropdown, changes resistor body color
def change_resistor_body_color(canvas, res_body, button_3, button_6):
    global chosen_color
    new_color = tk.colorchooser.askcolor(title="Choose Resistor Color")

    if new_color[1] is None:
        return
    
    temp_old = chosen_color
    chosen_color = new_color

    if chosen_color[0] in band_color_array:
        messagebox.showerror("Invalid Option", "Please select a different color for the resistor body.")
        chosen_color = temp_old
    else:
        canvas.itemconfig(res_body, fill=chosen_color[1])
        if button_3["state"] == tk.DISABLED:
            button_3.config(bg=chosen_color[1])
        if button_6["state"] == tk.DISABLED:
            button_6.config(bg=chosen_color[1])

# disables a button
curr_band_num = 6

def disable_button(clicked_button, button_less, button_more, new_band_num, 
                   button_3, button_4, button_6,
                   digit3_LF, mult_LF, tcr_LF,
                   label_LF3, label_LF6):
    global curr_band_num
    old_band_num = curr_band_num
    curr_band_num = new_band_num
    
    clicked_button.config(state=tk.DISABLED, relief=tk.SUNKEN)
    button_less.config(state=tk.NORMAL, relief=tk.RAISED, fg="black")
    button_more.config(state=tk.NORMAL, relief=tk.RAISED, fg="black")

    if curr_band_num == 6:
        button_3.config(state=tk.NORMAL, relief=tk.RAISED)
        button_6.config(state=tk.NORMAL, relief=tk.RAISED)
        button_4.place(x=275, y=176, width=37.5, height=99)
        tcr_LF.place(x=472.5, y=325, width=77.5, height=50)
        mult_LF.place(x=297.5, y=325, width=67.5, height=50)
        digit3_LF.place(x=215, y=325, width=62.5, height=50)
        label_LF6.config(text="ppm/\u00b0C")
        if old_band_num == 4:
            label_LF3.config(text="")
    elif curr_band_num == 5:
        button_3.config(state=tk.NORMAL, relief=tk.RAISED)
        button_6.config(state=tk.DISABLED, relief=tk.FLAT, bg=chosen_color[1])
        button_4.place(x=275, y=176, width=37.5, height=99)
        tcr_LF.place_forget()
        mult_LF.place(x=297.5, y=325, width=67.5, height=50)
        digit3_LF.place(x=215, y=325, width=62.5, height=50)
        if old_band_num == 4:
            label_LF3.config(text="")
    else:
        button_3.config(state=tk.DISABLED, relief=tk.FLAT, bg=chosen_color[1])
        button_6.config(state=tk.DISABLED, relief=tk.FLAT, bg=chosen_color[1])
        button_4.place(x=225, y=176, width=37.5, height=99)
        tcr_LF.place_forget()
        digit3_LF.place_forget()
        mult_LF.place(x=215, y=325, width=62.5, height=50)

BAND_HEX = {
    "Black": "#000000", "Brown": "#8B4513", "Red": "#FF0000", "Orange": "#FF8800",
    "Yellow": "#FFFF00", "Green": "#008000", "Blue": "#0000FF", "Violet": "#A22AA2",
    "Gray": "#808080", "White": "#FFFFFF", "Gold": "#EFBF04", "Silver": "#C0C0C0",
}

BAND_RGB = {
    "Black": (0, 0, 0), "Brown": (139, 69, 19), "Red": (255, 0, 0), "Orange": (255, 136, 0),
    "Yellow": (255, 255, 0), "Green": (0, 128, 0), "Blue": (0, 0, 255), "Violet": (238, 130, 238),
    "Gray": (128, 128, 128), "White": (255, 255, 255), "Gold": (239, 191, 4), "Silver": (192, 192, 192),
}

DIGIT_LABELS = {
    "Black": "    0", "Brown": "    1", "Red": "    2",
    "Orange": "    3", "Yellow": "    4", "Green": "    5",
    "Blue": "    6", "Violet": "    7", "Gray": "    8",
    "White": "    9",
}

MULTIPLIER_LABELS = {
    "Black": " 1", "Brown": " 10", "Red": " 10²",
    "Orange": " 10³", "Yellow": " 10⁴", "Green": " 10⁵",
    "Blue": " 10⁶", "Violet": " 10⁷", "Gray": " 10⁸",
    "White": " 10⁹", "Gold": " 0.1", "Silver": "0.01",
}

TOLERANCE_LABELS = {
    "Brown": "   1%", "Red": "   2%", "Orange": "   3%", "Yellow": "   4%",
    "Green": " 0.5%", "Blue": "0.25%", "Violet": " 0.1%", "Gray": "0.05%",
    "Gold": "   5%", "Silver": "  10%",
}

TEMPCOEFF_LABELS = {
    "Black": "  250", "Brown": "  100", "Red": "   50",
    "Orange": "   15", "Yellow": "   25", "Green": "   20",
    "Blue": "   10", "Violet": "    5", "Gray": "    1",
}

def _value_label(band_id, color_name):
    if band_id in ("B1", "B2", "B3"):
        return DIGIT_LABELS.get(color_name, "")
    elif band_id == "B4":
        return MULTIPLIER_LABELS.get(color_name, "")
    elif band_id == "B5":
        return TOLERANCE_LABELS.get(color_name, "")
    elif band_id == "B6":
        return TEMPCOEFF_LABELS.get(color_name, "")
    return ""

def format_band_option(band_id, color_name):
    # pad the color name so the value lines up in a loose second "column"
    return f"{color_name.ljust(8)}{_value_label(band_id, color_name)}"

def get_dropdown_data(band_id):
    color_names = get_colors_for_band(band_id)
    display_strings = []
    display_to_name = {}
    color_pairs = []

    for color_name in color_names:
        display_text = format_band_option(band_id, color_name)
        display_strings.append(display_text)
        display_to_name[display_text] = color_name

        bg_hex = BAND_HEX.get(color_name, "#FFFFFF")
        rgb = BAND_RGB.get(color_name, (255, 255, 255))
        fg_hex = "#FFFFFF" if bg_lum(rgb) else "#000000"
        color_pairs.append((bg_hex, fg_hex))

    return display_strings, display_to_name, color_pairs

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
    
    if state["active_band"] == band_id and dropdown.winfo_viewable():
        dropdown.place_forget()
        state["active_band"] = None
        return

    # update application states
    state["active_band"] = band_id

    # update search list properties matching selected band
    display_strings, display_to_name, color_pairs = get_dropdown_data(band_id)
    dropdown.all_options = display_strings
    dropdown.display_to_name = display_to_name
    dropdown["values"] = display_strings
    dropdown.set("")
    dropdown.set_option_colors(color_pairs)

    # pull geometry properties from button layout
    x_pos = clicked_button.winfo_x()
    y_pos = clicked_button.winfo_y()
    btn_height = clicked_button.winfo_height()
    btn_width = clicked_button.winfo_width()

    dropdown_width = max(btn_width + 37.5, 145)

    # keep the dropdown from rendering past the window's right edge
    window_width = clicked_button.winfo_toplevel().winfo_width()
    if x_pos + dropdown_width > window_width:
        x_pos = window_width - dropdown_width - 5
    x_pos = max(x_pos, 0)

    # put dropdown frame below button edge
    dropdown.place(x=x_pos, y=y_pos + btn_height + 3, height=37.5, width=dropdown_width)
    dropdown.focus_set()