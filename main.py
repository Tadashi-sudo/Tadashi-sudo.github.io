import math
import kivy
kivy.require("1.9.0")
from kivy.app import App
from kivy.uix.button import Label

class welcome(App):
    def build(self):
        return Label(text = "Daiso Dollar Checker")

def truncate(x):
    return math.floor(x * 10 ** 2) / 10 ** 2

def calc(*snack, **drink):
    dict = {}
    tax = 0.047
    snax = 0
    drinx = 0
    for each in snack:
        for every in each:
            snax += truncate((every * tax) + every)

    for each in drink:
        for every in each:
            drinx += truncate((every * tax) + every + 6)

    tot = snax + drinx

    for each in range(1, 1001):
        dict.update({(1.83 * each) + tot : each})

    shown = False
    for price, num in dict.items():
        if float.is_integer(price) == True and shown == False:
            print(num, "$1.75 items must be bought for a total of", price, "dollars")  
            shown = True

s_price = []
s_total = input("Num of snack(s): ")
s_total = int(s_total)
for each in range(s_total):
    temp = input("Price of snack: ")
    temp = float(temp)
    s_price.append(temp)

d_price = []
d_total = input("Num of drink(s): ")
d_total = int(d_total)
for each in range(d_total):
    temp = input("Price of drink: ")
    temp = float(temp)
    d_price.append(temp)

calc(s_price, d_price)

run = welcome()
run.run()