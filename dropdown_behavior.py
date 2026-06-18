import tkinter as tk
from tkinter import ttk


class EnhancedDropdown(ttk.Combobox):

    def __init__(self, master, options, **kwargs):
        # start with state="normal" so user can type to filter colors
        super().__init__(master, values=options, state="normal", **kwargs)
        self.all_options = options

        self.bind("<Key>", self._on_key_press)
        self.bind("<KeyRelease>", self._on_key_release)

    def _on_key_press(self, event):
        # ignore navigation keys and return/escape
        if event.keysym in ("BackSpace", "Delete"):
            return
        if event.keysym in (
            "Shift_L",
            "Shift_R",
            "Control_L",
            "Control_R",
            "Alt_L",
            "Alt_R",
            "Left",
            "Right",
            "Return",
            "Tab",
        ):
            return

        # get current cursor position and the text typed so far
        current_cursor_pos = self.index(tk.INSERT)
        if self.selection_present():
            typed_text = (
                self.get()[: self.index(tk.SEL_FIRST)] + event.char
            )
        else:
            typed_text = self.get()[:current_cursor_pos] + event.char

        if not event.char:
            return

    def _on_key_release(self, event):
        # ignore navigation keys and return/escape
        if event.keysym in ("Left", "Right", "Return", "Escape"):
            return

        # get current text in entry
        typed_text = self.get()
        if self.selection_present():
            typed_text = self.get()[: self.index(tk.SEL_FIRST)]

        if not typed_text:
            self["values"] = self.all_options
            return

        # filters colors based on typed text
        matches = [
            item for item in self.all_options
            if item.lower().startswith(typed_text.lower())
        ]
        self["values"] = matches

        if matches and event.keysym not in ("BackSpace", "Delete"):
            self.tk.call("ttk::combobox::Post", self._w)

    def validate_entry(self):
        return self.get() in self.all_options

def handle_color_selection(event, dropdown, state, update_ui_callback):
    if dropdown.validate_entry():
        selected_color = dropdown.get()
        update_ui_callback(state["active_band"], selected_color)
        dropdown.selection_clear()
        dropdown.place_forget()
