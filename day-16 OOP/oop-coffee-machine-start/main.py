from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

"""latte = MenuItem("latte", 200, 150, 24, 2.5) 

espresso = MenuItem("espresso", 50, 0, 18, 1.5)

cappuccino = MenuItem("cappuccino", 250, 100, 24, 3)"""

menu = Menu()

coffee_maker = CoffeeMaker()

money_machine = MoneyMachine()

is_on = True

while is_on:

    choice = input(menu.get_items())

    if choice == "off":
        is_on = False

    elif choice == "report" :
        coffee_maker.report()
        money_machine.report()

    elif menu.find_drink(choice) :

        drink = menu.find_drink(choice)

        if coffee_maker.is_resource_sufficient(drink):

             if  money_machine.make_payment(drink.cost):
                 coffee_maker.make_coffee(drink)

             else :
                 print("Sorry not enough money. Money Refunded.")

        else :
            print("Sory  not enough ingredients.")








