import keyboard

def blockKeyboard():
    keyboard.block_key("windows")
    keyboard.block_key("alt")
    keyboard.block_key("control")

def unblockKeyboard():
    keyboard.unblock_key("windows")
    keyboard.unblock_key("alt")
    keyboard.unblock_key("control")
