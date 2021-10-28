applePrice = 20
orangePrice = 25
print(f"Apple price = {applePrice}")
print(f"Orange price = {orangePrice}")

appleQuantity = int(input("How many apples do you want to buy?  "))
orangeQuantity = int(input("How may oranges do you want to buy?  "))

appleTotalCost = applePrice * appleQuantity
orangeTotalCost = orangePrice * orangeQuantity
totalCost = appleTotalCost + orangeTotalCost

print(f"The total amount is {totalCost}.")