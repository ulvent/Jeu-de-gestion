class Bill:
    def __init__(self, priceu, product, quantity, nb):
        self.PriceU = priceu
        self.Quantity = quantity
        self.Product = product
        self.Number = nb

    def GetPrice(self):
        return self.PriceU

    def GetQuantity(self):
        return self.Quantity

    def GetNumber(self):
        return self.Number

    def GetProduct(self):
        return self.Product

    def GetTotalPrice(self):
        impPrice = round(self.GetPrice() * self.GetQuantity())
        TVA = round((impPrice / 100) * 21, 2)
        return impPrice+TVA
