#Enter the Price of the Chocolate bar)
vPrice = float(input("Please enter the price of the chocolate you want:"))
print(vPrice)

#Enter the Cash to pay for the chocolate
vCash = float(input("Please enter the cash of the chocolate you want:"))
print(vCash)

##Calculate the Change Due
vChangeDue = vCash - vPrice
vChangeGiven = round(vChangeDue,2)

#Display the Price, Cash, Change Due and ChangeGiven
print("TRANSACTION SUMMARY MY FUNCTION")
print("Price of Chocolate:",vPrice)
print("Cash Paid:",vCash)
print("Change Due:",round(vChangeDue,2))
print("Total Change Given:",vChangeGiven)

#While the Change Due is greater than 0
#   Give out the largest coin possible

while vChangeDue >= 50:
    vChangeGiven = vChangeGiven + 50
    vChangeDue = vChangeDue - 50
    print("Giving out $50 note")

while vChangeDue >= 20:
    vChangeGiven = vChangeGiven + 20
    vChangeDue = vChangeDue - 20
    print("Giving out $20 note")

while vChangeDue >= 10:
    vChangeGiven = vChangeGiven + 10
    vChangeDue = vChangeDue - 10
    print("Giving out $10 coin")

while vChangeDue >= 5.0:
    vChangeGiven = vChangeGiven + 5.0
    vChangeDue = vChangeDue - 5.0
    print("Giving out $5 coin")

while vChangeDue >= 2.0:
    vChangeGiven = vChangeGiven + 2.0
    vChangeDue = vChangeDue - 2.0
    print("Giving out $2 coin")

while vChangeDue >= 1.0:
    vChangeGiven = vChangeGiven + 1.0
    vChangeDue = vChangeDue - 1.0
    print("Giving out $1 coin")

while vChangeDue >= 0.50:
    vChangeGiven = vChangeGiven + 0.50
    vChangeDue = vChangeDue - 0.50
    print("Giving out 50 cents")

while vChangeDue >= 0.20:
    vChangeGiven = vChangeGiven + 0.20
    vChangeDue = vChangeDue - 0.20
    print("Giving out 20 cents")

while vChangeDue >= 0.10:
    vChangeGiven = vChangeGiven + 0.10
    vChangeDue = vChangeDue - 0.10
    print("Giving out 10 cents")
