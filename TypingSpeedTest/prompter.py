from tkinter import Canvas, font as f

from checker import Checker
from tkinter.font import Font


class Prompter(Canvas, Checker):
    def __init__(self, master, font: Font, width=800, height=100):
        super().__init__(master, width=width, height=height)
        # , relief='raised', borderwidth=5
        self.tkfont = font

    def print(self):
        self.delete('all')
        line = Checker.filehandler.get().split()
        typed_line = Checker.typed_line.split()
        print("typed line:", typed_line)
        x = 20
        y = 20
        word_height = round(self.tkfont.metrics('linespace') * 1.5)
        word_spacing = round(0.4 * self.tkfont['size'])

        for i in range(len(line)):
            word_length = self.tkfont.measure(line[i])
            if i < len(typed_line):
                if typed_line[i] == line[i]:
                    self.create_text(x, y, text=line[i], stipple='', fill='green', anchor="nw")
                else:
                    self.create_text(x, y, text=line[i], stipple='', fill='red', anchor="nw")
            else:
                self.create_text(x, y, text=line[i], anchor="nw")
            x += word_length + word_spacing
        pass
