from time import time

class Timer():
    def __init__(self):
        self.current_time = 0
        self.started = False

    def start(self):
        self.current_time = time()
        self.started = True


    def get_elapsed_time(self):
        if self.current_time == 0:
            return 0
        else:
            return time() - self.current_time

    def get_str_time(self):
        time = round(self.get_elapsed_time(), 2)
        return f"{time:0>4}"

    def get_minutes(self):
        return self.get_elapsed_time() / 60

    def reset(self):
        self.current_time = 0
        self.started = False

