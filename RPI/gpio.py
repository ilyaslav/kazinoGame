import RPi.GPIO as GPIO
import time

class PiHandler:
    def __init__(self):
        self.initGPIO()
        self.inputs = {
            'x1': [GPIO.input(8), 8],
            'x2': [GPIO.input(10), 10],
            'x3': [GPIO.input(7), 7],
            'x4': [GPIO.input(11), 11],
            'x5': [GPIO.input(13), 13],
            'x6': [GPIO.input(15), 15],
            'x7': [GPIO.input(19), 19],
            'x8': [GPIO.input(21), 21],
            'x9': [GPIO.input(23), 23],
            'x10': [GPIO.input(29), 29],
            'x11': [GPIO.input(31), 31],
            'x12': [GPIO.input(33), 33],
            'x13': [GPIO.input(37), 37]
        }

        self.outs = {
            "y1": 3,
            "y2": 5,
            "y3": 12,
            "y4": 16,
            "y5": 18,
            "y6": 22,
            "y7": 24,
            "y8": 26,
            "y9": 32,
            "y10": 36,
            "y11": 38,
            "y12": 40
        }

    @staticmethod
    def getInputs():
        inputs = {
            'x1': GPIO.input(8),
            'x2': GPIO.input(10),
            'x3': GPIO.input(7),
            'x4': GPIO.input(11),
            'x5': GPIO.input(13),
            'x6': GPIO.input(15),
            'x7': GPIO.input(19),
            'x8': GPIO.input(21),
            'x9': GPIO.input(23),
            'x10': GPIO.input(29),
            'x11': GPIO.input(31),
            'x12': GPIO.input(33),
            'x13': GPIO.input(37)
        }
        return inputs

    def sensorsLoop(self):
        while True:
            try:
                for input in self.inputs:
                    status = GPIO.input(self.inputs[input][1])
                    if self.inputs[input][0] != status:
                        self.inputs[input][0] = status
                        self.resetInput(input, int(status))
                time.sleep(0.1)
            except:
                pass

    def initGPIO(self):
        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(8, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        GPIO.setup(10, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        GPIO.setup(7, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        GPIO.setup(11, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        GPIO.setup(13, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        GPIO.setup(15, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        GPIO.setup(19, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        GPIO.setup(21, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        GPIO.setup(29, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        GPIO.setup(31, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        GPIO.setup(33, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        GPIO.setup(37, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

        GPIO.setup(3, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(5, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(32, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(36, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(38, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(40, GPIO.OUT, initial=GPIO.LOW)

    def resetOut(self, out, status):
        if status:
            GPIO.output(self.outs[out], GPIO.HIGH)
        else:
            GPIO.output(self.outs[out], GPIO.LOW)

    def resetInput(self, input, status):
        pass