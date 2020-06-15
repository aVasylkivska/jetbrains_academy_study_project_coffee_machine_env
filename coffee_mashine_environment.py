water_av = 400
milk_av = 540
coffee_av = 120
cups_av = 9
money = 550
coffee = ['espresso', 'latte', 'cappuccino']


def buying_coffee():
    print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')
    coffee_type = (input())
    if coffee_type == 'back':
        main_process()
    elif int(coffee_type) == 1:
        make_coffee(250, 0, 16, 1, 4)
    elif int(coffee_type) == 2:
        make_coffee(350, 75, 20, 1, 7)
    elif int(coffee_type) == 3:
        make_coffee(200, 100, 12, 1, 6)
    else:
        print('I can not make this coffee type')


def make_coffee(a, b, c, d, e):
    global water_av, milk_av, coffee_av, cups_av, money
    water_av -= a
    milk_av -= b
    coffee_av -= c
    cups_av -= d
    money += e
    if water_av >= 0 and milk_av >= 0 and coffee_av >= 0 and cups_av >= 0:
        print('I have enough resources, making you a coffee!')
    elif water_av < 0:
        print('Sorry, not enough water!')
        water_av += a
        milk_av += b
        coffee_av += c
        cups_av += d
        money -= e
    elif milk_av < 0:
        print('Sorry, not enough milk!')
        water_av += a
        milk_av += b
        coffee_av += c
        cups_av += d
        money -= e
    elif coffee_av < 0:
        print('Sorry, not enough coffee!')
        water_av += a
        milk_av += b
        coffee_av += c
        cups_av += d
        money -= e
    elif cups_av < 0:
        print('Sorry, not enough cups!')
        water_av += a
        milk_av += b
        coffee_av += c
        cups_av += d
        money -= e
    print()
    main_process()


def filling():
    global water_av, milk_av, coffee_av, cups_av, money
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
    main_process()


def taking():
    global money
    print('I gave you $', money, sep='')
    money = 0
    print()
    main_process()


def remaining():
    print('The coffee machine has:')
    print(water_av, 'of water')
    print(milk_av, 'of milk')
    print(coffee_av, 'of coffee beans')
    print(cups_av, 'of disposable cups')
    print(money, 'of money')
    print()
    main_process()


def main_process():
    print('Write action (buy, fill, take, remaining, exit)')
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
    elif action == 'remaining':
        remaining()
    elif action == 'exit':
        exit()


main_process()
