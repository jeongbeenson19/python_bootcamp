class MenuItem:
    def __init__(self, name, cost, water, milk, coffee):
        self.name = name
        self.cost = cost
        self.ingredients = {
            'water': water,
            'milk': milk,
            'coffee': coffee,
        }


class Menu:
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", cost=2.5, water=200, milk=150, coffee=24),
            MenuItem(name="espresso", cost=1.5, water=50, milk=0, coffee=18),
            MenuItem(name="cappuccino", cost=3.0, water=250, milk=100, coffee=24)
        ]

    def get_items(self):
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_item(self, order_name):
        for item in self.menu:
            if item.name == order_name:
                return item
        print(f"Sorry, {order_name} is not available now")
