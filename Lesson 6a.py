def fsum():
    int1 = int(input("What should your first number be?: "))
    int2 = int(input("What should your second number be?: "))
    vtotal = int1 + int2
    return vtotal


# print(fsum())

def f_print_largest(int11, int22):
    if int11 > int22:
        print(int11, "is larger")
    elif int11 < int22:
        print(int22, "is larger")


f_print_largest(14, 20)

