from tkinter import Entry, Event
from checker import Checker

class Typer(Entry, Checker):
    def __init__(self, master, width=80):
        super().__init__(master, width=width)

    def load(self):
        """
        loads up the shared class object with the users current attempt
        does not do anything else.
        :return:
        """
        Checker.typed_line = self.get()