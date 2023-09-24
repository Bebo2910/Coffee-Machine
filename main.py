from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu_holder = Menu()

machine_is_on = True
while machine_is_on:
    order = input(f"What would you like? ({menu_holder.get_items()}): ").lower()
    if order == "report":
        coffee_maker.report()
        money_machine.report()
    elif order == "off":
        machine_is_on = False
    else:
        drink = menu_holder.find_drink(order)
        resources = coffee_maker.is_resource_sufficient(drink)
        if resources:
            enough = money_machine.make_payment(drink.cost)
            if enough:
                coffee_maker.make_coffee(drink)



