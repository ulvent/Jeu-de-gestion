#Autor : Alexis Callens
from Logs import EnterLog
from Models.Ressources import *

class RessourceControler:
    def __init__(self):
        self.ListR = []
        self.ReadRessources()
        self.CheckRessourceCompany()
        EnterLog("Init Ressource Controler :: SUCCESS")

    def ReadRessources(self):
        with open("Data/Ressources.txt", "r") as File:
            data = File.readlines()
            for i in range(0, len(data)):
                ext = data[i].split(":")
                self.ListR.append(Ressources(int(ext[0]), ext[1], 0, float(ext[2])))
            File.close()
        EnterLog("ReadRessources :: SUCCESS")

    def GetRessourceForCompany(self):
        lt = []
        with open("Data/Save/Ressources.txt", "r") as File:
            data = File.readlines()
            for i in range(0, len(data)):
                ext = data[i].split(":")
                ress = self.GetRessourceByID(ext[0])
                lt.append(Ressources(int(ext[0]), ress.GetName(), int(ext[1]), ress.GetPrice()))
            File.close()
        EnterLog("Get Ressources For Company:: SUCCESS")
        return lt

    def GetRessourceByID(self, value):
        for r in self.ListR:
            if int(r.GetID()) == int(value):
                return r

    def InitRessourcesForCompany(self):
        with open("Data/Save/Ressources.txt", "a+") as File:
            for i in range(0, len(self.ListR)):
                print("Name : "+self.ListR[i].GetName())
                File.write(str(self.ListR[i].GetID())+":0")
            File.close()
        EnterLog("Init Ressources For Company :: SUCCESS")

    def CheckRessourceCompany(self):
        EnterLog("Check Company's Ressources ")
        with open("Data/Save/Ressources.txt", "r") as File:
            data = File.readlines()
            if data == []:
                self.InitRessourcesForCompany()
