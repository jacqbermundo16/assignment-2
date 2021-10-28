money = int(input("How much money do you have?  "))
applePrice = int(input("How much does a piece of apple costs?  "))

maxQuantAppl = money // applePrice
totalCost = applePrice * maxQuantAppl
change = money - totalCost

print(f"You can buy {maxQuantAppl} apples and your change is {change}.")