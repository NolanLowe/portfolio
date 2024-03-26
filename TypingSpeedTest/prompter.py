from tkinter import *
from random import randint
from PIL import ImageFont

default_font = ("arial", 14)


def get_pil_text_size(text, font_size, font_name):
    font = ImageFont.truetype(font_name, font_size)
    size = font.getlength(text)
    return round(size * 1.33)


class Prompter(Frame):
    def __init__(self, master):
        super().__init__(master=master, width=800, height=400)
        self.font_size = default_font[1]
        self.font_size_px = round(self.font_size * 1.33)
        self.font = default_font

        with open(file="chaff.txt", mode='r') as file:
            self.text = file.readlines()
            while "\n" in self.text:
                self.text.remove('\n')
            self.current_index = 0

    def flourish(self) -> list[str]:
        """
        propogates the prompter panel with one paragraph.
        returns the paragraph as a list of individual words.
        :return: list of individual words used in prompter
        """
        if self.current_index == len(self.text) - 1:
            raise E
        else:
            self.current_index += 1

        max_cols = randint(9, 13)
        items = []
        words = self.text[self.current_index].strip().split()

        x = 0
        y = 0
        max_x = 800
        horizontal_word_spacing = 10
        vertical_word_spacing = self.font_size_px + 4

        for w in words:
            w = w.strip()
            brick = Label(self, text=w, font=self.font)

            word_length = get_pil_text_size(font_name=default_font[0], font_size=default_font[1], text=w)

            if x + word_length + horizontal_word_spacing > max_x:
                x = 0
                y += vertical_word_spacing

            brick.place(x=x, y=y)
            x += randint(8, horizontal_word_spacing) + word_length

            items.append(brick)

        return words
