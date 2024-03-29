from Controlers.RessourceControler import RessourceControler
from Models.Recipes import *
#from Views.RecipeView import *
from tkinter import *
from Logs import *
from View.RecipeView import RecipeView


class RecipeControler:
    def __init__(self, back, sc):
        self.recipe = []
        self.RV = RecipeView(self)
        self.RC =RessourceControler(back, sc)
        self.Back = back
        self.ReadFile()
        self.SC = sc
        EnterLog("Init RecipeControler")


    def ReadFile(self):
        with open("Data/Recipes.txt", encoding="windows-1252") as File:
            data = File.readlines()
            flag = -1
            for i in range(0, len(data)):
                if flag == -1:
                    ress = []
                    cost = []
                    split = data[i].split(":")
                    id = int(split[0])
                    product = split[1]
                    qt = int(split[2])
                    idm = int(split[3])
                    lvl = int(split[4])
                    flag = 0
                elif data[i] != "\n":
                    sp = data[i].split(":")
                    if flag == 0:
                        cost.append(sp[0])
                        ress.append(sp[1])
                else:
                    flag = -1
                    self.recipe.append(self.Create(id, product, qt, idm, cost, ress, lvl))
        EnterLog("Recipe Controler:: ReadFile")

    def GetRecipes(self, root):
        EnterLog("Recipe Controler :: GetRecipes")
        return self.RV.Shop(self.recipe, root)

    def Create(self, id, product, qt, idm, cost, ress, lvl):
        return Recipe(id, product, qt, idm, cost, ress, lvl)

    def CreateWithData(self, data):
        ress = []
        cost = []
        id = 0
        product = 0
        qt = 0
        idm = 0
        lvl = 0
        for i in range(0, len(data)):
            if flag == -1:
                ress = []
                cost = []
                split = data[i].split(":")
                id = int(split[0])
                product = split[1]
                qt = int(split[2])
                idm = int(split[3])
                lvl = int(split[4])
                flag = 0
            elif data[i] != "\n":
                if data[i].split("\n")[0] != "-" and flag == 0:
                    cost.append(data[i].split("\n")[0])
                elif flag == 1:
                    ress.append(data[i].split("\n")[0])
                else:
                    flag = 1
            else:
                flag = -1
        return self.Create(id, product, qt, idm, cost, ress, lvl)

    def GetRecipeById(self, id):
        for r in self.recipe:
            if r.GetID() == id:
                return r

    def GetInfo(self, value):
        for r in self.recipe:
            if r.GetID() == value:
                stg = r.GetProduct()
                stg += "\nCoût de production : "
                data = r.GetCost()
                ress = r.GetRess()
                for i in range(0, len(data)):
                    rCompany = self.RC.GetRessourceByIDForCompany(self.RC.GetRessourceForCompany(), ress[i])
                    stg += "\n"+str(data[i])+" "+self.RC.GetNameByID(ress[i])+" / "+str(rCompany.GetQuantity())
                return stg

    def GetRecipesByMachine(self, value, lvl):
        lt = []
        for r in self.recipe:
            print(r.GetProduct())
            if r.GetIDM() == value and r.GetLevel() <= lvl:
                lt.append(r)
        return self.verifRecipe(lt)

    def Retour(self):
        self.Back.Game()

    def RetourCompany(self, frame):
        self.Back.CC.GetUsine(frame)

    def AllRecipeByList(self, frame, list):
        for w in frame.winfo_children():
            w.destroy()
        self.RV.AllRecipesList(frame, list)

    def Production(self, qt, recipe):
        self.Back.Production(qt, recipe)

    def verifRecipe(self, list):
        lt = []
        searches = self.SC.GetSearches()
        for i in range(0, len(list)):
            flag = 0
            for j in range(0, len(searches)):
                if self.RC.GetIDByName(list[i].GetProduct()) == searches[j].GetIDR():
                    if searches[j].GetCheck() == 1:
                        lt.append(list[i])
                        flag =1
                    else:
                        flag = 2
            if flag == 0:
                lt.append(list[i])
        return lt

