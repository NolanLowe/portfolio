from tkinter import Label
from checker import Checker


class WPM(Checker):
    def __init__(self, label: Label):
        super().__init__()
        self.label = label
        self.correct_words = 0

        self.marked_correct = None

    def update(self):
        if self.monitor != Checker.filehandler.get():
            self.marked_correct = [False for _ in Checker.filehandler.get().split()]
            self.monitor = Checker.filehandler.get()
        """
        for each word in what the user has typed so far
        if it matches the corresponding word in the prompt, 
        and has not already been awarded, award one point, and note down that word, so it isn't awarded again.
        """

        actual_line = Checker.filehandler.get().split()
        typed_line = Checker.typed_line.split()

        for i in range(len(typed_line) - 1):  # everything but the last word from the prompt, which is almost guaranteed to be incomplete
            if actual_line[i] == typed_line[i] and self.marked_correct[i] is False:
                self.marked_correct[i] = True
                self.correct_words += 1

        wpm = 0 if Checker.timer.get_minutes() == 0 else self.correct_words / Checker.timer.get_minutes()
        wpm = "{:.2f}".format(wpm)
        self.label.configure(text=f"WPM:{wpm}")
