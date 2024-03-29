from Logs import EnterLog
from Models.Bill import *
import os

from View.BillView import BillView


class BillControler:
    def __init__(self, back):
        self.Bill = []
        self.ReadBill()
        self.BV = BillView(self)
        self.Back = back
        EnterLog("Init billControler")


    def GetBill(self, index):
        impPrice = round(self.Bill[index].GetPrice() * self.Bill[index].GetQuantity())
        TVA = round((impPrice / 100) * 21, 2)
        stg = "Facture n° " + str(self.Bill[index].GetNumber())
        if self.Bill[index].GetType() == 0:
            stg += "\nAchat de " + str(self.Bill[index].GetProduct())
        else:
            stg += "\nVente de " + str(self.Bill[index].GetProduct())
        stg += "\n-----------------------------"
        stg += "\nPrix unitaire :\t" + str(self.Bill[index].GetPrice())+"€"
        stg += "\nQuantitée :\t" + str(self.Bill[index].GetQuantity())+" unités"
        if self.Bill[index].GetType() == 0:
            stg += "\n-----------------------------"
            stg += "\nPrix imposable :\t" + str(impPrice)+"€"
            stg += "\nT.V.A 21% :\t" + str(TVA)+"€"
            stg += "\n-----------------------------"
            stg += "\nPrix TTC :\t" + str(round(impPrice + TVA, 2))+"€"
        else:
            stg += "\nPrix Total :\t" + str(impPrice) + "€"
        EnterLog("BillControler :: GetBill")
        return stg


    def writeBill(self):
        os.remove("Data/Save/Bill.txt")
        with open("Data/Save/Bill.txt", "a+") as File:
            for i in range(0, len(self.Bill)):
                stg = str(self.Bill[i].GetNumber()) + ":" + str(self.Bill[i].GetPrice()) + ":" + str(self.Bill[i].GetQuantity()) + ":" + str(self.Bill[i].GetProduct()) +":"+str(self.Bill[i].GetType())+ "\n"
                File.write(stg)
            File.close()
        EnterLog("BillControler :: WriteBill")

    def GetIndex(self, number):
        index = 0
        for b in self.Bill:
            if b.GetNumber() == number:
                return int(index)
            else:
                index += 1

    def addBill(self, priceu, product, quantity, nb, ty):
        self.Bill.append(Bill(priceu, product, quantity, nb, ty))

    def ReadBill(self):
        with open("Data/Save/Bill.txt") as File:
            data = File.readlines()
            if data != []:
                for i in range(0, len(data)):
                    sp = data[i].split(":")
                    self.addBill(float(sp[1]), sp[3], int(sp[2]), int(sp[0]), int(sp[4].split("\n")[0]))
                    File.close()
                EnterLog("BillControler :: ReadBill :: SUCCESS")
            else:
                EnterLog("BillControler :: ReadBill :: No data")

    def AddNewBill(self, priceu, product, quantity, ty):
        nb = len(self.Bill)+1
        self.Bill.append(Bill(priceu, product, quantity, nb, ty))
        self.writeBill()

    def GetAllBill(self, root):
        for w in root.winfo_children():
            w.destroy()
        self.BV.GetAllBill(self.Bill, root)

    def GetInfo(self, value):
        index = self.GetIndex(value)
        return self.GetBill(index)

    def Retour(self):
        self.Back.Game()
