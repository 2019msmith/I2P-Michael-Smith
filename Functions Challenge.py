"""
def max(a, b):

    if a < b:
        return a
    else:
        return b

print('Enter the first number')
aA = input()

print('Enter the second number')
bB = input()

print(str(max(aA,bB)) + ' is smaller')
"""
def largerValue(a, b):
    #DocString
    """ Function to find out the maximum of two numbers """

    if a > b:
        print(str(a) +'is larger than' + str(b))

    else:
        print (str(b) +' is larger than ' + str(a))


print ('Enter the first number')
aA = input()

print ('Enter the second number')
bB = input()

largerValue(aA,bB)
