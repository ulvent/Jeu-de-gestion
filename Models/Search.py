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
        return int(self.Price)

    def GetName(self):
        return self.Name

    def GetID(self):
        return int(self.ID)

    def GetIDM(self):
        return int(self.Machine)

    def GetIDR(self):
        return int(self.Ressource)

    def SetCheck(self):
        self.Check = 1

    def GetLevel(self):
        return self.Level

    def ToString(self):
        stg = self.Name
        stg += "\nRess : "+str(self.Ressource)
        stg += "\nMachine : "+str(self.Machine)
        return stg