class Machine:
    def __init__(self, id, name, lvl, power):
        self.ID = id
        self.Name = name
        self.Level = lvl
        self.Power = power

    def GetName(self):
        return self.Name

    def GetLevel(self):
        return self.Level

    def GetID(self):
        return self.ID

    def GetPower(self):
        return self.Power*self.Level