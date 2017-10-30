def fq():
    a=str(input("Would you like a mars bar? Y or N?: "))
    if a==str.upper("y"):
        print("Here is your mars bar")
    elif a==str.lower("y"):
        print("Here is your mars bar")
    elif a==str.upper("n"):
        print("No mars bar for you")
    elif a==str.lower("n"):
        print("No mars bar for you")
    else:
        print("I'm sorry I don't recognize your answer")
        fq()

fq()
