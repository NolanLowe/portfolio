from tkinter import Frame, Entry, Label


class InputComponent(Frame):
    def __init__(self, master, text, default_value=None):
        super().__init__(master=master)
        self.configure(width=40, height=10)
        self.entry = Entry(master=self, width=10)
        if default_value:
            self.entry.insert(index=0, string=default_value)
        self.label = Label(master=self, text=text, width=30)
        self.label.grid(row=0, column=0, sticky="w")
        self.entry.grid(row=0, column=1, sticky="e")

    def get(self) -> int:
        return int(self.entry.get())
