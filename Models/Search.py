class Search:
    def __init__(self, id, name, machine, ressource, level, price, valid):
        self.ID = id
        self.Name = name
        self.Machine = machine
        self.Ressource = ressource
        self.Level = level
        self.Price = price
        self.Check =  valid

    def GetCheck(self):
        return int(self.Check)

    def GetPrice(self):
        return self.Price

    def GetName(self):
        return self.Name

    def GetID(self):
        self.ID

    def GetIDM(self):
        return int(self.Machine)

    def GetIDR(self):
        return int(self.Ressource)