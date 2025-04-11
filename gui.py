
# Afternoon

# DISCONTINUED FOR NOW


import os
os.system('clear')
import tkinter as tk
from tkinter import ttk

versionNumber = 'v0.3'
print(f"Thank you for using DevConvert {versionNumber} written by Oliver Lengeling")

def update(entry, label):
    try:
        salesTax = 0.07
        cost = entry.get()
        tax = float(cost) * float(salesTax) + float(cost)
        label.config(text=f"The cost will be ${tax:.2f} in Iowa")
    except ValueError:
        label.config(text="error 1", fg="red")

def devTax():
    new_window = tk.Toplevel(root)
    new_window.geometry("250x150")

    label = tk.Label(new_window, text="Cost of item:")
    label.pack()

    entry = tk.Entry(new_window)
    entry.pack()

    result_label = tk.Label(new_window, text="")
    result_label.pack()

    button = tk.Button(new_window, text="Enter", command=lambda: update(entry, result_label))
    button.pack()


def devTempUpdateF(entryf, label):
    try:
        f = float(entryf.get())
        c = (f - 32) * 5 / 9
        label.config(text=f"The temp is {c:.2f} celsius")
    except:
        label.config(text="error", fg="red")
        print("error 1")

def devTempF():
    devtemp = tk.Toplevel(root)
    devtemp.geometry("350x120")

    ff = tk.Label(devtemp, text="Enter F to get C")
    ff.pack()

    entryf = tk.Entry(devtemp)
    entryf.pack()

    result_label = tk.Label(devtemp, text="")
    result_label.pack()

    button = tk.Button(devtemp, text="F to C", command=lambda: devTempUpdateF(entryf, result_label))
    button.pack()


def devTempUpdateC(entryc, label):
    try:
        c = float(entryc.get())
        f = (c * 9/5) + 32
        label.config(text=f"The temp is {f:.2f} ferenheight")
    except:
        print("error 1", fg="red")

def devTempC():
    devtempc = tk.Toplevel(root)
    devtempc.geometry("350x120")

    cc = tk.Label(devtempc, text="Enter C to get F")
    cc.pack()

    entryc = tk.Entry(devtempc)
    entryc.pack()

    result_label = tk.Label(devtempc, text="")
    result_label.pack()

    buttonc = tk.Button(devtempc, text="C to F", command=lambda: devTempUpdateC(entryc, result_label))
    buttonc.pack()

    devtempc.mainloop()

def devTempMenu():
    menu = tk.Toplevel(root)
    menu.geometry("250x150")

    f = tk.Button(menu, text="F to C", command=devTempF)
    f.pack()
    c = tk.Button(menu, text="C to F", command=devTempC)
    c.pack()


def mphUpdate(entry, label):

    kph = float(entry.get())
    mph = float(kph * 1.60934)
    label.config(text=f"{mph:.2f} mph")


def mphMenu():
    mph2 = tk.Toplevel(root)
    mph2.geometry("250x350")

    mphToKph = tk.Label(mph2, text="Mph to Kph")
    mphToKph.pack()

    entry = tk.Entry(mph2)
    entry.pack()

    result_label = tk.Label(mph2, text="")
    result_label.pack()

    button = tk.Button(mph2, text="mph to kph", command=lambda: mphUpdate(entry, result_label))
    button.pack()


def kphUpdate(entryKph, label):
    mph = float(entryKph.get())
    kph = float(mph * 0.621371)
    label.config(text=f"{kph:.2f} kph")

def kphMenu():
    kph = tk.Toplevel(root)
    kph.geometry("250x350")

    kphToMph = tk.Label(kph, text="Kph to Mph")
    kphToMph.pack()

    entryKph = tk.Entry(kph)
    entryKph.pack()

    result_label = tk.Label(kph, text="")
    result_label.pack()

    kphConvert = tk.Button(kph, text="kph to mph", command=lambda: kphUpdate(entryKph, result_label))
    kphConvert.pack()



def mphToKphMenu():
    conMenu = tk.Toplevel(root)
    conMenu.geometry("250x350")

    mph1 = tk.Button(conMenu, text="mph to kph", command=mphMenu)
    mph1.pack()
    kph1 = tk.Button(conMenu, text="kph to mph", command=kphMenu)
    kph1.pack()

root = tk.Tk()
root.title("DevConvert")
root.geometry("250x150")

devTax = tk.Button(text="Sales tax", command=devTax)
devTax.pack()

devTemp = tk.Button(text="Temp Converter", command=devTempMenu)
devTemp.pack()

mph = tk.Button(text="MPH to KPH", command=mphToKphMenu)
mph.pack()

root.mainloop()

print("Exiting...")
