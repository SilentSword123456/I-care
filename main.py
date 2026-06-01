import threading
import systemtray
import timer

timeSec = 1*60
breakSec = 20


StopEvent = threading.Event()

class Worker(threading.Thread):
    def __init__(self, timer, breakSec):
        super().__init__()
        self.timer = timer
        self.breakSec = breakSec
    def run(self):
        while not StopEvent.is_set():
            timer.scheduleBreak(self.timer, self.breakSec, StopEvent)

def stop():
    StopEvent.set()
def start():
    StopEvent.clear()

systemtrayThread = threading.Thread(target=systemtray.start, args=[stop])
timerThread = Worker(timeSec, breakSec)



def main():
    print("Starting app...")
    systemtrayThread.start()
    timerThread.start()
    print("The app is on!")



if __name__ == "__main__":
    main()