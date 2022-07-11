#Autor : Alexis Callens
from Logs import EnterLog
from Models.Ressources import *
from View.RessourceView import RessourceView


class RessourceControler:
    def __init__(self, backup):
        self.ListR = []
        self.ReadRessources()
        self.CheckRessourceCompany()
        self.RV = RessourceView(self)
        self.Back = backup
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

    def SetQuantityForCompany(self, id, value, list):
        for r in list:
            if int(r.GetID()) == int(id):
                r.SetQuantity(value+r.GetQuantity())
                return list


    def InitRessourcesForCompany(self):
        with open("Data/Save/Ressources.txt", "a+") as File:
            for i in range(0, len(self.ListR)):
                print("Name : "+self.ListR[i].GetName())
                File.write(str(self.ListR[i].GetID())+":0\n")
            File.close()
        EnterLog("Init Ressources For Company :: SUCCESS")

    def CheckRessourceCompany(self):
        EnterLog("Check Company's Ressources ")
        with open("Data/Save/Ressources.txt", "r") as File:
            data = File.readlines()
            if data == []:
                self.InitRessourcesForCompany()
            else:
                EnterLog("Check Company's Ressources :: Exist")

    def GetShop(self, frame):
        for w in frame.winfo_children():
            w.destroy()
        self.RV.Shop(self.ListR, frame)

    def GetInfo(self, value):
        r = self.GetRessourceByID(value)
        chaine = r.GetName()+"\nPrix TTC : "+str(round(r.GetPrice()*1.21, 2))+"€/unité"
        return chaine

    def Retour(self):
        self.Back.Game()

    def Buy(self, qt, value):
        r = self.GetRessourceByID(value)
        impPrice = round(r.GetPrice() * qt.get())
        TVA = round((impPrice / 100) * 21, 2)
        TotalPrice = impPrice+TVA
        print("Prix total : "+str(TotalPrice)+"€")
        self.Back.Buy(TotalPrice, r, qt.get())

    def GetStorage(self, frame, list):
        for w in frame.winfo_children():
            w.destroy()
        self.RV.GetStorage(frame, list)
