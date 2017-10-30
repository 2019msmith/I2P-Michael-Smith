def fPrintSummary():

    print()
    print("TRANSACTION SUMMARY MY FUNCTION")
    print("Price of Chocolate:",vPrice)
    print("Cash Paid:",vCash)
    print("Change Due:",round(vChangeDue,2))
    print("Total Change Given:",vChangeGiven)
    print()

def fdispenseCoin(coin):
    global vChangeGiven
    global vChangeDue

    while vChangeDue >= coin:
        vChangeGiven = vChangeGiven + coin

