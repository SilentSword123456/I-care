import tkinter as tk
from keys import blockKeyboard, unblockKeyboard
import screeninfo

monitors = screeninfo.get_monitors()


def startBreak(timeSec):
    blackoutScreen(timeSec)

def countdown(root, label, remaining):
    if remaining <= 0:
        root.destroy()
        return
    label.config(text=f"{remaining} seconds remaining")
    root.after(1000, countdown, root, label, remaining - 1)

def addAllMonitors(root):
    for monitor in monitors[1:]:
        win = tk.Toplevel(root)
        win.geometry(f"{monitor.width}x{monitor.height}+{monitor.x}+{monitor.y}")
        win.configure(bg="black")
        win.overrideredirect(True)


def blackoutScreen(timeSec):
    root = tk.Tk()

    root.geometry(f"{monitors[0].width}x{monitors[0].height}+{monitors[0].x}+{monitors[0].y}")
    root.configure(bg="black")
    root.overrideredirect(True)

    addAllMonitors(root)

    label = tk.Label(root, fg="white", bg="black", font=("Arial", 48))
    label.pack()

    blockKeyboard()

    countdown(root, label, remaining=timeSec)
    root.mainloop()

    unblockKeyboard()

if __name__ == "__main__":
    startBreak(10)