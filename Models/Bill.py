class Bill:
    def __init__(self, priceu, product, quantity, nb, ty):
        self.PriceU = priceu
        self.Quantity = quantity
        self.Product = product
        self.Number = nb
        self.Type = ty

    def GetPrice(self):
        return self.PriceU

    def GetQuantity(self):
        return self.Quantity

    def GetNumber(self):
        return self.Number

    def GetProduct(self):
        return self.Product

    def GetType(self):
        return self.Type

    def GetTotalPrice(self):
        total = 0
        impPrice = round(self.GetPrice() * self.GetQuantity())
        TVA = round((impPrice / 100) * 21, 2)
        if int(self.Type) == 0:
            total = impPrice+TVA
        else:
            total = impPrice
        return total
