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
        space = self.tkfont.measure(" ")

        for i in range(len(line)):  # go through each word in the full actual prompter line
            for j in range(len(line[i])):  # go through each letter of each full, target word
                letter_length = self.tkfont.measure(line[i][j])
                if i < len(typed_line) and j < len(typed_line[i]):  # check if the user has typed this far, only want to color code for letters they have typed.
                    if typed_line[i][j] == line[i][j]:
                        self.create_text(x, y, text=line[i][j], stipple='', fill='green', anchor="nw")
                    else:
                        self.create_text(x, y, text=line[i][j], stipple='', fill='red', anchor="nw")
                else:
                    self.create_text(x, y, text=line[i][j], anchor="nw")    # user hasn't typed that far in the prompt, no color code
                x += letter_length

            # individual word has ended, add a space (they've been removed by split())
            self.create_text(x, y, text=" ", anchor="nw")
            x += space
