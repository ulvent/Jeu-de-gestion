from Logs import EnterLog
from Models.Machine import Machine


class MachineControler:
    def __init__(self):
        self.Machine = []
        EnterLog("Init MachineControler")

    def ReadMachine(self):
        with open("Data/Save/Machine.txt") as File:
            data = File.readlines()
            for i in range(0, len(data)):
                sp = data[i].split(":")
                self.Machine.append(Machine(sp[0], sp[1], int(sp[2]), int(sp[3])))
            File.close()
            return self.Machine

    def GetPowerMax(self):
        pw = 0
        for m in self.Machine:
            pw += m.GetPower()
        return pw

