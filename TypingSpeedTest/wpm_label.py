from tkinter import Label
from checker import Checker

class WPM(Checker):
    def __init__(self, label: Label):
        super().__init__()
        self.label = label

    def update(self):
        self.label.configure(text=f"TIME:{Checker.timer.get_str_time()}")



