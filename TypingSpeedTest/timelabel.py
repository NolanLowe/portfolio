from tkinter import Label
from checker import Checker


class TimeLabel(Checker):
    def __init__(self, label: Label):
        super().__init__()
        self.label = label

    def update(self):
        self.label.configure(text=f"ElAPSED TIME:{Checker.timer.get_str_time()}s")
