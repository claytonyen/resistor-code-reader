import tkinter as tk
from tkinter import ttk

class OhmDropdown(ttk.Combobox):

    def __init__(self, master, options, **kwargs):
        super().__init__(master, values=options, state="readonly", **kwargs)
        self.all_options = options

        