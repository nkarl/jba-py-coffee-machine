# Write your code here
import traceback
import copy

coffee_menu = {
    '1': (
        'espresso'  , {'water' : 250, 'milk' : 0, 'beans'   : 16, 'cups': 1, 'money' : 4}
    ),
    '2': (
        'latte'     , {'water' : 350, 'milk' : 75, 'beans'  : 20, 'cups': 1, 'money' : 7}
    ),
    '3': (
        'cappuccino', {'water' : 200, 'milk' : 100, 'beans' : 12, 'cups': 1, 'money' : 6}
    )
}

supplies = {
    'water': 400, 'milk': 540, 'beans': 120, 'cups': 9, 'money': 550
}


def make_coffee(coffee_type: dict):
    for k in coffee_type:
        if supplies[k] < coffee_type[k]:
            print(f'Sorry, not enough {k}')
            return
    print('I have enough resources, making you a coffee!')
    print()
    for k in coffee_type:
        if k == 'money':
            supplies[k] += coffee_type[k]
        else:
            supplies[k] -= coffee_type[k]


def buy():
    # the user must choose one of the three types of coffee: espresso, latte, or cappuccino
    print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
    try:
        order = input()
        if order in coffee_menu:
            coffee = coffee_menu.get(order)[1]
            make_coffee(coffee)
    except KeyError:
        print(traceback.format_exc())


def fill():
    supplies['water'] = supplies['water'] + int(input('Write how many ml of water you want to add:\n'))
    supplies['milk']  = supplies['milk']  + int(input('Write how many ml of milk you want to add:\n'))
    supplies['beans'] = supplies['beans'] + int(input('Write how many grams of coffee beans you want to add:\n'))
    supplies['cups']  = supplies['cups']  + int(input('Write how many disposable cups you want to add:\n'))


def take():
    print(f"I gave you ${supplies['money']}")
    supplies['money'] = 0


def display_supplies():
    print()
    print('The coffee machine has:')
    print(f"{supplies['water']} of water")
    print(f"{supplies['milk']} of milk")
    print(f"{supplies['beans']} of coffee beans")
    print(f"{supplies['cups']} of disposable cups")
    print(f"{supplies['money']} of money")
    print()


action_menu = {'buy': buy, 'fill': fill, 'take': take, 'remaining': display_supplies, 'exit': exit}


def process_order(order: str):
    action_menu.get(order)()


def run_machine():
    # display_supplies()
    process_order(input('Write action (buy, fill, take, remaining, exit):\n'))
    # display_supplies()


def check_supplies():
    unit_water = 200
    unit_milk  = 50
    unit_beans = 15

    avail_water = int(input('Write how many ml of water the coffee machine has:\n'))
    avail_milk  = int(input('Write how many ml of milk the coffee machine has:\n'))
    avail_beans = int(input('Write how many grams of coffee beans the coffee machine has:\n'))
    cups        = int(input('Write how many cups of coffee you will need:\n'))

    tmp = [
        avail_water // unit_water,
        avail_milk  // unit_milk,
        avail_beans // unit_beans
    ]
    max_cups = min(tmp)

    if max_cups == cups:
        print('Yes, I can make that amount of coffee')
    elif max_cups > cups:
        print(f'Yes, I can make that amount of coffee (and even {max_cups - cups} more than that')
    else:
        print(f'No, I can make only {max_cups} cups of coffee')


if __name__ == '__main__':
    while True:
        run_machine()
