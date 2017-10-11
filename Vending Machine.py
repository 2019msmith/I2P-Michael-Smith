price = float(input("How much does your chocolate bar cost?: "))
print("Please insert money")
money = float(input("How much money did you insert?: "))
print(money - price, "is your change")
print("You will receive ", (money - price), "dollars in change.")

change = money - price
while change <= 10:
    print("You need to add more money!")

else:
