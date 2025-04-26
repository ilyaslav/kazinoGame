class TimeSettings:
    def __init__(self):
        self.time = 0
        self.timeLimit = 3600

    @staticmethod
    def getHours(time):
        hours = int(time / 3600)
        if hours < 10:
            return f'0{hours}'
        else:
            return f'{hours}'

    @staticmethod
    def getMinutes(time):
        minutes = int((time % 3600) / 60)
        if minutes < 10:
            return f'0{minutes}'
        else:
            return f'{minutes}'

    @staticmethod
    def getSeconds(time):
        seconds = time % 60
        if seconds < 10:
            return f'0{seconds}'
        else:
            return f'{seconds}'

    def getProgress(self) -> int:
        return int(self.time / self.timeLimit * 100)

    def addTime(self, time):
        self.time += int(time)

    def removeTime(self, time):
        self.time -= int(time)

    def getTime(self) -> int:
        return self.time

    def getTimeStr(self) -> str:
        return f"{self.getHours(self.time)}:{self.getMinutes(self.time)}:{self.getSeconds(self.time)}"

    def addTimeLimit(self):
        self.timeLimit += 180

    def removeTimeLimit(self):
        if self.timeLimit > 3600:
            self.timeLimit -= 180

    def getTimeLimit(self) -> int:
        return self.timeLimit

    def getTimeLimitStr(self) -> str:
        return f"{self.getHours(self.timeLimit)}:{self.getMinutes(self.timeLimit)}:{self.getSeconds(self.timeLimit)}"

    def initTime(self):
        self.time = 0
        self.timeLimit = 3600
