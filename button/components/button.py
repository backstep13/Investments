from django_unicorn.components import UnicornView


class ButtonView(UnicornView):
    interval: int = 10
    amount: int = 20000
    percent: int = 5
    add: int = 500
    tax: int = 13
    invest: float = 0
    total_taxes: float = 0
    total: float = 0

    def calculate(self):
        if int(self.interval) > 0:
            self.invest = int(self.amount) + (int(self.add)*12*int(self.interval))
            self.total_taxes = (int(self.total) - int(self.invest)) * int(self.tax)*0.01
            self.total = int(self.amount)*(1+int(self.percent)*0.01/12)**(12*int(self.interval)) + \
                (int(self.add)*((1+int(self.percent)*0.01/12)**(12*int(self.interval))-1))/(int(self.percent)*0.01/12)
