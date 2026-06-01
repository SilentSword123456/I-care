import time

import balckout
import notify

def scheduleBreak(timeSec, breakSec, StopEvent):
    notify.sent = False
    startTime = time.time()
    while time.time() - startTime <= timeSec and not StopEvent.is_set():
        StopEvent.wait(1)
        if time.time() - startTime >= timeSec - 60 and not notify.sent:
            notify.sendWarningNotification()

    if not StopEvent.is_set():
        balckout.startBreak(breakSec)
    return

