import threading

from client import Client
from music import Music
from gpio import PiHandler


class GameHandler(PiHandler):
    def __init__(self):
        super().__init__()
        self.client = Client(self.sendInputs)
        self.gm = Music()

    def messageHandler(self, message: str):
        m1, m2 =  message.split(":")
        if m1 == 'play':
            self.gm.play(m2)
        elif m1 == 'stop':
            self.gm.stop(m2)
        elif m1 == 'pause':
            self.gm.pause(m2)
        elif m1 == 'volume':
            self.gm.changeVolume(int(m2))
        else:
            self.resetOut(m1, int(m2))

    def resetInput(self, input, status):
        self.client.sendMessage(f'{input}:{status};')

    def sendInputs(self):
        inputs = PiHandler.getInputs()
        for inputName in inputs:
            self.client.sendMessage(f'{inputName}{int(inputs[inputName])};')


def main():
    gh = GameHandler()
    threading.Thread(target=gh.client.clientFunction, daemon=True).start()
    gh.sensorsLoop()


if __name__ == '__main__':
    main()