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
    T9 = 15
    T10 = 5
    T11 = 1
    T12 = 2
    T13 = 4
    T14 = 2
    T15 = 2


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
            "volume": 100,
            "skipStage": False
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
            "startGame": SingleTimer(self.startGameScript),
            "box": SingleTimer(self.boxScript),
            "roulette": SingleTimer(self.rouletteScript),
            "map": SingleTimer(self.mapScript),
            "bottle": SingleTimer(self.bottleScript),
            "phone": SingleTimer(self.phoneScript),
            "door": SingleTimer(self.doorScript),
            "activateY10": SingleTimer(lambda: self.activateOut("y10"), Times.T9.value),
            "deactivateY8": SingleTimer(lambda: self.deactivateOut("y8"), Times.T12.value),
            "deactivateY11": SingleTimer(lambda: self.deactivateOut("y11"), Times.T10.value),
            "blinkY10": Blinker(lambda: self.blinkOuts(["y10"]), Times.T9.value),
            "blinkY1": Blinker(lambda: self.blinkOuts(["y1"])),
            "blinkY2345": Blinker(lambda: self.blinkOuts(["y2","y3","y4","y5"])),
        }

        self.onlineInputsList = [
            "x1",
            "x3",
            "x4",
            "x5",
            "x6",
            "x7",
            "x8",
            "x9",
            "x10",
        ]

    def messageHandler(self, message: str):
        inputName, value = message.split(':')
        if inputName not in self.inputs.keys() or inputName == "x1" and self.settings["doorLock"]:
            return

        self.inputs[inputName] = bool(int(value))
        if self.inputs[inputName]:
            if inputName == "x1" and self.checkStart():
                self.tasks["startGame"].start()
            elif inputName == "x2":
                self.tasks["box"].start()
            elif inputName in ["x3", "x4", "x5", "x6"] and self.checkRoulette():
                self.tasks["roulette"].start()
            elif inputName in ["x7", "x8", "x9", "x10"] and self.checkMap():
                self.tasks["map"].start()
            elif inputName == "x11":
                self.tasks["bottle"].start()
            elif inputName == "x12":
                self.tasks["phone"].start()
            elif inputName == "x13":
                self.tasks["door"].start()
        else:
            if inputName == "x1"  and self.checkWin():
                self.settings["winEvent"] = True
            elif inputName == "x1":
                self.tasks["startGame"].stop()

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
        if not self.checkMap():
            self.inputs["map"] = False
        if not self.checkRoulette():
            self.inputs["roulette"] = False
        self.deactivateOuts()
        self.checkState()
        self.timeSettings.initTime()
        self.stopAllMusic()
        self.activateOut("y11")

    def startGameScript(self):
        sleep(Times.T15.value)
        if self.checkStart():
            self.settings["startEvent"] = True

    def checkStart(self):
        return not self.settings["doorLock"] and self.settings["waitingStatus"] == WaitingStatus.READY

    def checkStartScript(self, scriptName: str):
       return not self.stages[scriptName] and self.settings["gameStatus"] == GameStatus.LAUNCHED

    def startGame(self):
        self.settings["startEvent"] = False
        self.settings["gameStatus"] = GameStatus.LAUNCHED
        self.settings["waitingStatus"] = WaitingStatus.BLOCKED
        self.playMusic(Track.TRACK1.value)

    def activateStage(self, stage: str):
        self.settings["skipStage"] = True
        self.tasks[stage].start()

    def boxScript(self):
        if not self.checkStartScript("box"):
            return
        if self.settings["skipStage"]:
            self.settings["skipStage"] = False
        self.stages["box"] = True

        self.activateOut("y1")
        self.stopMusic(Track.TRACK1.value)
        self.playMusic(Track.TRACK2.value)

    def checkRoulette(self):
        return all(self.inputs.get(f"x{i}") for i in range(3, 7))

    def rouletteScript(self):
        if not self.checkStartScript("roulette"):
            return
        if self.settings["skipStage"]:
            self.settings["skipStage"] = False
        else:
            sleep(Times.T2.value)
        self.stages["roulette"] = True
        self.inputs["roulette"] = True

        if self.checkQuest():
            self.questScript()
        else:
            self.defaultScript("y2")

    def checkMap(self):
        return all(self.inputs.get(f"x{i}") for i in range(7, 11))

    def mapScript(self):
        if not self.checkStartScript("map"):
            return
        if self.settings["skipStage"]:
            self.settings["skipStage"] = False
        else:
            sleep(Times.T5.value)
        self.stages["map"] = True
        self.inputs["map"] = True

        if self.checkQuest():
            self.questScript()
        else:
            self.defaultScript("y3")

    def bottleScript(self):
        if not self.checkStartScript("bottle"):
            return
        if self.settings["skipStage"]:
            self.settings["skipStage"] = False
        else:
            sleep(Times.T6.value)
        self.stages["bottle"] = True

        if self.checkQuest():
            self.questScript()
        else:
            self.defaultScript("y4")

    def phoneScript(self):
        if not self.checkStartScript("phone"):
            return
        if self.settings["skipStage"]:
            self.settings["skipStage"] = False
        else:
            sleep(Times.T7.value)
        self.stages["phone"] = True

        if self.checkQuest():
            self.questScript()
        else:
            self.defaultScript("y5")

    def doorScript(self):
        if not self.checkStartScript("door"):
            return
        if self.settings["skipStage"]:
            self.settings["skipStage"] = False
        self.stages["door"] = True
        self.tasks["blinkY2345"].stop()
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
        self.deactivateOut("y2")
        self.deactivateOut("y3")
        self.deactivateOut("y4")
        self.deactivateOut("y5")
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