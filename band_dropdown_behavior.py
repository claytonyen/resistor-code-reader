import tkinter as tk
from tkinter import ttk


class EnhancedDropdown(ttk.Combobox):

    def __init__(self, master, options, **kwargs):
        #start normal so user can type to search
        super().__init__(master, values=options, state="normal", **kwargs)
        self.all_options = options

        self.display_to_name = {}

        # separate bindings for autocomplete typing loop
        self.bind("<KeyRelease>", self._on_key_release)
        self.bind("<BackSpace>", self._on_backspace)
        self.bind("<Up>", lambda event: "break")
        self.bind("<Down>", lambda event: "break")
        self._skip_autocomplete = False

    def set_option_colors(self, color_pairs):
        self._color_pairs = color_pairs
        try:
            popdown = self.tk.eval(f"ttk::combobox::PopdownWindow {self}")
            listbox = f"{popdown}.f.l"
            self._apply_colors(listbox)

            if not getattr(self, "_listbox_bound", False):
                self.tk.call("bind", listbox, "<Map>", self.register(lambda: self._apply_colors(listbox)))
                self._listbox_bound = True
        except tk.TclError:
            pass

    def _apply_colors(self, listbox):
        values = self.cget("values")
        if values:
            self.tk.call(listbox, "delete", 0, "end")
            self.tk.call(listbox, "insert", "end", *values)
            max_len = max(len(v) for v in values)
            self.tk.call(listbox, "configure", "-width", max_len + 2)
        for index, (bg, fg) in enumerate(getattr(self, "_color_pairs", [])):
            try:
                self.tk.call(listbox, "itemconfigure", index, "-background", bg, "-foreground", fg)
            except tk.TclError:
                pass

        if not getattr(self, "_arrow_key_bound", False):
            self.tk.call("bind", listbox, "<Up>", "break")
            self.tk.call("bind", listbox, "<Down>", "break")
            self._arrow_key_bound = True

        if not getattr(self, "_hover_bound", False):
            hover_cmd = self.register(lambda y: self._on_hover(listbox, y))
            self.tk.call("bind", listbox, "<Motion>", f"{hover_cmd} %y")
            self._hover_bound = True

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
    
    @staticmethod
    def _lighten(hex_color, factor=0.4):
        hex_color = hex_color.lstrip("#")
        r, g, b = int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)
        r = int(r + (255 - r) * factor)
        g = int(g + (255 - g) * factor)
        b = int(b + (255 - b) * factor)
        return (r, g, b), f"#{r:02x}{g:02x}{b:02x}"

    @staticmethod
    def _contrast_fg(rgb):
        r, g, b = rgb
        luminance = (0.3 * r + 0.587 * g + 0.114 * b) / 255
        return "#FFFFFF" if luminance < 0.47 else "#000000"

    def _on_hover(self, listbox, y):
        try:
            index = int(self.tk.call(listbox, "nearest", y))
        except (tk.TclError, ValueError):
            return
        pairs = getattr(self, "_color_pairs", [])
        if 0 <= index < len(pairs):
            bg, _ = pairs[index]
            light_rgb, light_hex = self._lighten(bg)
            fg = self._contrast_fg(light_rgb)
            self.tk.call(listbox, "configure", "-selectbackground", light_hex, "-selectforeground", fg)

def handle_color_selection(event, dropdown, state, update_ui_callback):
    if dropdown.validate_entry():
        selected_color = dropdown.display_to_name.get(dropdown.get(), dropdown.get())
        update_ui_callback(state["active_band"], selected_color)
        dropdown.selection_clear()
        dropdown.place_forget()
