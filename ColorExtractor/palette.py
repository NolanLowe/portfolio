import math
from tkinter import Frame
from swatch import Swatch


class Palette(Frame):
    def __init__(self, master):
        super().__init__(master=master)
        self.swatches = []

    def add_swatch(self, rgb, prevalence):
        self.swatches.append(Swatch(master=self, rgb=rgb, prevalence=prevalence))

    def construct(self):
        row, col, side_len = 0, 0, math.ceil(math.sqrt(len(self.swatches)))

        for s in self.swatches:
            s.grid(row=row, column=col)
            row += 1
            if row == side_len:
                row = 0
                col += 1
            if col == side_len:
                return

