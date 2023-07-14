MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18
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
    "coffee": 100,
}

def check_res(order):
    for item in order:
        if order[item] > resources[item]:
            return False
        else:
            return True


def insert_coin():
    total = 0
    penny = int(input("Insert your pennies"))
    nickle = int(input("Insert your nickles"))
    dime = int(input("Insert your dimes"))
    quarter = int(input("Insert your quarters"))

    total = round((penny*0.01 + nickle*0.05 + dime*0.10 + quarter*0.25), 2)

    print(f" yo have {total} dollars")

    return total

choice=""


while  choice != "off" :
    choice = input("What coffe do you want 'espreso'/'latte'/'cappucino' or 'report' for resources or if you want to turn of the machine 'off'")

    x = 0
    change = 0

    if choice == "report":
        for i in  resources:
            print(f"{i}:{resources[i]}")

    if choice == "espresso" :
        if check_res(MENU["espresso"]["ingredients"]) :
            x = insert_coin()
            if x > MENU["espresso"]["cost"]:
                change = x - MENU["cappuccino"]["cost"]
                print(f"Here is your espresso ☕️ and your change : {change}")
                for item in resources:
                    resources[item] -= MENU["espresso"]["ingredients"][item]
            else:
                print("Sry, not enough money. Money refunded.")

        else :
            print("Sorry we don't have enough ingredients.Money refunded")


    if choice == "latte" :
        if check_res(MENU["latte"]["ingredients"]) :
            x = insert_coin()
            if x > MENU["latte"]["cost"]:
                change = x - MENU["cappuccino"]["cost"]
                print(f"Here is your latte ☕️ and your change : {change}")
                for item in resources:
                    resources[item] -= MENU["latte"]["ingredients"][item]
            else:
                print("Sry, not enough money. Money refunded.")

        else :
            print("Sorry we don't have enough ingredients.Money refunded")

    if choice == "cappuccino" :
        if check_res(MENU["cappuccino"]["ingredients"]) :
            x = insert_coin()
            if x > MENU["cappuccino"]["cost"]:
                change = x - MENU["cappuccino"]["cost"]
                print(f"Here is your cappuccino ☕️ and your change : {change}")
                for item in resources:
                    resources[item] -= MENU["cappuccino"]["ingredients"][item]
            else:
                print("Sry, not enough money. Money refunded. ")

        else :
            print("Sorry we don't have enough ingredients.Money refunded")

















