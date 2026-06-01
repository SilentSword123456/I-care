import os
from win11toast import toast

sent = False
skip = False

def skipNextBreak(args=None):
    global skip
    skip = True
    print("Skip break!")

def sendWarningNotification():
    global sent
    toast(
        "I Care - You have one more minute until your break!",
        icon=os.path.join(os.path.dirname(os.path.abspath(__file__)), "eye.ico"),
        button="Skip this one",
        on_click=skipNextBreak
    )
    sent = True

if __name__ == "__main__":
    sendWarningNotification()