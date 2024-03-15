import time 
class Stopwatch :
    def __init__(self):
        self.start_time = None
        self.stop_time = None
        self.running = False

    def start(self):
        if not self.running:
            self.start_time = time.time()
            self.running = True

    def stop(self):
        if self.running:
            self.stop_time = time.time()
            self.running = False

    def elapsed_time(self):
        if self.running:
            return time.time() - self.start_time
        else:
            return self.stop_time - self.start_time

    def reset(self):
        self.start_time = None
        self.stop_time = None
        self.running = False