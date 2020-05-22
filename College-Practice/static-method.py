class Bank():
    def __init__(self, p, r, t):
        self.p = p
        self.r = r
        self.t = t

    @staticmethod
    def SI(p, r, t):
        print(p*r*t*0.01)

cus = Bank(100, 1, 2)
cus.SI()
Bank.SI(100, 2, 2)
