import ctypes
import sys


def isAdmin():
    return ctypes.windll.shell32.IsUserAnAdmin()

def launchWithAdmin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)