from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_on = True

menu = Menu()
money_machine = MoneyMachine()
coffee_machine = CoffeeMaker()

while machine_on:
    print("Choose your drink below, type 'off' to power off, or 'report        for a report.'")
    choice = input(f"What would you like? {menu.get_items()}\n")
    drink = menu.find_drink(choice)

    if choice == 'off':
        print('Powering off the machine.')
        machine_on = False
    elif choice == 'report':
        coffee_machine.report()
    else:
        if coffee_machine.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)