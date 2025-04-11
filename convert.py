import os
import math
os.system('clear')

<<<<<<< HEAD
# v1.2.2

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
=======
# v1.0.0

def tax():
    os.system('clear')
    salesTax = int(input('Enter sales tax percentage: '))
    salesTax = salesTax / 100
    cost = float(input('Cost: '))
    final = cost * salesTax + cost
    print(f"${final:.2f}")
    input('Enter to continue')
>>>>>>> origin
    mainMenu()

def temp():
    os.system('clear')

    print('1: C to F')
    print('2: F to C')

    tempMenu = int(input('Enter '))

    if tempMenu == 1:
<<<<<<< HEAD
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
=======
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
>>>>>>> origin
    else:
        mainMenu()

def speed():
    os.system('clear')

    print('1: MPH to KPH')
    print('2: KPH to MPH')

    speedMenu = int(input('Enter: '))

    if speedMenu == 1:
<<<<<<< HEAD
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
=======
        os.system('clear')
        mph = float(input('MPH: '))
        kph = float(mph * 1.60934)
        print(f'{kph:.2f} kph')
        input('Enter to continue')
        mainMenu()
    elif speedMenu == 2:
        os.system('clear')
        kph = float(input('KPH: '))
        mph = float(kph * 0.621371)
        print(f'{mph:.2f} MPH')
        input('Enter to continue')
        mainMenu()
>>>>>>> origin
    else:
        print('Error: Returning home...')
        mainMenu()

def calc():
    os.system('clear')
    print('1: 4 function')
    print('2: Square root')
<<<<<<< HEAD
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
=======

    calc = int(input('Enter: '))

    if calc == 1:
        calc1()
    elif calc == 2:
        calc2()
>>>>>>> origin

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
<<<<<<< HEAD
            calc()
        calc()
=======
            print('Error')
            input('Enter to go home')
        mainMenu()

>>>>>>> origin
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
<<<<<<< HEAD
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

def exit():
    os.system('clear')
=======
    os.system('clear')
    print('Square root')
    x = float(input('Number: '))
    y = float(math.sqrt(x))
    print(y)
    input('Enter to continue')
    mainMenu()
>>>>>>> origin

def mainMenu():
    os.system('clear')
    print('Welcome to DevConvert')
    print('')
    print('1: Sales tax')
    print('2: Temp')
    print('3: MPH to KPH')
    print('4: Calculator ')
    print('5: Exit')

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
<<<<<<< HEAD
    else:
        print("error")
        exit()
mainMenu()
=======
    elif menu == 5:
        os.system('clear')
        exit()
    else:
        print("error")
        mainMenu()
mainMenu()

>>>>>>> origin
