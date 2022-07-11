#Autor : Alexis Callens
from tkinter import *

from Controlers.BillControler import BillControler
from Controlers.CompanyControler import *
from Controlers.RecipeControler import RecipeControler
from Controlers.RessourceControler import *

from Logs import *

class Management:
    def __init__(self):
        EnterLog("Game :: Init")
        self.Root = Tk()
        self.ContentFrame = Frame(self.Root)
        self.Rframe = Frame(self.ContentFrame, relief=SUNKEN, bd=2)
        self.Lframe = Frame(self.ContentFrame, relief=SUNKEN, bd=2)
        self.Tframe = Frame(self.ContentFrame, relief=SUNKEN, bd=2)

        #Controlers
        self.RC = RessourceControler(self)
        self.CC = CompanyControler(self.RC)
        self.RCC = RecipeControler()
        self.BC = BillControler(self)

        #window settings
        self.Root.minsize("1000", "500")
        self.Root.title("Optimisation Incorporation")

        #Programme setting
        Version = "Version 0.2.1"
        Label(self.Root, text=Version).pack(side=BOTTOM)

        #test
        Label(self.Lframe, text="test").pack()
        EnterLog("Init Management")
        EnterLog("Game :: Begin\n")
        self.Game()

    def Lunch(self):
        self.Root.mainloop()

    def Game(self):
        self.ClearFrames()
        if not self.Tframe.winfo_children():
            self.initTop()

        #Left Frame
        Label(self.Lframe, text=self.CC.GetName(), font=("Arial", 15, "underline")).pack()
        Label(self.Lframe, text=self.CC.GetToString(), font=("Arial", 13), justify=LEFT).pack()

        #Right Frame
        Button(self.Rframe, text="Marchand", font=("Arial", 15), command=lambda: self.RC.GetShop(self.Rframe)).pack(fill=X)
        Button(self.Rframe, text="Usine", font=("Arial", 15)).pack(fill=X)
        Button(self.Rframe, text="Laboratoire", font=("Arial", 15)).pack(fill=X)
        Button(self.Rframe, text="Stockage", font=("Arial", 15), command=lambda: self.RC.GetStorage(self.Rframe, self.CC.GetRessources())).pack(fill=X)
        Button(self.Rframe, text="Amélioration", font=("Arial", 15)).pack(fill=X)
        Button(self.Rframe, text="Historique des transactions", font=("Arial", 15), command=lambda: self.BC.GetAllBill(self.Rframe)).pack(fill=X)

        self.Tframe.pack(side=TOP, fill=X)
        self.Lframe.pack(side=LEFT, fill=BOTH, expand=TRUE)
        self.Rframe.pack(side=RIGHT, fill=BOTH, expand=TRUE)
        self.ContentFrame.pack(fill=X)
        EnterLog("Init Content Frame with Lframe and Rframe")



    def ClearFrames(self):
        for w in self.Lframe.winfo_children():
            w.destroy()
        for w in self.Rframe.winfo_children():
            w.destroy()
        EnterLog("ClearFrame")

    def initTop(self):
        for w in self.Tframe.winfo_children():
            w.destroy()
        qtTotal = self.CC.GetStorageQuantity()
        stg = "Argent : "+str(self.CC.GetMoney())+"€\tEmployés : "+str(self.CC.GetEmployes())+"\tStockage : "+str(round(qtTotal/(self.CC.GetStorage()*1500)*100, 2))+"%"+"\tEnergie : "+str(self.CC.GetPower())+"/"+str(self.CC.GetMaxPower())
        Label(self.Tframe, text=stg, font=("Arial", 15)).pack()
        EnterLog("Init Top frame")

    def Buy(self, price, Ress, qt):
        if self.CC.GetMoney() >= price:
            print(str(self.CC.GetMoney())+"-"+str(price))
            self.CC.SetMoney(self.CC.GetMoney()-price)
            self.CC.SetRessources(self.RC.SetQuantityForCompany(Ress.GetID(), qt, self.CC.GetRessources()))
            self.BC.AddNewBill(Ress.GetPrice(), Ress.GetName(), qt)
            self.CC.WriteRessources()
            self.CC.SaveCompany()
            self.initTop()
            self.Game()





