import tkinter as tk
from tkinter import ttk


class EnhancedDropdown(ttk.Combobox):

    def __init__(self, master, options, **kwargs):
        #start normal so user can type to search
        super().__init__(master, values=options, state="normal", **kwargs)
        self.all_options = options

        # separate bindings for autocomplete typing loop
        self.bind("<KeyRelease>", self._on_key_release)
        self.bind("<BackSpace>", self._on_backspace)
        self._skip_autocomplete = False

    # flags deleting text to not force auto-completions
    def _on_backspace(self, event):
        self._skip_autocomplete = True

    # ignore some controls
    def _on_key_release(self, event):
        if event.keysym in (
            "Left",
            "Right",
            "Up",
            "Down",
            "Return",
            "Escape",
            "Tab",
            "Shift_L",
            "Shift_R",
            "Control_L",
            "Control_R",
            "Alt_L",
            "Alt_R",
        ):
            return

        # ff user backspaces, reset flag and allow deletion
        if self._skip_autocomplete:
            self._skip_autocomplete = False
            return

        typed_text = self.get()

        # if empty, reset drop list to show all valid colors
        if not typed_text:
            self["values"] = self.all_options
            return

        # filter backend list to search color matches
        matches = [
            item
            for item in self.all_options
            if item.lower().startswith(typed_text.lower())
        ]
        self["values"] = matches

        # add remaining text as editable highlighted selection
        if matches:
            best_match = matches[0]
            current_length = len(typed_text)

            # insert matching option capitalization correctly
            self.set(best_match)

            # highlight from where the user stopped typing to the end of the word
            self.selection_range(current_length, tk.END)
            self.icursor(current_length)

    def validate_entry(self):
        return self.get() in self.all_options

def handle_color_selection(event, dropdown, state, update_ui_callback):
    if dropdown.validate_entry():
        selected_color = dropdown.get()
        update_ui_callback(state["active_band"], selected_color)
        dropdown.selection_clear()
        dropdown.place_forget()
