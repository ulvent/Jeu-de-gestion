#Autor : Alexis Callens
class Ressources:
    def __init__(self, id, name, quantity, price):
        self.ID = id
        self.Name = name
        self.Quantity = quantity
        self.Price = price

    def GetName(self):
        return self.Name

    def GetQuantity(self):
        return self.Quantity

    def GetPrice(self):
        return self.Price

    def GetID(self):
        return self.ID

    def SetQuantity(self, value):
        self.Quantity = value

    def GetInfoShop(self):
        chaine = "Nom : "+self.Name
        chaine += "\nPrix : "+str(self.Price)+"€/unité"
        chaine += "\nT.V.A : "+str(round((self.Price/100)*21, 2))+"€"
        chaine += "\n-----------------------------------------------------"
        chaine += "\nPrix TTC : "+str(round(self.Price*1.21, 2))+"€/unité"
        return chaine