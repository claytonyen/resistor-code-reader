import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class EnhancedDropdown(ttk.Combobox):
    def __init__(self, master, options, **kwargs):
        super().__init__(master, values=options, **kwargs)
        self.all_options = options
        
        self.bind("<Key>", self._on_key_press)
        self.bind("<KeyRelease>", self._on_key_release)

    def _on_key_press(self, event):
        if event.keysym in ("BackSpace", "Delete"):
            return
            
        if event.keysym in ("Shift_L", "Shift_R", "Control_L", "Control_R", "Alt_L", "Alt_R", "Left", "Right", "Return", "Tab"):
            return

        current_cursor_pos = self.index(tk.INSERT)
        
        if self.selection_present():
            typed_text = self.get()[:self.index(tk.SEL_FIRST)] + event.char
        else:
            typed_text = self.get()[:current_cursor_pos] + event.char

        if not event.char:
            return

    def _on_key_release(self, event):
        if event.keysym in ("Left", "Right", "Return", "Escape"):
            return

        typed_text = self.get()
        if self.selection_present():
            typed_text = self.get()[:self.index(tk.SEL_FIRST)]

        if not typed_text:
            self['values'] = self.all_options
            return

        matches = [item for item in self.all_options if item.lower().startswith(typed_text.lower())]
        self['values'] = matches

        if matches and event.keysym not in ("BackSpace", "Delete"):
            self.tk.call('ttk::combobox::Post', self._w)

    def validate_entry(self):
        """Checks if current text exactly matches an authorized option."""
        return self.get() in self.all_options

# --- Application Setup ---

def submit_selection():
    if dropdown.validate_entry():
        return
    else:
        messagebox.showerror("Invalid Option", "Please select a valid option from the dropdown menu.")

root = tk.Tk()
root.title("Advanced Dropdown UI")
root.geometry("400x250")

fruits = ["Apple", "Apricot", "Banana", "Blueberry", "Cherry", "Cranberry", "Grape", "Mango", "Orange", "Peach"]

label = tk.Label(root, text="Type to search fruits:")
label.pack(pady=10)

dropdown = EnhancedDropdown(root, options=fruits, width=25)
dropdown.pack(pady=10)

submit_btn = tk.Button(root, text="Submit Selection", command=submit_selection)
submit_btn.pack(pady=20)

root.mainloop()