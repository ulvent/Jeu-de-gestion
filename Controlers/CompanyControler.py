#Autor : Alexis Callens
from Logs import EnterLog
import os
from Models.Company import Company


class CompanyControler:
    def __init__(self, rc):
        self.Company = 0
        self.RC = rc

        self.SetCompany()
        EnterLog("Init Company Controler :: SUCCESS")

    def SetCompany(self):
        ress = self.RC.GetRessourceForCompany()
        with open("Data/Save/Company.txt", "r") as File:
            data = File.readlines()
            if data == []:
                EnterLog("New Company")
                self.Company = Company("Optimisation.Inc", 1500, 10, 0, 1, 0, 1, 1, ress)
                File.close()
                self.SaveCompany()
            else:
                EnterLog("Company exist")
                Name = data[0].split("\n")[0]
                Money = float(data[1].split("\n")[0])
                Employe = int(data[2].split("\n")[0])
                Power = int(data[3].split("\n")[0])
                Storage = int(data[4].split("\n")[0])
                Laboratory = int(data[5].split("\n")[0])
                Factory = int(data[6].split("\n")[0])
                Generator = int(data[7].split("\n")[0])
                self.Company = Company(Name, Money, Employe, Power, Storage, Laboratory, Factory, Generator, ress)
            File.close()
        EnterLog("SetCompany :: SUCCESS")

    def GetName(self):
        return self.Company.GetName()

    def GetToString(self):
        return self.Company.ToString()

    def GetRessources(self):
        return self.Company.GetRess()

    def GetStorage(self):
        return self.Company.GetStorage()

    def GetMoney(self):
        return self.Company.GetMoney()

    def GetEmployes(self):
        return self.Company.GetEmployes()

    def GetGenerator(self):
        return self.Company.GetGenerator()

    def GetPower(self):
        return self.Company.GetPower()

    def GetMaxPower(self):
        return self.Company.GetMaxPower()

    def SetMoney(self, value):
        self.Company.SetMoney(value)

    def SetRessources(self, value):
        self.Company.SetRessources(value)

    def GetStorageQuantity(self):
        st = 0
        for r in self.GetRessources():
            st += r.GetQuantity()
        return st

    def WriteRessources(self):
        os.remove("Data/Save/Ressources.txt")
        with open("Data/Save/Ressources.txt", "a+") as File:
            for r in self.GetRessources():
                File.write(str(r.GetID())+":"+str(r.GetQuantity())+"\n")
            File.close()

    def SaveCompany(self):
        os.remove("Data/Save/Company.txt")
        with open("Data/Save/Company.txt", "a+") as File:
            File.write(self.Company.GetSave())
            File.close()
