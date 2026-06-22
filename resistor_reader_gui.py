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
button_4_band = tk.Button(root, text="4  Band", bd=2, font=("Arial", 18),
                          highlightthickness=2, highlightbackground="#000000",
                          activebackground="#D3D3D3",
                          command=lambda: bF.disable_button(button_4_band, button_5_band, button_6_band, 4,
                                                            button_3, button_4, button_6))
button_4_band.place(x=50, y=300, width=150, height=50)
button_5_band = tk.Button(root, text="5  Band", bd=2, font=("Arial", 18),
                          highlightthickness=2, highlightbackground="#000000",
                          activebackground="#D3D3D3",
                          command=lambda: bF.disable_button(button_5_band, button_4_band, button_6_band, 5,
                                                            button_3, button_4, button_6))
button_5_band.place(x=225, y=300, width=150, height=50)
button_6_band = tk.Button(root, text="6  Band", bd=2, font=("Arial", 18),
                          highlightthickness=2, highlightbackground="#000000", 
                          activebackground="#D3D3D3",
                          command=lambda: bF.disable_button(button_6_band, button_4_band, button_5_band, 6,
                                                            button_3, button_4, button_6))
button_6_band.place(x=400, y=300, width=150, height=50)
button_6_band.config(state=tk.DISABLED, relief=tk.SUNKEN)  # start with 6 band disabled


## reset button ##
reset_button = tk.Button(root, text="Reset", 
    bd=2, bg="#FF3838", font=("Arial", 12),
    highlightthickness=2, highlightbackground="#000000",
    command=lambda: bF.reset_band_colors(button_1, button_2, button_3, button_4, button_5, button_6))
reset_button.place(x=475, y=362.5, width=75, height=37.5)


## change resistor body color ##
button_res_color = tk.Button(root, text="Change Body Color",
    bd=2, bg="#FFFFFF", font=("Arial", 10),
    highlightthickness=2, highlightbackground="#000000",
    command=lambda: bF.change_resistor_body_color(canvas, res_poly, button_3, button_6))
button_res_color.place(x=300, y=362.5, width=150, height=37.5)

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
button_1.place(x=100, y=78, width=37.5, height=145)

button_2 = tk.Button(root, text="2", font=("Arial", 12),
    bd=1, bg="#D2B48C",
    command=lambda: bF.on_band_click(button_2, "B2", dropdown),
)
button_2.place(x=175, y=98, width=37.5, height=105)

button_3 = tk.Button(root, text="3", font=("Arial", 12),
    bd=1, bg="#D2B48C",
    command=lambda: bF.on_band_click(button_3, "B3", dropdown),
)
button_3.place(x=225, y=101, width=37.5, height=99)

button_4 = tk.Button(root, text="M\nU\nL\nT", font=("Arial", 10),
    bd=1, bg="#D2B48C",
    command=lambda: bF.on_band_click(button_4, "B4", dropdown),
)
button_4.place(x=275, y=101, width=37.5, height=99)

button_5 = tk.Button(root, text="T\nO\nL", font=("Arial", 10),
    bd=1, bg="#D2B48C",
    command=lambda: bF.on_band_click(button_5, "B5", dropdown),
)
button_5.place(x=387.5, y=98, width=37.5, height=105)

button_6 = tk.Button(
    root, text="T\nC\nR", font=("Arial", 10),
    bd=1, bg="#D2B48C",
    command=lambda: bF.on_band_click(button_6, "B6", dropdown),
)
button_6.place(x=462.5, y=78, width=37.5, height=145)

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
        "Black": "#000000",
        "Brown": "#8B4513",
        "Red": "#FF0000",
        "Orange": "#FF8800",
        "Yellow": "#FFFF00",
        "Green": "#008000",
        "Blue": "#0000FF",
        "Violet": "#A22AA2",
        "White": "#FFFFFF",
        "Gray": "#808080",
        "Gold": "#EFBF04",
        "Silver": "#C0C0C0",
    }

    # find the correct button and correct color
    target_button = button_mapping.get(band_id)
    target_color = color_map.get(color_name)

    if target_button:
        # update the background color of the button dynamically
        target_button.config(bg=target_color)

        # adjust text color for readability against dark backgrounds
        if color_name in ("Black", "Brown", "Red", "Blue", "Green", "Violet"):
            target_button.config(fg="white")
        else:
            target_button.config(fg="black")

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


## display numerical values ##



root.bind_all("<Button-1>", close_dropdown_on_outside_click)
root.mainloop()