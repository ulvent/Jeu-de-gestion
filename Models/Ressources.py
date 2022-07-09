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