import os

from Logs import EnterLog
from Models.Machine import Machine
from View.MachineView import MachineView


class MachineControler:
    def __init__(self, back, sc):
        self.Machine = []
        self.Back = back
        self.MV = MachineView(self)
        self.SC =sc
        EnterLog("Init MachineControler")

    def ReadMachine(self):
        with open("Data/Save/Machine.txt", encoding="windows-1252") as File:
            data = File.readlines()
            for i in range(0, len(data)):
                sp = data[i].split(":")
                self.Machine.append(Machine(sp[0], sp[1], int(sp[2]), int(sp[3]), int(sp[4])))
            File.close()
            return self.Machine

    def GetPowerMax(self):
        pw = 0
        for m in self.Machine:
            pw += m.GetPower()
        return pw

    def GetAllMachine(self, frame):
        for w in frame.winfo_children():
            w.destroy()

        self.MV.AllMachine(frame, self.verifMachine())

    def Ameliorator(self, idm, price):
        self.Back.Upgrade(idm, price)

    def SetLevelMachine(self, idm):
        for m in self.Machine:
            if m.GetID() == idm:
                m.SetLevel(m.GetLevel() + 1)

    def WriteMachine(self):
        os.remove("Data/Save/Machine.txt")
        with open("Data/Save/Machine.txt", "a+") as File:
            for m in self.Machine:
                File.write(m.GetSaveMach())
            File.close()
        EnterLog("MachineControler :: WriteMachine :: SUCCESS")

    def GetNameByID(self, value):
        for m in self.Machine:
            if m.GetID() == int(value):
                return m.GetName()

    def GetMachine(self):
        return self.Machine

    def verifMachine(self):
        lt = []
        machines = self.Machine
        searches = self.SC.GetSearches()
        for i in range(0, len(machines)):
            flag =0
            for j in range(0, len(searches)):
                if machines[i].GetID() == searches[j].GetIDM() and int(machines[i].GetID()) != 0:
                    if searches[j].GetCheck() == 1:
                        lt.append(machines[i])
                        flag =1
                    else:
                        flag =2
            if flag == 0:
                lt.append(machines[i])
        return lt

    def GetInfo(self, idm, price):
        m = self.GetMachineByID(idm)
        stg = m.GetName()
        stg += "\nLevel : "+str(m.GetLevel())+" -> "+str(m.GetLevel()+1)
        stg += "\nEnergie : "+str(m.GetPower())+" -> "+str(m.GetPower()*2)
        stg += "\nPrix de l'amélioration : "+str(price)
        return stg

    def GetPrice(self):
        return self.Machine.GetPrice()

    def GetMachineByID(self, value):
        for m in self.Machine:
            if m.GetID() == int(value):
                return m

    def Retour(self):
        self.Back.Game()



