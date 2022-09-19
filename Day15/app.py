from resource import resources, MENU

def checkResources(coffeeType):
    """Check if has enough ingredients to make certain coffee"""
    enoughIngredients = True

    if resources["water"] - MENU[f"{coffeeType}"]["ingredients"]["water"] < 0:
        enoughIngredients = False

    if resources["milk"] - MENU[f"{coffeeType}"]["ingredients"]["milk"] < 0:
        enoughIngredients = False

    if resources["coffee"] - MENU[f"{coffeeType}"]["ingredients"]["coffee"] < 0:
        enoughIngredients = False

    return enoughIngredients

def checkMoney(coffee, total):
    """Checks if you have the necessary amount of cash to pay for the coffee, if does, return your change"""
    enoughMoney = True

    if MENU[coffee]["cost"] > total:
        enoughMoney = False

    change = total - MENU[coffee]["cost"]

    return {
        "enoughMoney": enoughMoney,
        "change": round(change, 2)
    }

is_on = True

while is_on:
    FLAVOR_ORDER = input("\nWhat would you like? (espresso/latte/cappuccino): ")

    if FLAVOR_ORDER == 'off':
        is_on = False
        break

    if FLAVOR_ORDER == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        continue
    
    enoughIngredients = checkResources(FLAVOR_ORDER)

    if enoughIngredients == False:
        print("\nCould not make coffee because there is not enough ingredient")

    print("\nIt will cost you $", MENU[FLAVOR_ORDER]["cost"])
    print("Please insert coins.")

    quarters = int(input("\nHow many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01

    enoughMoney = checkMoney(FLAVOR_ORDER, total)

    if enoughMoney["enoughMoney"] == False:
        print("\nCould not make coffee because there is not enough money")
    
    if enoughMoney["change"] > 0:
        print(f'Here is your change: {enoughMoney["change"]}')

    print(f'Here is your {FLAVOR_ORDER} ☕️. Enjoy!')
