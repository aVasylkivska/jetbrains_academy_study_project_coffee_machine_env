water_av = 400
milk_av = 540
coffee_av = 120
cups_av = 9
money = 550
coffee = ['espresso', 'latte', 'cappuccino']


def buying_coffee():
    print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')
    coffee_type = (int(input()))
    if coffee_type == 1:
        make_coffee(250, 0, 16, 1, 4)
    elif coffee_type == 2:
        make_coffee(350, 75, 20, 1, 7)
    elif coffee_type == 3:
        make_coffee(200, 100, 12, 1, 6)
    else:
        print('I can not make this coffee type')


def make_coffee(a, b, c, d, e):
    global water_av
    global milk_av
    global coffee_av
    global cups_av
    global money
    water_av -= a
    milk_av -= b
    coffee_av -= c
    cups_av -= d
    money += e
    print('The coffee machine has:')
    print(water_av, 'of water')
    print(milk_av, 'of milk')
    print(coffee_av, 'of coffee beans')
    print(cups_av, 'of disposable cups')
    print(money, 'of money')


def filling():
    global water_av
    global milk_av
    global coffee_av
    global cups_av
    print('Write how many ml of water do you want to add:')
    water_filled = int(input())
    water_av += water_filled
    print('Write how many ml of milk do you want to add:')
    milk_filled = int(input())
    milk_av += milk_filled
    print('Write how many grams of coffee beans do you want to add:')
    coffee_filled = int(input())
    coffee_av += coffee_filled
    print('Write how many disposable cups of coffee do you want to add:')
    cups_filled = int(input())
    cups_av += cups_filled


def taking():
    global water_av
    global milk_av
    global coffee_av
    global cups_av
    global money
    print('I gave you $', money, sep='')
    money = 0
    print()
    print('The coffee machine has:')
    print(water_av, 'of water')
    print(milk_av, 'of milk')
    print(coffee_av, 'of coffee beans')
    print(cups_av, 'of disposable cups')
    print(money, 'of money')


print('The coffee machine has:')
print(water_av, 'of water')
print(milk_av, 'of milk')
print(coffee_av, 'of coffee beans')
print(cups_av, 'of disposable cups')
print(money, 'of money')
print()
print('Write action (buy, fill, take)')
action = input()
if action == 'buy':
    buying_coffee()
elif action == 'fill':
    filling()
    print('The coffee machine has:')
    print(water_av, 'of water')
    print(milk_av, 'of milk')
    print(coffee_av, 'of coffee beans')
    print(cups_av, 'of disposable cups')
    print(money, 'of money')
elif action == 'take':
    taking()
