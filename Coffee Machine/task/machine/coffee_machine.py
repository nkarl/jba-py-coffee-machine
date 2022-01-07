# Write your code here
import json
import traceback
import os

if os.path.isdir('./machine'):
    os.chdir('./machine')
cwd = os.getcwd()
cmenu = cwd + '/coffee_menu.json'
st = cwd + '/stocks.json'

with open(cmenu) as c, open(st) as s:
    coffees = json.load(c)
    stocks = json.load(s)


class CoffeeTransaction:

    def __init__(self, coffees_json: dict, supplies_json: dict):
        self.coffees = coffees_json
        self.stocks = supplies_json
        self.action_menu = {
            'buy': self.buy,
            'fill': self.fill,
            'take': self.take,
            'remaining': self.display_supplies,
            'exit': exit
        }

    def make_coffee(self, coffee_type: dict):
        for k in coffee_type:
            if self.stocks[k] < coffee_type[k]:
                print(f'Sorry, not enough {k}')
                return
        print('I have enough resources, making you a coffee!\n')
        for k in coffee_type:
            if k == 'money':
                self.stocks[k] += coffee_type[k]
            else:
                self.stocks[k] -= coffee_type[k]

    def buy(self):
        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        try:
            order = input()
            if order == 'back':
                return
            # if order in self.coffees:
            coffee = self.coffees.get(order)[1]
            self.make_coffee(coffee)
        except KeyError:
            print(traceback.format_exc())

    def fill(self):
        self.stocks['water'] = self.stocks['water'] + \
                               int(input('Write how many ml of water you want to add:\n'))
        self.stocks['milk'] = self.stocks['milk'] + \
                              int(input('Write how many ml of milk you want to add:\n'))
        self.stocks['beans'] = self.stocks['beans'] + \
                               int(input('Write how many grams of coffee beans you want to add:\n'))
        self.stocks['cups'] = self.stocks['cups'] + \
                              int(input('Write how many disposable cups you want to add:\n'))

    def take(self):
        print(f"I gave you ${self.stocks['money']}")
        self.stocks['money'] = 0

    def display_supplies(self):
        print()
        print('The coffee machine has:')
        print(f"{self.stocks['water']} of water")
        print(f"{self.stocks['milk']} of milk")
        print(f"{self.stocks['beans']} of coffee beans")
        print(f"{self.stocks['cups']} of disposable cups")
        print(f"{self.stocks['money']} of money")
        print()

    def process_order(self, order: str):
        self.action_menu.get(order)()

    def update_database(self):
        pass


def run_machine(user_instance: CoffeeTransaction):
    user_instance.process_order(input('Write action (buy, fill, take, remaining, exit):\n'))


if __name__ == '__main__':
    instance = CoffeeTransaction(coffees, stocks)
    while True:
        run_machine(instance)
