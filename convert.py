import os
import math
import random
os.system('clear')
# v1.5.0

def tax():
    try:
        os.system('clear')
        salesTax = int(input('Enter sales tax percentage: '))
        salesTax = salesTax / 100
        cost = float(input('Cost: '))
        final = cost * salesTax + cost
        print(f"${final:.2f}")
        input('Enter to continue')
    except:
        print('Error')
        input('Enter to home')
    mainMenu()

def temp():
    os.system('clear')

    print('1: C to F')
    print('2: F to C')

    tempMenu = int(input('Enter '))

    if tempMenu == 1:
        try:
            os.system('clear')
            c = int(input('C: '))
            f = (c * 9 / 5) + 32
            print(f'{f:.2f}F')
            input('Enter to continue')
            mainMenu()
        except:
            print('Error')
            input('Enter to go home')
            mainMenu()

    elif tempMenu == 2:
        try:
            os.system('clear')
            f = int(input('F: '))
            c = (f - 32) * 5 / 9
            print(f'{c:.2f}C')
            input('Enter to continue')
            mainMenu()
        except:
            print('Error')
            input('Enter to go home')
            mainMenu()
    else:
        mainMenu()

def speed():
    os.system('clear')

    print('1: MPH to KPH')
    print('2: KPH to MPH')

    speedMenu = int(input('Enter: '))

    if speedMenu == 1:
        try:
            os.system('clear')
            mph = float(input('MPH: '))
            kph = float(mph * 1.60934)
            print(f'{kph:.2f} kph')
            input('Enter to continue')
            mainMenu()
        except:
            print('Error')
            input('Enter to go home')
            mainMenu()

    elif speedMenu == 2:
        try:
            os.system('clear')
            kph = float(input('KPH: '))
            mph = float(kph * 0.621371)
            print(f'{mph:.2f} MPH')
            input('Enter to continue')
            mainMenu()
        except:
            print('Error')
            input('Enter to go home')
            mainMenu()
    else:
        print('Error: Returning home...')
        mainMenu()

def calc():
    os.system('clear')
    print('1: 4 function')
    print('2: Square root')
    print('3: Power of')
    print('4: Shapes')

    calc = int(input('Enter: '))

    try:
        if calc == 1:
            calc1()
        elif calc == 2:
            calc2()
        elif calc == 3:
            calc3()
        elif calc == 4:
            calc4()
        else:
            calc()
    except:
        mainMenu()

def calc1():
    os.system('clear')
    print('1: Add')
    print('2: Subtract')
    print('3: Multiply')
    print('4: Divide')

    calcMenu = int(input('Enter: '))

    if calcMenu == 1:
        os.system('clear')
        try:
            print('Add')
            x = float(input('Number 1: '))
            y = float(input('Number 2: '))
            z = float(x + y)
            print(z)
            input('Enter to continue')
        except:
            calc()
        calc()
    elif calcMenu == 2:
        os.system('clear')
        print('Subtract')
        try:
            x = float(input('Number 1: '))
            y = float(input('Number 2: '))
            z = float(x - y)
            print(z)
            input('Enter to continue')
        except:
            print('Error')
            input('Enter to go home')
        mainMenu()

    elif calcMenu == 3:
        os.system('clear')
        try:
            print('Multiply')
            x = float(input('Number 1: '))
            y = float(input('Number 2: '))
            z = float(x * y)
            print(z)
            input('Enter to continue')
        except:
            print('Error')
            input('Enter to go home')
        mainMenu()

    elif calcMenu == 4:
        os.system('clear')
        try:
            print('Divide')
            x = float(input('Number 1: '))
            y = float(input('Number 2: '))
            z = float(x / y)
            print(z)
            input('Enter to continue')
        except:
            print('Error')
            input('Enter to go home')
        mainMenu()

    elif calcMenu > 4:
        input('Error press enter')
        mainMenu()

def calc2():
    try:
        os.system('clear')
        print('Square root')
        x = float(input('Number: '))
        y = float(math.sqrt(x))
        print(y)
        input('Enter to continue')
        mainMenu()
    except:
            print('Error')
            input('Enter to go home')
            mainMenu()

def calc3():
    try:
        os.system('clear')
        print('Power')
        x = float(input('Number: '))
        y = float(input('Power: '))
        z = float(x ** y)
        print(z)
        input('Enter to continue ')
        calc()
    except:
        input('Error')
        mainMenu()

def calc4():
    os.system('clear')
    print('1: Circles')
    print('2: Triangles')
    print('3: Square/Rectangle')

    calcMenu = int(input('Enter: '))

    if calcMenu == 1:
        os.system('clear')
        print('1: Circumference')
        print('2: Area')
        calcMenuCircle = float(input('Enter: '))
        if calcMenuCircle == 1:
            try:
                os.system('clear')
                r = float(input('Radius: '))
                c = float(2 * math.pi * r)
                print(f'C = {c}')
                input('Enter to continue')
                calc4()
            except:
                mainMenu()
        if calcMenuCircle == 2:
            try:
                os.system('clear')
                r = float(input('Radius: '))
                a = float(math.pi * r ** 2)
                print(f'A = {a}')
                input('Enter to continue')
                calc4()
            except:
                mainMenu()
    if calcMenu == 2:
        try:
            os.system('clear')
            print('Area of triangle')
            b = float(input('Base: '))
            h = float(input('Height: '))
            a = float(0.5 * b * h)
            print(f'A = {a}')
            input('Enter to continue')
            calc4()
        except:
            mainMenu()

    if calcMenu == 3:
        try:
            os.system('clear')
            print('1: Area')
            print('2: Diagonal')
            calcMenuRect = int(input('Enter: '))

            if calcMenuRect == 1:
                os.system('clear')
                try:
                    x = float(input('Length: '))
                    y = float(input('Width: '))
                    z = float(x * y)
                    print(f'A = {z}')
                    input('Enter to continue')
                    calc4()
                except:
                    mainMenu()

            if calcMenuRect == 2:
                os.system('clear')
                try:
                    x = float(input('Length: '))
                    y = float(input('Width: '))
                    z = float(math.sqrt(y ** 2 + x ** 2))
                    print(f'D = {z}')
                    input('Enter to continue')
                    calc4()
                except:
                    mainMenu()
        except:
            mainMenu()

def rand():
        z = int(0)
        os.system('clear')
        print('Enter an integer')
        x = int(input('Number 1: '))
        y = int(input('Number 2: '))

        while 1 == True:
            z = random.randint(x, y)
            print(z)
            input()
        mainMenu()

def money():
    os.system('clear')
    print('1: USD')
    print('2: Euro')
    moneyMenu = int(input('Enter: '))
    if moneyMenu == 1:
        usd()
    elif moneyMenu == 2:
        euro()
    elif moneyMenu == 3:
        mainMenu()

# Inflation
e = 0.88
c = 1.39
p = 20.29
u = 1.14

def usd():
    os.system('clear')
    print('1: To Euro')
    print('2: To Canadian')
    print('3: To Peso')

    usdMenu = int(input('Enter: '))
    os.system('clear')
    if usdMenu == 1:
        usd = float(input('USD: '))
        euro = usd * e
        print(f'{euro:.2f} Euros')
        input('Enter to continue')
        money()
    if usdMenu == 2:
        usd = float(input('USD: '))
        can = usd * c
        print(f'{can:.2f} Canadian')
        input('Enter to continue')
        money()
    if usdMenu == 3:
        usd = float(input('USD: '))
        peso = usd * p
        print(f'{peso:.2f} Pesos')
        input('Enter to continue')
        money()
def euro():
    os.system('clear')
    print('1: To USD')
    print('2: To Peso')
    print('3: To Canadian')

    euroMenu = int(input('Euro: '))

    if euroMenu == 1:
        os.system('clear')
        euro = float(input('Euro: '))
        usd = float(euro * u)
        print(f'{usd} USD')
        input('Enter to continue')
        money()
    if euroMenu == 2:
        os.system('clear')
        euro = float(input('Euro: '))
        peso = float(euro * p)
        print(f'{peso} Pesos')
        input('Enter to continue')
        money()
    if euroMenu == 3:
        os.system('clear')
        euro = float(input('Euro: '))
        can = float(euro * c)
        print(f'{can} Canadian')
        input('Enter to continue')
        money()

def games():
    os.system('clear')

    print('1: Rock paper scissors')
    gameMenu = input('Enter: ')

    if gameMenu == '':
        mainMenu()

    if gameMenu == '1':
        x = random.randint(1, 3)
        os.system('clear')
        print('Rock, paper, scissors')
        user = input('Enter: ')

        if user == 'rock':
            y = 1
        elif user == 'paper':
            y = 2
        elif user == 'scissors':
            y = 3
        elif y == x:
            print('tie')
        else:
            mainMenu()

        if y == 1 and x == 3:
            print('win')
            input()
            games()
        elif y == 2 and x == 1:
            print('win')
            input()
            games()
        elif y == 3 and x == 2:
            print('win')
            input()
            games()
        else:
            print('lose')
            input()
            games()
    else:
        mainMenu()
def exit():
    os.system('clear')

def mainMenu():
    os.system('clear')
    print('Welcome to DevConvert')
    print('')
    print('1: Sales tax')
    print('2: Temp')
    print('3: MPH to KPH')
    print('4: Calculator ')
    print('5: Random integer')
    print('6: Money')
    print('7: Games')
    print('8: Exit')

    global menu
    menu = int(input('Enter: '))

    if menu == 1:
        tax()
    elif menu == 2:
        temp()
    elif menu == 3:
        speed()
    elif menu == 4:
        calc()
    elif menu == 5:
        rand()
    elif menu == 6:
        money()
    elif menu == 7:
        games()
    else:
        print("exiting...")
        exit()
mainMenu()
