import argparse
from sched import scheduler
import subprocess
from time import sleep, time
from threading import Thread


class RepeatedTimer(Thread):
    def __init__(self, interval, function):
        self.interval = interval
        self.function = function
        self.stopped = False
        super().__init__()

    def run(self):
        while not self.stopped:
            sleep(self.interval)
            self.function()


class Updater(object):
    def __init__(self):
        self.start = time()

    def elapsed(self):
        return time() - self.start

    def __call__(self):
        print(" {:.2f}     ".format(self.elapsed()), end='\r')


def main():
    parser = argparse.ArgumentParser()
    known, unknown_args = parser.parse_known_args()
    
    timer = RepeatedTimer(0.08, Updater())
    timer.start()
    subprocess.call(unknown_args)
    timer.stopped = True
    

main()
