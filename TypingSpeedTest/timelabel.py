from tkinter import Label
from checker import Checker
import threading
from time import sleep


class TimeLabel(Checker):
    def __init__(self, label: Label):
        super().__init__()
        self.label = label
        self.t = threading.Thread(group=None, target=self.__update, name="Thread-0")
        self.stopped = False
        self.iterations = 0

    def __update(self, delay: float = 0.07):
        self.label.configure(text=f"TIME:{Checker.timer.get_str_time()}s")
        self.label.master.update()
        sleep(delay)
        if not self.stopped:
            self.__update()

    def start(self):
        self.t = threading.Thread(group=None, target=self.__update, name=f"Thread-{self.iterations}")
        self.iterations += 1
        self.t.start()
        self.stopped = False

    def stop(self):
        self.stopped = True
        self.t.join(timeout=0.1)

    def has_started(self):
        return self.t.is_alive()