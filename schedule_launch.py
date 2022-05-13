import subprocess
import threading
import time, datetime

stop_all_threads = False
thread_stopper = []
launcher_threads = []

def timed_launch(pos: int, filename, delta) -> None:
    """
    This is the main thread function, it runs a timer loop and runs the specified program at the end.
    Will also end early if stop_all_threads flag or its thread_stopper[pos] flag are detected as True.
    :param pos: the position of thread in the list.
    :param filename: the location and filename of the program.
    :param delta: the time at which the program will be executed.
    """
    end_time = datetime.datetime.now() + delta
    while datetime.datetime.now() < end_time:
        time.sleep(1)
        if stop_all_threads or thread_stopper[pos]:
            print(pos) # REMOVE PRINT STATEMENT LATER
            break
    if not stop_all_threads or not thread_stopper:
        print(subprocess.Popen(filename)) # REMOVE PRINT STATEMENT LATER

def delta_creator(input):
    """
    Function that creates the time delta
    :param input: user input date and time string
    :return: datetime object
    """
    time = datetime.datetime.strptime(input, '%m/%d/%Y %I:%M%S %p')
    return time

def thread_creator():
    pass

def main():
    print(delta_creator("5/13/2022 6:00 PM"))

if __name__ == '__main__':
    main()