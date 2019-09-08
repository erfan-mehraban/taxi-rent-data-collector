class waitTimeCalculator:
    LINEAR_TRESHOLD = 5
    LINEAR_WAIT_TIME = 1
    EXPONENTIAL_TRESHOLD = 15
    EXPONENTIAL_FACTOR = 2

    error_count = 0

    def __init__(self):
        self.error_queue = []

    def reset(self):
        self.error_count = 0

    def count_error(self):
        self.error_count += 1

    def get_wait_time(self):
        if self.error_count < self.LINEAR_TRESHOLD:
            return self.LINEAR_WAIT_TIME
        if self.error_count < self.EXPONENTIAL_TRESHOLD:
            return (self.error_count - self.LINEAR_TRESHOLD) * self.EXPONENTIAL_FACTOR
        raise TimeoutError

    def still_error(self):
        return self.error_count > 0
