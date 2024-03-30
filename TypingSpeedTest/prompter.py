from tkinter import Canvas, font as f

from checker import Checker
from tkinter.font import Font


class Prompter(Canvas, Checker):
    def __init__(self, master, font: Font, width=600, height=30):
        super().__init__(master, width=width, height=height)
        # , relief='raised', borderwidth=5
        self.tkfont = font
        self.w = width
        self.h = height

    def print(self):
        self.delete('all')
        line = Checker.filehandler.get().split()
        typed_line = Checker.typed_line.split()

        total_line_width = self.tkfont.measure(Checker.filehandler.get())
        x = (self.w - total_line_width) / 2
        y = (self.h - self.tkfont.metrics('linespace')) / 2

        for i in range(len(line)):
            word_length = self.tkfont.measure(line[i])
            if i < len(typed_line):
                if typed_line[i] == line[i]:
                    self.create_text(x, y, text=line[i], stipple='', fill='green', anchor="nw")
                else:
                    self.create_text(x, y, text=line[i], stipple='', fill='red', anchor="nw")
            else:
                self.create_text(x, y, text=line[i], anchor="nw")
            x += word_length

            space = self.tkfont.measure(" ")
            self.create_text(x, y, text=" ", anchor="nw")
            x += space


