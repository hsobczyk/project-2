import subprocess
import threading
import time, datetime

launcher_threads = [False] * 5 # False is a spot that is available for thread

def timed_launch(pos: int, filename, delta) -> None:
    """
    This is the main thread function, it runs a timer loop and runs the specified program at the end.
    Will also end early if stop_all_threads flag or its thread_stopper[pos] flag are detected as True.
    :param pos: the position of thread in the list.
    :param filename: the location and filename of the program.
    :param delta: datetime object to indicate how long unit it runs
    """
    timer = datetime.datetime.now() + delta
    while datetime.datetime.now() < timer:
        time.sleep(1)
    subprocess.Popen(filename)

def delta_creator(ihours:int=0,iminutes:int=0,iseconds:int=0):
    """
    Function that creates the time delta.
    For usage without the need to include datetime in other files
    :param hours: hours integer
    :param minutes: minutes integer
    :param seconds: seconds integer
    :return: datetime object
    """
    return datetime.timedelta(hours=ihours,minutes=iminutes,seconds=iseconds)

def thread_creator(filename, delta):
    """
    Creates threads in launcher_threads.
    :param filename: the file name and location of program to be executed.
    :param delta: the time delta object
    """
    for i in range(5):
        if launcher_threads[i] == False:
            launcher_threads[i] = threading.Thread(target=timed_launch, args={i, filename, delta})
            launcher_threads[i].daemon = True #This thread dies when program ends.
            break
        else:
            continue

def run_threads():
    """
    Function that starts all the threads
    """
    for i in range(5):
        if not launcher_threads[i]:
            continue
        launcher_threads[i].start()

def main():
    # all of this is junk code for developement
    thread_creator('C:\\Windows\\System32\\calc.exe', datetime.timedelta(seconds=3))
    thread_creator('C:\\Windows\\System32\\calc.exe', datetime.timedelta(seconds=7))
    #thread_creator('C:\\Windows\\System32\\calc.exe', delta_creator(iseconds=12))
    run_threads()

if __name__ == '__main__':
    main()