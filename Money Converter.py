name = input("What's your name?: ")
print("Nice to meet you, " + name + "! My name is Pennywise, we aren't strangers anymore!")
place = input("Where will you be travelling to today, " + name + "? " "New York or London?: ")
if place == "New York":
    HKD = int(input("How many Hong Kong Dollars will you be converting for your trip to New York?: "))
    USD = 0.13
    print("You have ", USD * HKD, "USD")
if place == "new york":
    HKD = int(input("How many Hong Kong Dollars will you be converting for your trip to New York?: "))
    USD = 0.13
if place == "newyork":
    HKD = int(input("How many Hong Kong Dollars will you be converting for your trip to New York?: "))
    USD = 0.13
else:
    HKD = int(input("How many Hong Kong Dollars will you be converting for your trip to London?: "))
    GBP = 0.097
    print("You have ", GBP * HKD, "GPB")
