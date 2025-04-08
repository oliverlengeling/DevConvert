import os
os.system('clear')

def tax():
    os.system('clear')
    salesTax = int(input('Enter sales tax percentage: '))
    salesTax = salesTax / 100
    cost = float(input('Cost: '))
    final = cost * salesTax + cost
    print(f"${final:.2f}")
    input('Enter to continue')
    mainMenu()

def temp():
    os.system('clear')

    print('1: C to F')
    print('2: F to C')

    tempMenu = int(input('Enter '))

    if tempMenu == 1:
        os.system('clear')
        c = int(input('C: '))
        f = (c * 9 / 5) + 32
        print(f'{f:.2f}F')
        input('Enter to continue')
        mainMenu()
    elif tempMenu == 2:
        os.system('clear')
        f = int(input('F: '))
        c = (f - 32) * 5 / 9
        print(f'{c:.2f}C')
        input('Enter to continue')
        mainMenu()
    else:
        mainMenu()

def speed():
    os.system('clear')

    print('1: KPH to MPH')
    print('2: MPH to KPH')

    speedMenu = int(input('Enter: '))

    if speedMenu == 1:
        os.system('clear')
        kph = float(input('KPH: '))
        mph = float(kph * 1.60934)
        print(f'{mph:.2f} MPH')
        input('Enter to continue')
        mainMenu()
    elif speedMenu == 2:
        os.system('clear')
        mph = float(input('MPH: '))
        kph = float(mph * 0.621371)
        print(f'{kph:.2f} KPH')
        input('Enter to continue')
        mainMenu()
    else:
        print('Error: Returning home...')
        mainMenu()

def mainMenu():
    os.system('clear')
    print('1: Sales tax')
    print('2: Temp')
    print('3: MPH to KPH')

    global menu
    menu = int(input('Enter: '))

    if menu == 1:
        tax()
    elif menu == 2:
        temp()
    elif menu == 3:
        speed()
    else:
        print("error")
mainMenu()

