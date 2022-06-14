def calc(*prices):
    return 0

dict = {}
for each in range(1, 101):
    dict.update({(1.57 * each) + 2.61 : each})

for price, num in dict.items():
    if float.is_integer(price) == True:
        print(num, "$1.50 items must be bought")