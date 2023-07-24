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
    "coffee": 100,
}

user_choice = input('What would you like? (espresso/latte/cappuccino): ')


def insert_coins():
    quarter = int(input('How many quarters?: '))
    penny = int(input('How many pennies?: '))
    nickel = int(input('How many nickels?: '))
    dime = int(input('How many dimes?: '))


def quantity_check(flavor):
    print(flavor)
    if resources['water'] < flavor['water']:
        print('Sorry there is not enough water.')
    elif 'milk' in flavor.keys():
        if resources['milk'] < flavor['milk']:
            print('Sorry there is not enough milk.')
    elif resources['coffee'] < flavor['coffee']:
        print('Sorry there is not enough coffee.')
    else:
        print('Please insert coins.')
        insert_coins()


if user_choice == 'report':
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
elif user_choice == 'espresso':
    quantity_check(MENU['espresso']['ingredients'])
elif user_choice == 'latte':
    quantity_check(MENU['latte']['ingredients'])

elif user_choice == 'cappuccino':
    quantity_check(MENU['cappuccino']['ingredients'])
