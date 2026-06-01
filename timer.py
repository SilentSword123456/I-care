import time
import blackout
import notifier

def scheduleBreak(timeSec, breakSec, StopEvent):
    notifier.sent = False
    notifier.skip = False
    startTime = time.time()
    while time.time() - startTime <= timeSec and not StopEvent.is_set():
        StopEvent.wait(1)
        if time.time() - startTime >= timeSec - 60 and not notifier.sent and not notifier.skip:
            notifier.sendWarningNotification()

    if not StopEvent.is_set() and not notifier.skip:
        blackout.startBreak(breakSec)
    return

