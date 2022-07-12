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
        return self.Check

    def GetPrice(self):
        return self.Price