import os
import pystray
from PIL import Image



def start(stop):
    def onQuit(icon, item):
        icon.stop()
        stop()

    icon = pystray.Icon(
        name="I-Care",
        icon=Image.open(os.path.join(os.path.dirname(__file__), "eye.ico")),
        title="I-Care",
        menu=pystray.Menu(
            pystray.MenuItem("Quit", onQuit),
        )
    )

    icon.run()
    
