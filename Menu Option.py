def print_menu():
    print("1. Menu Option 1")
    print("2. Menu Option 2")
    print("3. Menu Option 3")

loop=True

while loop:
    print_menu()
    choice = str(input("Enter your choice; 1, 2, or 3: "))

    if choice=="1":
        print("Chosen Option 1")
    elif choice=="2":
        print("Chosen Option 2")
    elif choice=="3":
        print("Chosen Option 3")
        loop=False
    else:
        print("Wrong option selection. Try again:")
