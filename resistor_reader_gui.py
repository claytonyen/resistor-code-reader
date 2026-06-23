import tkinter as tk
from tkinter import ttk
import button_functions as bF
import dropdown_behavior as dB
import resistor_calculation as rC


root = tk.Tk()
root.option_add("*TCombobox*Listbox*Font", ("Arial", 11))
root.title("Resistor Color Code Reader")
root.geometry("600x700")
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


## canvas ##
canvas = tk.Canvas(root, width=600, height=700, bg="#D3D3D3")
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
                          command=lambda: bF.disable_button(button_4_band, button_5_band, button_6_band, 4,
                                                            button_3, button_4, button_6,
                                                            digit3_LF, mult_LF, tcr_LF,
                                                            label_LF3, label_LF6))
button_4_band.place(x=25, y=25, width=150, height=50)
button_5_band = tk.Button(root, text="5  Band", bd=2, font=("Arial", 18),
                          highlightthickness=2, highlightbackground="#000000",
                          activebackground="#D3D3D3",
                          command=lambda: bF.disable_button(button_5_band, button_4_band, button_6_band, 5,
                                                            button_3, button_4, button_6,
                                                            digit3_LF, mult_LF, tcr_LF,
                                                            label_LF3, label_LF6))
button_5_band.place(x=225, y=25, width=150, height=50)
button_6_band = tk.Button(root, text="6  Band", bd=2, font=("Arial", 18),
                          highlightthickness=2, highlightbackground="#000000", 
                          activebackground="#D3D3D3",
                          command=lambda: bF.disable_button(button_6_band, button_4_band, button_5_band, 6,
                                                            button_3, button_4, button_6,
                                                            digit3_LF, mult_LF, tcr_LF,
                                                            label_LF3, label_LF6))
button_6_band.place(x=425, y=25, width=150, height=50)
button_6_band.config(state=tk.DISABLED, relief=tk.SUNKEN)  # start with 6 band disabled


## reset button ##
def clear_res(button_1, button_2, button_3, button_4, button_5, button_6):
    bF.reset_band_colors(button_1, button_2, button_3, button_4, button_5, button_6)
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
pgradient = tk.PhotoImage(file="pastelgradient.png")
button_res_color = tk.Button(root, text="Change Body Color",
    bd=2, bg="#FFFFFF", font=("Arial", 10),
    highlightthickness=2, highlightbackground="#000000",
    image=pgradient, compound=tk.CENTER,
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


## change resistor band colors ##
# initialize dropdown
dropdown = dB.EnhancedDropdown(root, options=[], style="BigArrow.TCombobox")
band_pressed = False

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
button_1 = tk.Button(root, text="1", font=("Arial", 12),
    bd=1, bg="#D2B48C",
    command=lambda: bF.on_band_click(button_1, "B1", dropdown),
)
button_1.place(x=100, y=153, width=37.5, height=145)

button_2 = tk.Button(root, text="2", font=("Arial", 12),
    bd=1, bg="#D2B48C",
    command=lambda: bF.on_band_click(button_2, "B2", dropdown),
)
button_2.place(x=175, y=173, width=37.5, height=105)

button_3 = tk.Button(root, text="3", font=("Arial", 12),
    bd=1, bg="#D2B48C",
    command=lambda: bF.on_band_click(button_3, "B3", dropdown),
)
button_3.place(x=225, y=176, width=37.5, height=99)

button_4 = tk.Button(root, text="M\nU\nL\nT", font=("Arial", 10),
    bd=1, bg="#D2B48C",
    command=lambda: bF.on_band_click(button_4, "B4", dropdown),
)
button_4.place(x=275, y=176, width=37.5, height=99)

button_5 = tk.Button(root, text="T\nO\nL", font=("Arial", 10),
    bd=1, bg="#D2B48C",
    command=lambda: bF.on_band_click(button_5, "B5", dropdown),
)
button_5.place(x=387.5, y=173, width=37.5, height=105)

button_6 = tk.Button(
    root, text="T\nC\nR", font=("Arial", 10),
    bd=1, bg="#D2B48C",
    command=lambda: bF.on_band_click(button_6, "B6", dropdown),
)
button_6.place(x=462.5, y=153, width=37.5, height=145)

# changing band colors
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
        "Black": rC.black_band.hex_code,
        "Brown": rC.brown_band.hex_code,
        "Red": rC.red_band.hex_code,
        "Orange": rC.orange_band.hex_code,
        "Yellow": rC.yellow_band.hex_code,
        "Green": rC.green_band.hex_code,
        "Blue": rC.blue_band.hex_code,
        "Violet": rC.violet_band.hex_code,
        "White": rC.white_band.hex_code,
        "Gray": rC.gray_band.hex_code,
        "Gold": rC.gold_band.hex_code,
        "Silver": rC.silver_band.hex_code,
    }

    class_map = {
        "Black": rC.black_band,
        "Brown": rC.brown_band,
        "Red": rC.red_band,
        "Orange": rC.orange_band,
        "Yellow": rC.yellow_band,
        "Green": rC.green_band,
        "Blue": rC.blue_band,
        "Violet": rC.violet_band,
        "White": rC.white_band,
        "Gray": rC.gray_band,
        "Gold": rC.gold_band,
        "Silver": rC.silver_band,
    }

    superscripts = {
        -1: "⁻¹", -2: "⁻²",
        0: "⁰", 1: "¹", 2: "²", 3: "³", 4: "⁴", 
        5: "⁵", 6: "⁶", 7: "⁷", 8: "⁸", 9: "⁹"
    }

    # find the correct button and correct color
    target_button = button_mapping.get(band_id)
    target_color = color_map.get(color_name)

    if target_button:
        # update the background color of the button
        target_button.config(bg=target_color)

        # adjust text color for readability against dark backgrounds
        if color_name in ("Black", "Brown", "Red", "Blue", "Green", "Violet"):
            target_button.config(fg="white")
        else:
            target_button.config(fg="black")

    # changes text in labelframes
    band_color = class_map.get(color_name)
    if band_id == "B1":
        label_LF1.config(text = band_color.first_digit)
    elif band_id == "B2":
        label_LF2.config(text = band_color.second_digit)
    elif band_id == "B3":
        label_LF3.config(text = band_color.third_digit)
    elif band_id == "B4":
        label_LF4.config(text = f"10{superscripts[band_color.power]}")
    elif band_id == "B5":
        label_LF5.config(text = f"{band_color.tolerance} %")
    else:
        label_LF6.config(text = f"{band_color.tempcoeff} ppm/\u00b0C")

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