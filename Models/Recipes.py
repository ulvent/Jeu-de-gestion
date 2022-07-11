class Recipe:
    def __init__(self, id, name, product, qt, idm, cout, ress):
        self.ID = id
        self.Name = name
        self.Product = product
        self.Quantity = qt
        self.IDM = idm
        self.Cost = cout
        self.Ress = ress

    def GetName(self):
        return self.Name

    def GetProduct(self):
        return self.Product

    def GetQuantity(self):
        return self.Quantity

    def GetCost(self):
        return self.Cost

    def GetRess(self):
        return self.Ress

    def GetID(self):
        return self.ID

    def Tostring(self):
        chaine = self.Name
        chaine += "\n\nProduit : "+str(self.Quantity)+" "+self.Product
        chaine += "\nCoût de production : "
        for i in range(0, len(self.Cost)):
            chaine += "\n"+str(self.Cost[i])+" "+str(self.Ress[i])
        return chaine