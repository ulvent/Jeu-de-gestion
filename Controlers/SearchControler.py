import os

from Controlers.MachineControler import MachineControler
from Controlers.RessourceControler import RessourceControler
from Logs import EnterLog
from Models.Search import *
from View.SearchView import SearchView


class SearchControler:
    def __init__(self, back):
        self.Searches = []
        self.ReadSearch()
        self.Back = back
        self.MC = MachineControler(back, self)
        self.RC = RessourceControler(back, self)
        self.SV = SearchView(self)
        self.labLvl = 0
        EnterLog("Init SearchControler")

    def SetLab(self, value):
        self.labLvl = value

    def ReadSearch(self):
        with open("Data/Save/Search.txt", encoding="windows-1252") as File:
            data = File.readlines()
            for i in range(0, len(data)):
                sp = data[i].split(":")
                self.Searches.append(Search(sp[0], sp[1], sp[2], sp[3], sp[4], sp[5], sp[6]))
            File.close()
        EnterLog("SearchControler :: ReadSearch :: SUCCESS")

    def AllSearch(self, frame):
        for w in frame.winfo_children():
            w.destroy()
        if self.labLvl >= 1:
            self.SV.AllSearch(self.Searches, frame)
        else:
            self.SV.AllSearch([], frame)

    def Retour(self):
        self.Back.Game()

    def GetSearches(self):
        return self.Searches

    def GetSearchByID(self, value):
        for s in self.Searches:
            if int(s.GetID()) == int(value):
                return s

    def Buy(self, value):
        s = self.GetSearchByID(value)
        self.Back.BuySearch(s.GetPrice(), s)

    def ValidSearch(self, ids):
        s = self.GetSearchByID(ids)
        s.SetCheck()


    def WriteSearch(self):
        os.remove("Data/Save/Search.txt")
        with open("Data/Save/Search.txt", "a+", encoding="windows-1252") as File:
            for s in self.Searches:
                stg = str(s.GetID())+":"+s.GetName()+":"+str(s.GetIDM())+":"+str(s.GetIDR())+":"+str(s.GetLevel())+":"+str(s.GetPrice())+":"+str(s.GetCheck())+"\n"
                File.write(stg)
            File.close()

    def GetInfo(self, ids):
        s = self.GetSearchByID(ids)
        stg = s.GetName()
        print(s.ToString())
        stg += "\nPrix : "+str(s.GetPrice()*1.21)+"€"
        if int(s.GetIDM()) != 0:
            stg += "\nMachine débloquée : "+str(self.MC.GetNameByID(s.GetIDM()))
        else:
            stg += "\nMachine débloquée : AUCUNE"

        if int(s.GetIDR()) != 0:
            stg += "\nRessource débloquée : "+str(self.RC.GetNameByID(s.GetIDR()))
        else:
            stg += "\nRessource débloquée : AUCUNE"
        return stg

