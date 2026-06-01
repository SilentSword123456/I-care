import time
import balckout
import notify

def scheduleBreak(timeSec, breakSec, StopEvent):
    elapsed = 0
    while elapsed <= timeSec and not StopEvent.is_set():
        StopEvent.wait(1)
        elapsed = elapsed + 1
        if timeSec - 60 == elapsed:
            notify.sendWarningNotification()

    if not StopEvent.is_set():
        balckout.startBreak(breakSec)
    return

