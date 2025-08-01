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
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

from art import logo

machine_on = True
profit = 0


def print_report():
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: ${profit}")


def is_resource_sufficient(order_ingredients):
    """Checks if there are enough ingredients for the selected drink."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def process_coins():
    """Prompts user to insert coins and returns total amount."""
    print("Please insert coins.")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.10
    total += int(input("How many nickels? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Returns True if payment is enough, otherwise refunds."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        if change > 0:
            print(f"Here is your change: ${change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deducts ingredients and serves the coffee."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕ Enjoy!")


# Start the machine

print(logo)
print("Welcome to Coffee Café ☕")

while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        print("Shutting down. Goodbye!")
        machine_on = False
    elif choice == "report":
        print_report()
    elif choice in MENU:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
    else:
        print("Sorry, we don't have that. Please choose espresso, latte, or cappuccino.")
