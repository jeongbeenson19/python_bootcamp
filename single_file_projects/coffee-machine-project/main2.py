from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
cm = CoffeeMaker()
mm = MoneyMachine()

is_on = True

while is_on:
    menu_list = menu.get_items()
    choice = input(f"What would you like ({menu_list}): ")
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        cm.report()
        mm.report()
    else:
        drink = menu.find_item(choice)
        if cm.is_resource_sufficient(drink) and mm.make_payment(drink.cost):
            cm.make_coffee(drink)
