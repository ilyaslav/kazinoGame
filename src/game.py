import threading
from enum import Enum, IntEnum
from time import sleep

from server import Server
from blinker import Blinker
from singleTimer import SingleTimer
from timeSettings import TimeSettings


class Times(IntEnum):
    T1 = 2
    T2 = 1
    T3 = 3
    T4 = 2
    T5 = 1
    T6 = 1
    T7 = 3
    T8 = 1
    T9 = 10
    T10 = 5
    T11 = 1
    T12 = 2
    T13 = 4
    T14 = 2


class GameStatus(Enum):
    NOT_READY = "Квест не собран"
    READY = "Квест собран"
    LAUNCHED = "Квест запущен"
    FINISHED = "Квест окончен"


class WaitingStatus(Enum):
    NOT_READY = "notReady"
    READY = "ready"
    BLOCKED = "blocked"


class Track(Enum):
    TRACK1 = "Трек №1  «Проникновение»"
    TRACK2 = "Трек №2  «Фон»"
    TRACK3 = "Трек №3  «Замок»"
    TRACK4 = "Трек №4  «Сирена»"
    TRACK5 = "Трек №5  «Победа»"
    TRACK6 = "Трек №6  «Поражение»"
    TRACK7 = "Трек №7  «Alarm»"


class Game:
    def __init__(self):
        self.timeSettings = TimeSettings()
        self.server = Server()
        threading.Thread(target=lambda: self.server.serverFunction(self.messageHandler), daemon=True).start()

        self.inputs = {
            "x1": False,
            "x2": False,
            "x3": False,
            "x4": False,
            "x5": False,
            "x6": False,
            "x7": False,
            "x8": False,
            "x9": False,
            "x10": False,
            "x11": False,
            "x12": False,
            "x13": False,
            "roulette": False,
            "map": False
        }

        self.outs = {
            "y1": False,
            "y2": False,
            "y3": False,
            "y4": False,
            "y5": False,
            "y6": False,
            "y7": False,
            "y8": False,
            "y9": False,
            "y10": False,
            "y11": False,
            "y12": False
        }

        self.stages = {
            "box": False,
            "roulette": False,
            "map": False,
            "bottle": False,
            "phone": False,
            "door": False,
        }

        self.settings = {
            "gameStatus": GameStatus.NOT_READY,
            "startEvent": False,
            "winEvent": False,
            "defeatEvent": False,
            "waitingStatus": WaitingStatus.NOT_READY,
            "doorLock": False,
            "volume": 100
        }

        self.music = {
            Track.TRACK1.value: 1,
            Track.TRACK2.value: 2,
            Track.TRACK3.value: 3,
            Track.TRACK4.value: 4,
            Track.TRACK5.value: 5,
            Track.TRACK6.value: 6,
            Track.TRACK7.value: 7,
        }

        self.tasks = {
            "questScript": SingleTimer(self.questScript),
            "defaultScriptY2": SingleTimer(lambda: self.defaultScript("y2")),
            "defaultScriptY3": SingleTimer(lambda: self.defaultScript("y3")),
            "defaultScriptY4": SingleTimer(lambda: self.defaultScript("y4")),
            "defaultScriptY5": SingleTimer(lambda: self.defaultScript("y5")),
            "activateY10": SingleTimer(lambda: self.activateOut("y10"), Times.T9.value),
            "deactivateY8": SingleTimer(lambda: self.deactivateOut("y8"), Times.T12.value),
            "deactivateY11": SingleTimer(lambda: self.deactivateOut("y11"), Times.T10.value),
            "blinkY10": Blinker(lambda: self.blinkOuts(["y10"]), Times.T9.value),
            "blinkY1": Blinker(lambda: self.blinkOuts(["y1"])),
            "blinkY2345": Blinker(lambda: self.blinkOuts(["y2","y3","y4","y5"])),
        }

    def messageHandler(self, message: str):
        inputName, value = message.split(':')
        self.inputs[inputName] = bool(int(value))
        if self.inputs[inputName]:
            if inputName == "x1" and self.checkStart():
                self.settings["startEvent"] = True
            elif inputName == "x2":
                self.boxScript()
            elif inputName in ["x3", "x4", "x5", "x6"] and self.checkRoulette():
                self.rouletteScript()
            elif inputName in ["x7", "x8", "x9", "x10"] and self.checkMap():
                self.mapScript()
            elif inputName == "x11":
                self.bottleScript()
            elif inputName == "x12":
                self.phoneScript()
            elif inputName == "x13":
                self.doorScript()
        else:
            if inputName == "x1"  and self.checkWin():
                self.settings["winEvent"] = True

    def playMusic(self, name: str):
        track = self.music[name]
        self.server.send_message(f'play:{track};')

    def alarm(self):
        self.server.send_message(f'play:7;')

    def pauseMusic(self, name: str):
        track = self.music[name]
        self.server.send_message(f'pause:{track};')

    def stopMusic(self, name: str):
        track = self.music[name]
        self.server.send_message(f'stop:{track};')

    def changeVolume(self, volume: int):
        self.settings["volume"] = volume
        self.server.send_message(f'volume:{volume};')

    def resetOut(self, outName: str):
        if self.outs[outName]:
            self.server.send_message(f'{outName}:1;')
        else:
            self.server.send_message(f'{outName}:0;')

    def activateOut(self, outName: str):
        self.outs[outName] = True
        self.resetOut(outName)
        if outName == "y8":
            self.tasks["deactivateY8"].start()
        elif outName == "y11":
            self.tasks["deactivateY11"].start()

    def deactivateOut(self, outName: str):
        self.outs[outName] = False
        self.resetOut(outName)

    def deactivateOuts(self):
        for out in self.outs:
            self.deactivateOut(out)

    def checkState(self):
        game = GameStatus.READY
        waiting = WaitingStatus.NOT_READY
        for inputName in self.inputs:
            if self.inputs[inputName]:
                game = GameStatus.NOT_READY
                waiting = WaitingStatus.NOT_READY
        self.settings["gameStatus"] = game
        self.settings["waitingStatus"] = waiting

    def stopTasks(self):
        for task in self.tasks:
            self.tasks[task].stop()

    def stopAllMusic(self):
        for track in self.music:
            self.server.send_message(f'stop:{self.music[track]};')

    def initGame(self):
        self.stopTasks()
        self.settings["doorLock"] = False
        self.stages = {
            "box": False,
            "roulette": False,
            "map": False,
            "bottle": False,
            "phone": False,
            "door": False,
        }
        self.deactivateOuts()
        self.checkState()
        self.timeSettings.initTime()
        self.stopAllMusic()

    def checkStart(self):
        return not self.settings["doorLock"] and self.settings["waitingStatus"] == WaitingStatus.READY

    def startGame(self):
        self.settings["startEvent"] = False
        self.settings["gameStatus"] = GameStatus.LAUNCHED
        self.settings["waitingStatus"] = WaitingStatus.BLOCKED
        self.playMusic(Track.TRACK1.value)

    def activateStage(self, stage: str):
        activationScript = {
            "box": self.boxScript,
            "roulette":  self.rouletteScript,
            "map":  self.mapScript,
            "bottle":  self.bottleScript,
            "phone":  self.phoneScript,
            "door":  self.doorScript,
        }
        activationScript[stage]()

    def boxScript(self):
        if self.stages["box"]:
            return
        self.stages["box"] = True

        self.activateOut("y1")
        self.stopMusic(Track.TRACK1.value)
        self.playMusic(Track.TRACK2.value)

    def checkRoulette(self):
        return all(self.inputs.get(f"x{i}") for i in range(3, 7))

    def rouletteScript(self):
        if self.stages["roulette"]:
            return
        self.stages["roulette"] = True

        if self.checkQuest():
            self.tasks["questScript"].start()
        else:
            self.tasks["defaultScriptY2"].start()

    def checkMap(self):
        return all(self.inputs.get(f"x{i}") for i in range(7, 11))

    def mapScript(self):
        if self.stages["map"]:
            return
        self.stages["map"] = True

        if self.checkQuest():
            self.tasks["questScript"].start()
        else:
            self.tasks["defaultScriptY3"].start()

    def bottleScript(self):
        if self.stages["bottle"]:
            return
        self.stages["bottle"] = True

        if self.checkQuest():
            self.tasks["questScript"].start()
        else:
            self.tasks["defaultScriptY4"].start()

    def phoneScript(self):
        if self.stages["phone"]:
            return
        self.stages["phone"] = True

        if self.checkQuest():
            self.tasks["questScript"].start()
        else:
            self.tasks["defaultScriptY5"].start()

    def doorScript(self):
        if self.stages["door"]:
            return
        self.stages["door"] = True
        self.stopMusic(Track.TRACK4.value)
        self.playMusic(Track.TRACK2.value)
        self.activateOut("y1")
        self.activateOut("y2")
        self.activateOut("y3")
        self.activateOut("y4")
        self.activateOut("y5")
        self.deactivateOut("y7")
        self.deactivateOut("y9")
        self.tasks["blinkY10"].start()
        self.tasks["activateY10"].start()

    def checkWin(self):
        return all(self.stages.values())

    def winScript(self):
        if self.settings["gameStatus"] != GameStatus.LAUNCHED:
            return
        self.settings["winEvent"] = False
        self.settings["gameStatus"] = GameStatus.FINISHED
        self.stopMusic(Track.TRACK2.value)
        self.playMusic(Track.TRACK5.value)
        self.deactivateOut("y1")

    def defeatScript(self):
        if self.settings["gameStatus"] != GameStatus.LAUNCHED:
            return
        self.settings["defeatEvent"] = False
        self.settings["gameStatus"] = GameStatus.FINISHED
        self.stopMusic(Track.TRACK2.value)
        self.playMusic(Track.TRACK6.value)
        self.tasks["blinkY1"].start()

    def checkQuest(self):
        return all(self.stages[key] for key in ("roulette", "map", "bottle", "phone"))

    def questScript(self):
        self.pauseMusic(Track.TRACK2.value)
        self.playMusic(Track.TRACK3.value)
        self.deactivateOut("y1")
        self.activateOut("y12")
        sleep(Times.T3.value)
        self.activateOut("y8")
        sleep(Times.T4.value)
        self.stopMusic(Track.TRACK3.value)
        self.deactivateOut("y8")
        self.tasks["blinkY2345"].start()
        sleep(Times.T13.value)
        self.activateOut("y6")
        self.activateOut("y7")
        sleep(Times.T14.value)
        self.playMusic(Track.TRACK4.value)
        self.activateOut("y9")
        self.deactivateOut("y12")

    def defaultScript(self, outName: str):
        self.pauseMusic(Track.TRACK2.value)
        self.playMusic(Track.TRACK3.value)
        self.deactivateOut("y1")
        self.activateOut("y12")
        sleep(Times.T3.value)
        self.activateOut(outName)
        sleep(Times.T4.value)
        self.activateOut("y1")
        self.deactivateOut("y12")
        self.stopMusic(Track.TRACK3.value)
        self.playMusic(Track.TRACK2.value)

    def lockDoor(self):
        self.settings["doorLock"] = not self.settings["doorLock"]

    def blinkOuts(self, outs):
        for outName in outs:
            self.outs[outName] = not self.outs[outName]
            self.resetOut(outName)