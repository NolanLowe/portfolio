from tkinter import Canvas, Label, Event, Message, CENTER, SUNKEN
import pyperclip as pc


def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    r, g, b = rgb
    return f'#{r:02x}{g:02x}{b:02x}'


class Swatch(Canvas):
    width, height = 50, 50
    clipboard = ""

    def __init__(self, master, rgb, prevalence):
        super().__init__(master=master)

        self.color = _from_rgb(rgb)
        self.configure(width=Swatch.width, height=Swatch.height)
        self.create_line(0, 10, Swatch.width, 10, fill=self.color, width=20)
        self.create_text(0, 30, text=self.color, anchor="w")
        self.create_text(0, 40, text=f"%{prevalence}", anchor="w", font=("Helvetica", 8))
        self.bind("<Button-1>", self.clicked)
        self.prevalence = prevalence

    def clicked(self, event: Event):
        Swatch.clipboard += self.color + ", "
        pc.copy(Swatch.clipboard)
        self.show_msg()

    def show_msg(self):
        # msg = Message(self.master, text='copied!')
        # msg.place(relx=.5, rely=.5, anchor=CENTER)
        # self.master.after(1000, msg.destroy)

        lbl = Label(self, text="copied!")
        lbl.place(relx=.5, rely=.5, anchor=CENTER)
        self.after(500, lbl.destroy)
