from time import time


class Timer:
    def __init__(self, bullet_limit=0.5):
        self.start_time = time()
        self.bullet_limit = bullet_limit

    def can_fire(self):
        if (time() - self.start_time) > self.bullet_limit:
            self.start_time = time()
            return True
        else:
            return False

    def start(self):
        self.start_time = time()

    def elapsed(self, minimum):
        if minimum < (time() - self.start_time):
            self.start()
            return True
        else:
            return False

