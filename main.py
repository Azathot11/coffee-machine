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

profit = 0

user_choice = input('What would you like? (espresso/latte/cappuccino): ')


def reduce_resource(ingredients):
    resources['water'] -= ingredients['water']
    if 'milk' in ingredients.keys():
        resources['milk'] -= ingredients['milk']
    resources['coffee'] -= ingredients['coffee']


def insert_coins(flavor):
    print(flavor)
    global profit
    quarter = float(input('How many quarters?: ')) * 0.25
    dime = float(input('How many dimes?: ')) * 0.10
    penny = float(input('How many pennies?: ')) * 0.05
    nickel = float(input('How many nickels?: ')) * 0.01
    sum_in_dollars = quarter + dime + penny + nickel
    profit += flavor['cost']
    reduce_resource(flavor['ingredients'])

    if sum_in_dollars > flavor['cost']:
        difference_in_dollars = sum_in_dollars - flavor['cost']
        print(f'Here is ${round(difference_in_dollars)} in change.')
        print(f"Here is your {user_choice} ☕️. Enjoy!")
    elif sum_in_dollars == flavor['cost']:
        print(f"Here is your {user_choice} ☕️. Enjoy!")
    else:
        print('Sorry that\'s not enough money. Money refunded.')


def quantity_check(flavor):

    if resources['water'] < flavor['ingredients']['water']:
        print('Sorry there is not enough water.')
    elif 'milk' in flavor.keys():
        if resources['milk'] < flavor['ingredients']['milk']:
            print('Sorry there is not enough milk.')
    elif resources['coffee'] < flavor['ingredients']['coffee']:
        print('Sorry there is not enough coffee.')
    else:
        print('Please insert coins.')
        insert_coins(flavor)


if user_choice == 'report':
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Coffee: ${profit}")
elif user_choice == 'espresso':
    quantity_check(MENU['espresso'])
elif user_choice == 'latte':
    quantity_check(MENU['latte'])

elif user_choice == 'cappuccino':
    quantity_check(MENU['cappuccino'])
