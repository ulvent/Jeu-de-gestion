#Autor : Alexis Callens
from Logs import EnterLog
import os
from Models.Company import Company
from View.CompanyView import CompanyView


class CompanyControler:
    def __init__(self, rc, mc, back, sc):
        self.Company = 0
        self.CV = CompanyView(self, back, sc)
        self.RC = rc
        self.MC = mc
        self.Back = back
        self.SC = sc

        self.SetCompany()
        EnterLog("Init Company Controler :: SUCCESS")

    def SetCompany(self):
        ress = self.RC.GetRessourceForCompany()
        mach = self.MC.ReadMachine()
        with open("Data/Save/Company.txt", "r") as File:
            data = File.readlines()
            if data == []:
                EnterLog("New Company")
                self.Company = Company("Optimisation.Inc", 1500,  1, 0, 1, 1, ress, mach)
                File.close()
                self.SaveCompany()
            else:
                EnterLog("Company exist")
                Name = data[0].split("\n")[0]
                Money = float(data[1].split("\n")[0])
                Storage = int(data[2].split("\n")[0])
                Laboratory = int(data[3].split("\n")[0])
                Factory = int(data[4].split("\n")[0])
                Generator = int(data[5].split("\n")[0])
                self.Company = Company(Name, Money, Storage, Laboratory, Factory, Generator, ress, mach)
            File.close()
        EnterLog("SetCompany :: SUCCESS")

    def GetName(self):
        return self.Company.GetName()

    def GetLabo(self):
        return self.Company.GetLabo()

    def GetToString(self):
        return self.Company.ToString()

    def GetRessources(self):
        return self.Company.GetRess()

    def GetStorage(self):
        return self.Company.GetStorage()

    def GetMoney(self):
        return self.Company.GetMoney()

    def GetGenerator(self):
        return self.Company.GetGenerator()

    def GetMaxPower(self):
        return self.Company.GetMaxPower()

    def SetMoney(self, value):
        self.Company.SetMoney(value)

    def SetRessources(self, value):
        self.Company.SetRessources(value)

    def GetMachines(self):
        return self.Company.GetMachines()

    def SetMachine(self, value):
        self.Company.SetMachine(value)

    def GetStorageQuantity(self):
        st = 0
        for r in self.GetRessources():
            st += r.GetQuantity()
        return st

    def WriteRessources(self):
        os.remove("Data/Save/Ressources.txt")
        with open("Data/Save/Ressources.txt", "a+", encoding="UTF-8") as File:
            for r in self.GetRessources():
                File.write(str(r.GetID())+":"+str(r.GetQuantity())+"\n")
            File.close()

    def SaveCompany(self):
        os.remove("Data/Save/Company.txt")
        with open("Data/Save/Company.txt", "a+") as File:
            File.write(self.Company.GetSave())
            File.close()

    def Retour(self):
        self.Back.Game()

    def GetUsine(self, frame):
        for w in frame.winfo_children():
            w.destroy()
        self.verifMachine()
        self.CV.GetUsine(frame, self.GetMachines())

    def verifMachine(self):
        lt = []
        machines = self.GetMachines()
        searches = self.SC.GetSearches()
        for i in range(0, len(machines)):
            flag =0
            for j in range(0, len(searches)):
                if machines[i].GetID() == searches[j].GetIDM():
                    if searches[j].GetCheck() == 1:
                        lt.append(machines[i])
                        flag =1
                    else:
                        flag =2
            if flag == 0:
                lt.append(machines[i])
        self.SetMachine(lt)

    def SetGenerateur(self, value):
        self.Company.SetGenerator(value)

    def SetLabo(self, value):
        self.Company.SetLabo(value)
