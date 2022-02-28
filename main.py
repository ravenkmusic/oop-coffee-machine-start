import money_machine
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
coffee_machine_on = True


while coffee_machine_on:
    choices = menu.get_items()
    drink = input(f"What would you like? {choices}: ")
    if drink == "off":
        coffee_machine_on = False
    elif drink == "report":
        coffee_machine_on = True
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(drink)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
                coffee_maker.report()
                money_machine.report()