v_password = str(input("Please Input a Password: "))
passwordcheck=input("Please retype your password to confirm: ")
v_count = 1
while v_password != passwordcheck:
    print("Incorrect Password")
    print("You have tried: ", v_count, "time(s)")
    v_count += 1
    if v_count > 4:
        print("Sorry you have entered ", v_count, "times, you have been denied access")
        break
    else:
        v_password = str(input("Please Input Password Again: "))
else:
    print("Access has been granted, you have entered the system")
