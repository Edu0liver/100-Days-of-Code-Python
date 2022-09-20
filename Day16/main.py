from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

while is_on:
    FLAVOR_ORDER = input("\nWhat would you like? (espresso/latte/cappuccino): ")

    if FLAVOR_ORDER == 'off':
        is_on = False
        break

    if FLAVOR_ORDER == 'report':
        coffee_maker.report()
        money_machine.report()
        continue
    
    itemInfo = menu.find_drink(FLAVOR_ORDER)

    is_sufficient = coffee_maker.is_resource_sufficient(itemInfo)

    if not is_sufficient:
        break
    
    print("\nIt will cost you $", itemInfo.cost)
    
    enoughMoney = money_machine.make_payment(itemInfo.cost)

    coffee_maker.make_coffee(itemInfo)
