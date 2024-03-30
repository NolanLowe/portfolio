from typer import Typer
from prompter import Prompter
from timelabel import TimeLabel
from wpm_label import WPM
from accuracylabel import AccuracyLabel
from tkinter import Tk, font, Label, Event, END
from checker import Checker, line_complete

window = Tk()

typer = Typer(window)
prompter = Prompter(window, font=font.nametofont('TkTextFont'))
tl = TimeLabel(
    Label(window, text="TIME")
)
wpm = WPM(
    Label(window, text="WPM")
)
acc = AccuracyLabel(
    Label(window, text="ACC")
)

typer.grid(row=2, column=0, columnspan=3, padx=5, pady=5)
prompter.grid(row=1, column=0, columnspan=3, padx=5, pady=5)
tl.label.grid(row=0, column=0, padx=5, pady=5)
wpm.label.grid(row=0, column=1, padx=5, pady=5)
acc.label.grid(row=0, column=2, padx=5, pady=5)


def enter(event):
    if line_complete():
        Checker.timer.pause()
        tl.stop()
        Checker.filehandler.get_next()
        typer.delete(0, END)
        typer.load()
        prompter.print()
    else:
        pass


def keypress(event: Event):
    print("key:", event.char, 'code:', event.keycode)

    if event.keycode in [13, 16, 9]:  # enter, shift, tab
        return

    if Checker.timer.is_going is False:
        Checker.timer.start()

    if tl.has_started() is False:
        tl.start()

    typer.load()
    prompter.print()
    wpm.update()
    acc.update(event)

    return "break"


typer.bind('<Return>', enter)
typer.bind('<KeyRelease>', keypress)
prompter.print()

window.mainloop()



