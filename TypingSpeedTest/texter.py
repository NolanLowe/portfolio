from tkinter import Text, Frame, END


class Texter(Frame):
    def __init__(self, master, text):
        super().__init__(master)
        self.text_area = Text(self)
        self.text_area.insert(END, chars=text)

        self.text_area.pack()

    def load(self, text) -> None:
        self.text_area.insert(END, chars=text)

