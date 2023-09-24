MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}
cash_back = 0


def remaining(ingredients):
    global resources
    for item in ingredients:
        resources[item] -= ingredients[item]


def report():
    return f"""Water: {resources["water"]}ml
Milk: {resources["milk"]}ml
Coffee: {resources["coffee"]}g
Money: ${round(cash_back, 1)}"""


def order_ingredient_making(order_made):
    order_ingredients = {}
    for item in MENU[order_made]["ingredients"]:
        order_ingredients[item] = MENU[order_made]["ingredients"][item]
    return order_ingredients


def is_resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if resources[item] <= order_ingredients[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def is_balance_sufficient(money_owed, order_made):
    order_price = MENU[order_made]["cost"]
    if money_owed < order_price:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        global cash_back
        cash_back = round(money_owed - order_price, 2)
        print(f"Here is ${cash_back} dollars in change.")
        return True


def total():
    print("Please, insert coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))
    total = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01 + cash_back
    return total


def coffee_machine():
    machine_is_on = True
    while machine_is_on:
        order = input("What would you like? (espresso/latte/cappuccino): ")
        # ordering report
        if order.lower() == "report":
            print(report())
        # turning off
        elif order.lower() == "off":
            return
        # ordering a drink
        else:
            drink = order_ingredient_making(order)
            is_sufficient = is_resources_sufficient(drink)
            if is_sufficient:
                money_paid = total()
                enough_money = is_balance_sufficient(money_paid, order)
                if enough_money:
                    remaining(drink)
                    print(f"Here is your {order.lower()}, Enjoy!")


coffee_machine()
