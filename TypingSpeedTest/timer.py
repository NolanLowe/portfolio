import time


class Timer:
    def __init__(self):
        self.starting_time = None

    def start(self) -> None:
        """
        'starts' the timer. Gets current time in S, to be used to divine time elapsed at a later date.
        :return: None
        """
        self.starting_time = time.time()

    def get_elapsed_time(self) -> str:
        """
        gets time passed since start of timer
        :return: string: MM:SS.MS
        """
        seconds = round(time.time() - self.starting_time, 2)
        minutes = seconds % 60
        seconds -= (60 * minutes)
        return f"{minutes:0>2}:{seconds}"
