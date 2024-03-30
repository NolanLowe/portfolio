from tkinter import Label, Event
from checker import Checker


class AccuracyLabel(Checker):
    def __init__(self, label: Label):
        super().__init__()
        self.label = label
        self.correct = 0
        self.total = 0

    def update(self, event: Event):
        if event.keycode in [8, 32]:  # backspace, spacebar
            return

        typed = Checker.typed_line
        actual = Checker.filehandler.get()

        if len(typed) <= len(actual):  # make sure you haven't typed past the last letter.
            print(typed[-1], actual[len(typed) - 1])
            if typed[-1] == actual[len(typed) - 1]:
                self.correct += 1

        self.total += 1
        self.label.configure(text=f"ACCURACY:{round(self.correct / self.total * 100, 2)}%")
