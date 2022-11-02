class Work:
    def __init__(self,hours,tariff):
        self.hours= hours
        self.tariff = tariff
    def calculate(self):
        print("Payment: ", self.hours*self.tariff)
payment = Work(int(input()), float(input()))
payment.calculate()