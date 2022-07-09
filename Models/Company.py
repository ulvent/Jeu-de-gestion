#Autor : Alexis Callens
from Logs import EnterLog

class Company:
    def __init__(self, name, money, employes, pw, st, lab, fact, gen,ress):
        self.Name = name
        self.Money = money
        self.Employes = employes
        self.PowerMax = gen*50
        self.Power = pw
        #batiments
        self.BAT_Storage = st
        self.BAT_Laboratory = lab
        self.BAT_Factory = fact
        self.BAT_Generator = gen

        self.Ressources = ress
        EnterLog("Init Company")

    def GetName(self):
        return self.Name

    def ToString(self):
        stg = "Entrepôt : "+str(self.BAT_Storage)
        stg += "\nLaboratoire : "+str(self.BAT_Laboratory)
        stg += "\nUsine : "+str(self.BAT_Factory)
        stg += "\nGénérateur : "+str(self.BAT_Generator)
        return stg

    def GetRess(self):
        return self.Ressources

    def GetStorage(self):
        return self.BAT_Storage

    def GetMoney(self):
        return self.Money

    def GetEmployes(self):
        return self.Employes

    def GetGenerator(self):
        return self.BAT_Generator

    def GetPower(self):
        return self.Power

    def GetMaxPower(self):
        return self.PowerMax

