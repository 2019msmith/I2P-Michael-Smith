num = 12
for i in range(1, 12):
   print(num,'x',i,'=',num*i)

num = int(input("Pick a number: "))
for i in range (0,13):
    print(num,'x',i,'=', num*i)

name = input("What's your name?: ")
print("Nice to meet you " + name + "! My name is Pennywise, we aren't strangers anymore!")
age = int(input("How old are you?: "))
if age < 18:
    print("So, you are " + str(age) + " years old, " + name + "! Sadly, you are too young to legally drink alcohol in Hong Kong. Try again next year!")
if age > 18:
    print("So, you are already " + str(age) + " years old, "+ name + "! You can legally drink alcohol in Hong Kong!")
print("Dude, you've been alive for", int(age)*365, "days! You're ancient! Remember to write your will!")
days = int(age)*365
print("Jeeze, you've been around for", int(days)*24, "hours! That's mental! But check this out...")
print("You've been on this Earth for", int(days)*3600, "seconds! Stop wasting your seconds reading this, go out and experience the world!")
