#Autor : Alexis Callens
from Logs import EnterLog

class Company:
    def __init__(self, name, money, st, lab, gen, ress, machine):
        self.Name = name
        self.Money = money
        #batiments
        self.BAT_Storage = st
        self.BAT_Laboratory = lab
        self.BAT_Generator = gen

        self.Ressources = ress
        self.Machines = machine
        EnterLog("Init Company")

    def GetName(self):
        return self.Name

    def ToString(self):
        stg = "Entrepôt : "+str(self.BAT_Storage)
        stg += "\nLaboratoire : "+str(self.BAT_Laboratory)
        stg += "\nGénérateur : "+str(self.BAT_Generator)
        return stg

    def GetRess(self):
        return self.Ressources

    def GetMachines(self):
        return self.Machines

    def GetStorage(self):
        return self.BAT_Storage

    def GetMoney(self):
        return float(self.Money)

    def GetGenerator(self):
        return self.BAT_Generator

    def GetMaxPower(self):
        return int(self.BAT_Generator)*50

    def SetMoney(self, value):
        self.Money = value

    def SetRessources(self, value):
        self.Ressources = value

    def SetMachine(self, value):
        self.Machines = value

    def SetGenerator(self, value):
        self.BAT_Generator = value

    def SetLabo(self, value):
        self.BAT_Laboratory = value

    def SetStock(self, value):
        self.BAT_Storage = value

    def GetLabo(self):
        return int(self.BAT_Laboratory)

    def GetSave(self):
        chaine = self.Name+"\n"
        chaine += str(self.Money)+"\n"
        chaine += str(self.BAT_Storage)+"\n"
        chaine += str(self.BAT_Laboratory)+"\n"
        chaine += str(self.BAT_Generator)+"\n\n"
        return chaine
