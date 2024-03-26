from tkinter import *
import pyperclip as pc

class Palette(Canvas):
    def __init__(self, colors, size):
        super().__init__()
        self.colors = colors
        self.size = size
        self.configure(width=size, height=size, bg="black", highlightthickness=False)
        x = 0
        y = size / 8
        for color in colors:
            self.create_line(x, y, x + size, y, fill=color, width=size / 4)
            y += (size / 4)

        self.bind("<Button-1>", self.clicked)

    def clicked(self, event: Event):
        pc.copy("[" + ", ".join(self.colors) + "]")

    def set_colors(self, colors):
        x = 0
        y = self.size / 8
        for color in colors:
            self.create_line(x, y, x + self.size, y, fill=color, width=self.size / 4)
            y += (self.size / 4)

