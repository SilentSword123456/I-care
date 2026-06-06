import json


class Config:
    def __init__(self):
        self.hotkey="<ctrl>+<shift>+s"
        self.breakSec=20
        self.workSec=20*60
        self.adminGranted=False

    def writeConfig(self):
        try:
            with open('config.json', 'w') as outfile:
                json.dump({
                    "hotkey": self.hotkey,
                    "breakSec": self.breakSec,
                    "workSec": self.workSec,
                    "adminGranted": self.adminGranted
                }, outfile)
        except:
             raise IOError("Unable to write to config.json")



    def loadConfig(self):
        try:
            with open('config.json') as json_file:
                data = json.load(json_file)
                self.breakSec=data['breakSec']
                self.workSec=data['workSec']
                self.adminGranted=data['adminGranted']
                self.hotkey=data['hotkey']
        except FileNotFoundError:
            self.writeConfig()

    def updateHotkey(self, hotkey):
        self.hotkey=hotkey
    def updateBreakTime(self, breakTime):
        if breakTime > 0:
            self.breakSec=breakTime
    def updateWorkTime(self, workTime):
        if workTime > 0:
            self.workSec=workTime
    def setAdminGranted(self, adminGranted):
        self.adminGranted=adminGranted
