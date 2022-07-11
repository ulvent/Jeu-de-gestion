from Models.Recipes import *
#from Views.RecipeView import *
from tkinter import *
from Logs import *
from View.RessourceView import RessourceView


class RecipeControler:
    def __init__(self):
        self.recipe = []
        self.RV = RessourceView(self)
        self.ReadFile()
        EnterLog("Init RecipeControler")


    def ReadFile(self):
        with open("Data/Recipes.txt") as File:
            data = File.readlines()
            flag = -1
            for i in range(0, len(data)):
                if flag == -1:
                    ress = []
                    cost = []
                    split = data[i].split(":")
                    id = int(split[0])
                    name = split[1]
                    product = split[2]
                    qt = int(split[3])
                    idm = int(split[4])
                    flag = 0
                elif data[i] != "\n":
                    sp = data[i].split(":")
                    if flag == 0:
                        cost.append(sp[0])
                        ress.append(sp[1])
                else:
                    flag = -1
                    self.recipe.append(self.Create(id, name, product, qt, idm, cost, ress))
        EnterLog("Recipe Controler:: ReadFile")

    def GetRecipes(self, root):
        EnterLog("Recipe Controler :: GetRecipes")
        return self.RV.Shop(self.recipe, root)

    def Create(self, id, name, product, qt, idm, cost, ress):
        return Recipe(id, name, product, qt, idm, cost, ress)

    def CreateWithData(self, data):
        ress = []
        cost = []
        id = 0
        name = ""
        product = 0
        qt = 0
        idm = 0
        for i in range(0, len(data)):
            if flag == -1:
                ress = []
                cost = []
                split = data[i].split(":")
                id = int(split[0])
                name = split[1]
                product = split[2]
                qt = int(split[3])
                idm = int(split[4])
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
        return self.Create(id, name, product, qt, idm, cost, ress)

    def GetRecipeById(self, id):
        for r in self.recipe:
            if r.GetID() == id:
                return r

    def GetInfo(self, value):
        for r in self.recipe:
            if r.GetID() == value:
                return r.Tostring()