from Logs import EnterLog
from Models.Search import *
from View.SearchView import SearchView


class SearchControler:
    def __init__(self, back):
        self.Searches = []
        self.ReadSearch()
        self.Back = back
        self.SV = SearchView(self)
        self.labLvl = 0
        EnterLog("Init SearchControler")

    def SetLab(self, value):
        self.labLvl = value

    def ReadSearch(self):
        with open("Data/Save/Search.txt", encoding="UTF-8") as File:
            data = File.readlines()
            for i in range(1, len(data)):
                sp = data[i].split(":")
                self.Searches.append(Search(sp[0], sp[1], sp[2], sp[3], sp[4], sp[5], sp[6]))
            File.close()
        EnterLog("SearchControler :: ReadSearch :: SUCCESS")

    def AllSearch(self, frame):
        for w in frame.winfo_children():
            w.destroy()
        if self.labLvl >=1:
            self.SV.AllSearch(self.Searches, frame)
        else:
            self.SV.AllSearch([], frame)

    def Retour(self):
        self.Back.Game()

    def GetSearches(self):
        return self.Searches
