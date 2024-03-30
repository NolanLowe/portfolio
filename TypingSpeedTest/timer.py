from time import time

class Timer():
    def __init__(self):
        self.current_time = 0
        self.is_going = False
        self.stored = 0

    def start(self):
        self.current_time = time()
        self.is_going = True

    def pause(self):
        self.stored += time() - self.current_time
        self.current_time = 0
        self.is_going = False

    def get_elapsed_time(self):
        if self.current_time == 0:  #
            return self.stored
        else:
            return time() - self.current_time + self.stored

    def get_str_time(self):
        t = self.get_elapsed_time()
        t = "{:.2f}".format(t)
        return f"{t:0>4}"

    def get_minutes(self):
        return self.get_elapsed_time() / 60

    def reset(self):
        self.current_time = 0
        self.stored = 0
        self.is_going = False

