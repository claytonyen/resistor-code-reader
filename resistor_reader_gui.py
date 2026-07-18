import tkinter as tk
import math
from tkinter import ttk
from tkinter import messagebox
import button_functions as bF
import band_dropdown_behavior as dB

## initialize window ##
root = tk.Tk()
root.option_add("*TCombobox*Listbox*Font", ("Arial", 14))
root.title("Resistor Color Code Reader")
root.geometry("600x600")
root.resizable(False, False)

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


## variables
b1_val = None
b2_val = None
b3_val = None
b4_val = None
b5_val = None
b6_val = None


## canvas ##
canvas = tk.Canvas(root, width=600, height=600, bg="#D3D3D3")
canvas.pack()


## create visual resistor ##
# box for resistor
canvas.create_rectangle(25, 100, 575, 400, fill="#f0f0f0", outline="#000000", width=2)

# resistor body
res_points = [175, 175, 
              425, 175, 
              450, 150, 
              525, 150, 
              550, 225, 
              525, 300, 
              450, 300, 
              425, 275,
              175, 275,
              150, 300,
              75, 300,
              50, 225,
              75, 150,
              150, 150]
res_poly = canvas.create_polygon(res_points, fill="#D2B48C", outline="#000000", width=1, smooth=True)


## 4, 5, or 6 band resistor color code buttons ##
button_4_band = tk.Button(root, text="4  Band", bd=2, font=("Arial", 18),
                          highlightthickness=2, highlightbackground="#000000",
                          activebackground="#D3D3D3",
                          command=lambda: band_change(button_4_band, button_5_band, button_6_band, 4, 
                                                      button_3, button_4, button_6,
                                                      digit3_LF, mult_LF, tcr_LF,
                                                      label_LF3, label_LF6))
button_4_band.place(x=25, y=25, width=150, height=50)
button_5_band = tk.Button(root, text="5  Band", bd=2, font=("Arial", 18),
                          highlightthickness=2, highlightbackground="#000000",
                          activebackground="#D3D3D3",
                          command=lambda: band_change(button_4_band, button_5_band, button_6_band, 5, 
                                                      button_3, button_4, button_6,
                                                      digit3_LF, mult_LF, tcr_LF,
                                                      label_LF3, label_LF6))
button_5_band.place(x=225, y=25, width=150, height=50)
button_6_band = tk.Button(root, text="6  Band", bd=2, font=("Arial", 18),
                          highlightthickness=2, highlightbackground="#000000", 
                          activebackground="#D3D3D3",
                          command=lambda: band_change(button_4_band, button_5_band, button_6_band, 6, 
                                                      button_3, button_4, button_6,
                                                      digit3_LF, mult_LF, tcr_LF,
                                                      label_LF3, label_LF6))
button_6_band.place(x=425, y=25, width=150, height=50)
button_6_band.config(state=tk.DISABLED, relief=tk.SUNKEN)  # start with 6 band disabled

old_bnum = 6

def band_change(button_4_band, button_5_band, button_6_band, new_bnum,
                button_3, button_4, button_6,
                digit3_LF, mult_LF, tcr_LF,
                label_LF3, label_LF6):
    
    global old_bnum
    global b3_val
    global b4_val
    global b5_val
    global b6_val

    if new_bnum == 4:
        bF.disable_button(button_4_band, button_5_band, button_6_band, 4,
                          button_3, button_4, button_6,
                          digit3_LF, mult_LF, tcr_LF,
                          label_LF3, label_LF6)
        b5_val = None
        b6_val = None
        old_bnum = 4
    elif new_bnum == 5:
        bF.disable_button(button_5_band, button_4_band, button_6_band, 5,
                          button_3, button_4, button_6,
                          digit3_LF, mult_LF, tcr_LF,
                          label_LF3, label_LF6)
        
        if old_bnum == 4:
            b3_val = None
        else:
            b6_val = None

        old_bnum = 5
    else:
        bF.disable_button(button_6_band, button_4_band, button_5_band, 6,
                          button_3, button_4, button_6,
                          digit3_LF, mult_LF, tcr_LF,
                          label_LF3, label_LF6)
        
        if old_bnum == 4:
            b3_val = None

        old_bnum = 5
        
    calculate_resistance()

## reset button ##
def clear_res(button_1, button_2, button_3, button_4, button_5, button_6):
    bF.reset_band_colors(button_1, button_2, button_3, button_4, button_5, button_6)
    final_display_entry.delete(0, tk.END)

    global b1_val
    global b2_val
    global b3_val
    global b4_val
    global b5_val
    global b6_val

    b1_val = None
    b2_val = None
    b3_val = None
    b4_val = None
    b5_val = None
    b6_val = None

    label_LF1.config(text="")
    label_LF2.config(text="")
    label_LF3.config(text="")
    label_LF4.config(text="")
    label_LF5.config(text="%")
    label_LF6.config(text="ppm/\u00b0C")

reset_button = tk.Button(root, text="Reset", 
    bd=2, bg="#FE4F4F", font=("Arial", 12),
    highlightthickness=2, highlightbackground="#000000",
    command=lambda: clear_res(button_1, button_2, button_3, button_4, button_5, button_6))
reset_button.place(x=337.5, y=112.5, width=75, height=25)

## change resistor body color ##
button_res_color = tk.Button(root, text="Change Body Color",
    bd=2, bg="#FFFFFF", font=("Arial", 10),
    highlightthickness=2, highlightbackground="#000000", compound=tk.CENTER,
    command=lambda: bF.change_resistor_body_color(canvas, res_poly, button_3, button_6))
button_res_color.place(x=187.5, y=112.5, width=125, height=25)

## display numerical values ##
digit1_LF = tk.LabelFrame(root, text="1st Digit:", font=("Arial", 8), labelanchor="n")
digit1_LF.place(x=50, y=325, width=62.5, height=50)
label_LF1 = tk.Label(digit1_LF, text="", font=("Arial", 13), justify="center")
label_LF1.pack()
digit2_LF = tk.LabelFrame(root, text="2nd Digit:", font=("Arial", 8), labelanchor="n")
digit2_LF.place(x=132.5, y=325, width=62.5, height=50)
label_LF2 = tk.Label(digit2_LF, text="", font=("Arial", 13), justify="center")
label_LF2.pack()
digit3_LF = tk.LabelFrame(root, text="3rd Digit:", font=("Arial", 8), labelanchor="n")
digit3_LF.place(x=215, y=325, width=62.5, height=50)
label_LF3 = tk.Label(digit3_LF, text="", font=("Arial", 13), justify="center")
label_LF3.pack()
mult_LF = tk.LabelFrame(root, text="Multiplier:", font=("Arial", 8), labelanchor="n")
mult_LF.place(x=297.5, y=325, width=67.5, height=50)
label_LF4 = tk.Label(mult_LF, text="", font=("Arial", 13), justify="center")
label_LF4.pack()
tol_LF = tk.LabelFrame(root, text="Tolerance:", font=("Arial", 8), labelanchor="n")
tol_LF.place(x=385, y=325, width=67.5, height=50)
label_LF5 = tk.Label(tol_LF, text="%", font=("Arial", 13), justify="center")
label_LF5.pack()
tcr_LF = tk.LabelFrame(root, text="Temp. Coeff:", font=("Arial", 8), labelanchor="n")
tcr_LF.place(x=472.5, y=325, width=77.5, height=50)
label_LF6 = tk.Label(tcr_LF, text="ppm/\u00b0C", font=("Arial", 10), justify="center")
label_LF6.pack()

# button locations
button_1 = tk.Button(root, bd=1, bg="#D2B48C",
    command=lambda: bF.on_band_click(button_1, "B1", dropdown),
)
button_1.place(x=100, y=153, width=37.5, height=145)

button_2 = tk.Button(root, bd=1, bg="#D2B48C",
    command=lambda: bF.on_band_click(button_2, "B2", dropdown),
)
button_2.place(x=175, y=173, width=37.5, height=105)

button_3 = tk.Button(root, bd=1, bg="#D2B48C",
    command=lambda: bF.on_band_click(button_3, "B3", dropdown),
)
button_3.place(x=225, y=176, width=37.5, height=99)

button_4 = tk.Button(root, bd=1, bg="#D2B48C",
    command=lambda: bF.on_band_click(button_4, "B4", dropdown),
)
button_4.place(x=275, y=176, width=37.5, height=99)

button_5 = tk.Button(root, bd=1, bg="#D2B48C",
    command=lambda: bF.on_band_click(button_5, "B5", dropdown),
)
button_5.place(x=387.5, y=173, width=37.5, height=105)

button_6 = tk.Button(root, bd=1, bg="#D2B48C",
    command=lambda: bF.on_band_click(button_6, "B6", dropdown),
)
button_6.place(x=462.5, y=153, width=37.5, height=145)


## change resistor band colors ##
# initialize dropdown
dropdown = dB.EnhancedDropdown(root, options=[], style="BigArrow.TCombobox")
band_pressed = False

# process color selection from dropdown
dropdown.bind(
    "<<ComboboxSelected>>",
    lambda e: dB.handle_color_selection(e, dropdown, bF.state, update_button_color))
# process enter key
dropdown.bind(
    "<Return>",
    lambda e: dB.handle_color_selection(e, dropdown, bF.state, update_button_color))

# button calculation
def validate_input(proposed_text)->bool:
    allowed_chars = ".0123456789rRkKmMgG\u03a9"
    max_limit = 15

    if proposed_text == "":
        return True
        
    return len(proposed_text) <= max_limit and all(char in allowed_chars for char in proposed_text)

def is_float(text)->bool:
    try:
        float(text)
        return True
    except ValueError:
        return False

def check_letter(float_num)->str:
    if 0.1 <= float_num < 1e3:
        return "R"
    elif 1e3 <= float_num < 1e6:
        return "K"
    elif 1e6 <= float_num < 1e9:
        return "M"
    else:
        return "G"
    
def get_confirmed_mult(letter)->float:
    mult_map = {
        "R": 1,
        "K": 1e3,
        "M": 1e6,
        "G": 1e9
    }

    try:
        return float(mult_map.get(letter, 1.0))
    except (TypeError, ValueError):
        return 1.0
    
def get_col(num)->str:
    num_to_col_map = {
        0: "Black",
        1: "Brown",
        2: "Red",
        3: "Orange",
        4: "Yellow",
        5: "Green",
        6: "Blue",
        7: "Violet",
        8: "Gray",
        9: "White"
    }

    try:
        return str(num_to_col_map.get(num))
    except (TypeError, ValueError):
        return "Black"

def get_mult_color(num)->str:
    map = {
        0: "Black",
        1: "Brown",
        2: "Red",
        3: "Orange",
        4: "Yellow",
        5: "Green",
        6: "Blue",
        7: "Violet",
        8: "Gray",
        9: "White",
        -1: "Gold",
        -2: "Silver"
    }

    try:
        return str(map.get(num))
    except (TypeError, ValueError):
        return "Black"

def round_dig(digit, rounder)->int:
    if rounder >= 5:
        digit += 1
    return digit

def process_entry(entry):
    letter_targets = ("R", "K", "M", "G")

    et = entry.get()
    et = et.upper()
    et = et.replace("\u03a9", "")
    
    if not et:
        return

    if et.count('.') > 1:
        et = ""
        final_display_entry.delete(0, tk.END)
        messagebox.showerror("Invalid Value", "Too Many Decimal Points!")
        return
    
    if et.count('K') + et.count('G') + et.count('M') + et.count('R') > 1:
        et = ""
        final_display_entry.delete(0, tk.END)
        messagebox.showerror("Invalid Value", "Too Many Multipliers!")
        return

    # rid of leading zeros
    et = et.lstrip('0')
    if et and et[0] == ".":
        et = "0" + et

    index = -1
    letter = "R"

    if not is_float(et):
        if not et.endswith(letter_targets):
            index, letter = next(((i, char) for i, char in enumerate(et) if char in letter_targets), (None, None))
            et = et.replace(letter, '.')
        else:
            index = len(et) - 1
            letter = et[index]
            et = et[:-1]
        
        if et.count('.') > 1:
            et = ""
            final_display_entry.delete(0, tk.END)
            messagebox.showerror("Invalid Value", "Decimal and Multiplier\nPlacement Error")
            return
        
        et_float = float(et) * get_confirmed_mult(letter)
    else:
        et_float = float(et)

    if et_float > 999e9 or et_float < 0.1:
        et = ""
        final_display_entry.delete(0, tk.END)
        messagebox.showerror("Invalid Value", "Range Error")
        return

    letter = check_letter(et_float)
    reduced_et_string = str(int(1000 * float(et_float) / get_confirmed_mult(letter)))

    actual_ohms = et_float

    sig1: int = 0
    sig2: int = 0
    sig3: int = 0
    rounder: int = 0

    if bF.curr_band_num == 4:
        if et_float > 99e9:
            et = ""
            final_display_entry.delete(0, tk.END)
            messagebox.showerror("Invalid Value", "Range Error\nTry on 5 Band")
            return
        
        sig1 = int(reduced_et_string[0])
        sig2 = int(reduced_et_string[1])
        rounder = int(reduced_et_string[2])
        sig2 = round_dig(sig2, rounder)
        
        if sig2 == 10:
            sig2 = 0
            sig1 += 1
            if sig1 == 10:
                reduced_et_string = f"{sig1}"
            else:
                reduced_et_string = f"{sig1}{sig2}"
        else: 
            reduced_et_string = f"{sig1}{sig2}"

        et_float = float(reduced_et_string) * get_confirmed_mult(letter) / 1000
        if et_float > 99e9:
            et_float = 99e9
            reduced_et_string = "99"

        if et_float.is_integer and et_float >= 10:
            degree = str(int(et_float))[2:]
            mult = degree.count('0')
        elif 1 < et_float < 10:
            mult = -1
        elif et_float < 1:
            mult = -2
        
    else:
        if et_float < 1:
            et = ""
            final_display_entry.delete(0, tk.END)
            messagebox.showerror("Invalid Value", "Range Error\nTry on 4 Band")
            return
        
        sig1 = int(reduced_et_string[0])
        sig2 = int(reduced_et_string[1])
        sig3 = int(reduced_et_string[2])
        rounder = int(reduced_et_string[3])
        sig3 = round_dig(sig3, rounder)
        
        if sig3 == 10:
            sig3 = 0
            sig2 += 1

            if sig2 == 10:
                sig2 = 0
                sig1 += 1

                if sig1 == 10:
                    reduced_et_string = f"{sig1}{sig2}"
                else:
                    reduced_et_string = f"{sig1}{sig2}{sig3}"
            else:
                reduced_et_string = f"{sig1}{sig2}{sig3}"
        else:
            reduced_et_string = f"{sig1}{sig2}{sig3}"

        et_float = float(reduced_et_string) * get_confirmed_mult(letter) / 1000
        if et_float > 999e9: 
            et_float = 999e9
            reduced_et_string = "999"
        
        if et_float.is_integer and et_float >= 100:
            degree = str(int(et_float))[3:]
            mult = degree.count('0')
        elif 10 < et_float < 100:
            mult = -1
        elif et_float < 10:
            mult = -2
        
        update_button_color("B3", get_col(int(reduced_et_string[2])))

    base_digits = int(reduced_et_string)
    multiplier_factor = actual_ohms / base_digits
    mult = round(math.log10(multiplier_factor))

    update_button_color("B4", get_mult_color(mult))
    update_button_color("B1", get_col(int(reduced_et_string[0])))
    update_button_color("B2", get_col(int(reduced_et_string[1])))
    
    root.focus_set()


vcmd = root.register(validate_input)
final_display_entry = tk.Entry(root, font=("Arial", 24), width=15, justify="center",
                               validate="key", validatecommand=(vcmd, "%P"))
final_display_entry.place(x=100, y=450)

final_display_entry.bind(
    "<Return>",
    lambda e: process_entry(final_display_entry))

final_display_entry.bind(
    "<FocusOut>",
    lambda e: process_entry(final_display_entry))

def calculate_resistance():
    final_display_entry.delete(0, tk.END)

    if bF.curr_band_num == 4:
        try:
            b1 = b1_val
            b2 = b2_val
            b4 = b4_val

            if b1 is None or b2 is None or b4 is None:
                return
            
            digits = int(f"{b1}{b2}")
            final_val = digits * b4

            letter = check_letter(float(final_val))
            divisor = get_confirmed_mult(letter)
            final_val = final_val / divisor
            if final_val.is_integer():
                final_val = int(final_val)

            if letter == "R": letter = "" 

            final_text = f"{final_val}{letter}\u03a9"
        
            final_display_entry.insert(0, final_text)
        
        except Exception as e:
            pass

    else:
        try:
            b1 = b1_val
            b2 = b2_val
            b3 = b3_val
            b4 = b4_val
        
            if b1 is None or b2 is None or b3 is None or b4 is None:
                return
            
            digits = int(f"{b1}{b2}{b3}")
            final_val = digits * b4
            
            letter = check_letter(float(final_val))
            divisor = get_confirmed_mult(letter)
            final_val = final_val / divisor
            if final_val.is_integer():
                final_val = int(final_val)

            if letter == "R": letter = "" 

            final_text = f"{final_val}{letter}\u03a9"

            final_display_entry.insert(0, final_text)
        
        except Exception as e:
            pass


## changing band color
def update_button_color(band_id, color_name):

    global b1_val
    global b2_val
    global b3_val
    global b4_val
    global b5_val
    global b6_val

    # mapping band IDs and button variables
    button_map = {
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
        "White": white_band.hex_code,
        "Gray": gray_band.hex_code,
        "Gold": gold_band.hex_code,
        "Silver": silver_band.hex_code,
    }

    class_map = {
        "Black": black_band,
        "Brown": brown_band,
        "Red": red_band,
        "Orange": orange_band,
        "Yellow": yellow_band,
        "Green": green_band,
        "Blue": blue_band,
        "Violet": violet_band,
        "White": white_band,
        "Gray": gray_band,
        "Gold": gold_band,
        "Silver": silver_band,
    }

    superscripts = {
        -1: "⁻¹", -2: "⁻²",
        0: "⁰", 1: "¹", 2: "²", 3: "³", 4: "⁴", 
        5: "⁵", 6: "⁶", 7: "⁷", 8: "⁸", 9: "⁹"
    }

    # find the correct button and correct color
    target_button = button_map.get(band_id)
    target_color = color_map.get(color_name)

    if target_button:
        # update the background color of the button
        target_button.config(bg=target_color)

    # changes text in labelframes
    band_color = class_map.get(color_name)
    if band_id == "B1":
        label_LF1.config(text = band_color.first_digit)
        b1_val = band_color.first_digit
    elif band_id == "B2":
        label_LF2.config(text = band_color.second_digit)
        b2_val = band_color.second_digit
    elif band_id == "B3":
        label_LF3.config(text = band_color.third_digit)
        b3_val = band_color.third_digit
    elif band_id == "B4":
        label_LF4.config(text = f"10{superscripts[band_color.power]}")
        b4_val = band_color.multiplier
    elif band_id == "B5":
        label_LF5.config(text = f"{band_color.tolerance} %")
        b5_val = band_color.tolerance
    elif band_id == "B6":
        label_LF6.config(text = f"{band_color.tempcoeff} ppm/\u00b0C")
        b6_val = band_color.tempcoeff

    calculate_resistance()

# closes dropdown if user clicks anywhere outside the dropdown itself or the band buttons
def close_dropdown_on_outside_click(event):
    # if the dropdown not open, do nothing
    if not dropdown.winfo_viewable():
        return

    clicked_widget = event.widget

    # get raw string identity path of widget
    widget_path = str(clicked_widget).lower()

    # ignore clicks on popdown, list options, or scrollbar
    if (
        "popdown" in widget_path
        or "listbox" in widget_path
        or "scrollbar" in widget_path
    ):
        return

    # check the true tkinter class name for fallback safety
    try:
        widget_class = clicked_widget.winfo_class()
    except Exception:
        widget_class = ""

    if widget_class in ("TCombobox", "Listbox"):
        return

    # handle clicking drop-down arrow to not register as parent master widget
    if clicked_widget == dropdown:
        return

    # check if clicked widget is a band button
    button_widgets = [
        button_1,
        button_2,
        button_3,
        button_4,
        button_5,
        button_6,
    ]
    if clicked_widget in button_widgets:
        return

    # click is confirmed outside; hide  menu
    dropdown.place_forget()
    bF.state["active_band"] = None

root.bind_all("<Button-1>", close_dropdown_on_outside_click)
root.mainloop()