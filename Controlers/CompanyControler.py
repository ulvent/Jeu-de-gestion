#Autor : Alexis Callens
from Logs import EnterLog
from Models.Company import Company


class CompanyControler:
    def __init__(self, rc):
        self.Company = 0
        self.RC = rc

        self.SetCompany()
        EnterLog("Init Company Controler :: SUCCESS")

    def SetCompany(self):
        ress = self.RC.GetRessourceForCompany()
        with open("Data/Save/Company", "a+") as File:
            data = File.readlines()
            if data == []:
                self.Company = Company("Optimisation.Inc", 1500, 10, 0, 1, 0, 1, 1, ress)
            else:
                data = File.readlines()
                Name = data[0].split("\n")[0]
                Money = float(data[1].split("\n")[0])
                Employe = int(data[2].split("\n")[0])
                PowerMax = int(data[3].split("\n")[0])
                Power = int(data[4].split("\n")[0])
                Storage = int(data[5].split("\n")[0])
                Laboratory = int(data[6].split("\n")[0])
                Factory = int(data[7].split("\n")[0])
                Generator = int(data[0].split("\n")[0])
                self.Company = Company(Name, Money, Employe, Power, Storage, Laboratory, Factory, Generator, ress)
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