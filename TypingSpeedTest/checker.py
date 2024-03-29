from timer import Timer
from filehandler import FileHandler


def line_complete():
    line = Checker.filehandler.get().split()
    typed_line = Checker.typed_line.split()
    if len(line) == len(typed_line):
        return True
    else:
        return False


class Checker:
    timer = Timer()
    filehandler = FileHandler()
    typed_line: str = ""

    def __init__(self):
        pass
