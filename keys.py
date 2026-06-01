import keyboard
from pynput import keyboard as pynput_kb
import notifier


def blockKeyboard():
    keyboard.block_key("windows")
    keyboard.block_key("alt")
    keyboard.block_key("control")

def unblockKeyboard():
    keyboard.unblock_key("windows")
    keyboard.unblock_key("alt")
    keyboard.unblock_key("control")

def hotkeyWatcher():
    with pynput_kb.GlobalHotKeys({'<ctrl>+<shift>+s': notifier.skipNextBreak}) as h:
        h.join()