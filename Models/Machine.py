class Machine:
    def __init__(self, id, name, lvl, power, price):
        self.ID = id
        self.Name = name
        self.Level = lvl
        self.Power = power
        self.Price = price

    def GetName(self):
        return self.Name

    def GetLevel(self):
        return int(self.Level)

    def GetID(self):
        return int(self.ID)

    def GetPower(self):
        return self.Power*self.Level

    def GetPrice(self):
        return int(self.Price)

    def SetLevel(self, value):
        self.Level = value

    def GetSaveMach(self):
        stg = str(self.ID)+":"+str(self.Name)+":"+str(self.Level)+":"+str(self.Power)+":"+str(self.Price)+"\n"
        return stg

