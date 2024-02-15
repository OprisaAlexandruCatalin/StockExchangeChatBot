import tkinter as tk

#  It is used to create a text widget with a placeholder text that is displayed when the widget is empty
class PlaceHolder(tk.Text):
    def __init__(self, master=None, placeholder="", *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.placeholder = placeholder
        self.bind("<FocusIn>", self._removePlaceholder)
        self.bind("<FocusOut>", self._addPlaceholder)
        self._addPlaceholder()

    def _removePlaceholder(self, event=None):
        if self.get("1.0", "end-1c") == self.placeholder:
            self.delete("1.0", "end")

    def _addPlaceholder(self, event=None):
        if not self.get("1.0", "end-1c"):
            self.insert("1.0", self.placeholder)