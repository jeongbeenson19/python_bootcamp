class MoneyMachine:
    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        print(f"Profit is {self.CURRENCY}{self.profit}")

    def coin_process(self):
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}: ")) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost):
        self.coin_process()
        if self.money_received >= cost:
            changes = round((self.money_received - cost), 2)
            self.profit += cost
            self.money_received = 0
            print(f"Here is your {self.CURRENCY}{changes}")
            return True
        else:
            print(f"You don't have not enough money")
            self.money_received = 0
            return False
