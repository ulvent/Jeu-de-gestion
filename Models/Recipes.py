class Recipe:
    def __init__(self, id, product, qt, idm, cout, ress, lvl):
        self.ID = id
        self.Product = product
        self.Quantity = qt
        self.IDM = idm
        self.Cost = cout
        self.Ress = ress
        self.Level = lvl

    def GetProduct(self):
        return self.Product

    def GetLevel(self):
        return self.Level

    def GetQuantity(self):
        return self.Quantity

    def GetCost(self):
        return self.Cost

    def GetRess(self):
        return self.Ress

    def GetID(self):
        return self.ID

    def GetIDM(self):
        return self.IDM

    def Tostring(self):
        chaine = "Produit : "+str(self.Quantity)+" "+self.Product
        chaine += "\nCoût de production : "
        for i in range(0, len(self.Cost)):
            chaine += str(self.Cost[i])+" "+str(self.Ress[i])
        return chaine