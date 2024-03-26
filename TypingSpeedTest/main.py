from tkinter import Tk, Button
from timer import Timer
from prompter import Prompter
from texter import Texter

prompter_sourcetext = "chaff.txt"


def main():
    window = Tk()

    clock = Timer()

    prompter = Prompter(window)
    text = prompter.flourish()
    prompter.grid(row=0, column=0, columnspan=3)

    texter = Texter(window, text=text)
    texter.grid_configure(row=1, column=0, columnspan=3)

    info = Button(bitmap='question')
    info.grid_configure(row=2, column=3, sticky="E")

    window.mainloop()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
