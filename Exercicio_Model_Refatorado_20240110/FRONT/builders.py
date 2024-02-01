import tkinter as tk
from tkinter import ttk


class BuilderEntry(tk.Frame):
    def __init__(self, master, labelText, entryWidth=20, varType=str, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.entryVar = tk.StringVar()
        self.varType = varType

        self.label = tk.Label(self, text=labelText, anchor='w')
        self.label.pack(side='top', fill='x')

        self.entry = tk.Entry(self, textvariable=self.entryVar, width=entryWidth)
        self.entry.pack(side='bottom', anchor='w')

    def get(self):
        value = self.entry.get()
        try:
            return (self.varType(value))
        except(ValueError, TypeError):
            return None

    def set(self, value):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, value)


class BuilderCombobox(tk.Frame):
    def __init__(self, master, labelText, comboboxValues, comboboxWidth=20, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.comboboxVar = tk.StringVar()

        self.label = tk.Label(self, text=labelText, anchor='w')
        self.label.pack(side='top', fill='x')

        self.combobox = ttk.Combobox(self, textvariable=self.comboboxVar, values=comboboxValues, width=comboboxWidth)
        self.combobox.pack(side='bottom')

    def get(self):
        return self.combobox.get()

    def set(self, valor):
        self.combobox.set(valor)