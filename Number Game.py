import random
print("\t Welcome to Guess my Number!")
print("************************************")
print("I am thinking of a number between 1 and 100. Can you guess it?")
number = random.randint(1,100)
guess = int(input("Choose a number between 1 and 100: "))
tries = 1
while guess != number:
    if guess > number:
        print("Your guess is too high")
        guess = int(input("Take a guess: "))
        tries += 1
    else:
        print("Your guess is too low")
        guess = int(input("Take a guess: "))
        tries += 1
print("You guessed it! The number was: ", number)
print("and you only took:", tries, " guesses! Well Done!")

input("\n\n Press Enter to Exit")
