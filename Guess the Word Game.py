"""
import random

index = -1
words = str(input("Input a Word"))


words_len = len(words)
guess = ""
attempt = 0
enter = ""
print(words)
temp = "_" * words_len

print("\t\t The word chosen by computer contains", words_len,"letters.")
print("\t  Tap any letter to check if this letter is in computer word.\n")
print("\t You got 5 attempts to check if tapped letter is in computer word.\n")
print("\t\t\t\t GOOD LUCK!!!\n\n\n\n")

for i in range(0, 5):
    attempt +=1
    guess = input("Attempt no. "+str(attempt)+":")
    if guess in words and guess != enter:
        for i in range(0, words_len):
            if guess == words[i]:
                temp = temp[:i] + guess +temp[i+1:]
        print("yes\n" + temp)
    if guess not in words:
        print("no")
    if "_" not in temp:
        print("\t\t*********** Congratulation!! You guess the word *************")
        break
    elif attempt == 5:
        guess = input("And the word is:")
        if guess == words:

            print("\t\t*********** Congratulation!! You guess the word *************")
        else:
            print("\t\t*********** WRONG!! Shame on you *************")
"""
name = str("mike")
number = float(input("How many letters are in the word? It is between 2 and 15: "))
while number != 4:
    number = float(input("Guess again!"))
    if number > 4:
        print("You're wrong!")
        print("lower")
        number += 1
    if number < 4:
        print("You're wrong!")
        print("higher")
while number == 4:
    print("Good Job!")
    break
print("Now you know that there are 4 letters in the word!")
first_letter = str(input("Try guess the first letter of the word! What do you think it is?"))
while first_letter != "m":
    first_letter = str(input("guess again!"))
while first_letter == "m":
    print("Good JOB!!!! you got the first letter")
    break
guess = str(input("Do you want to try guess the word? You have one chance!"))
while guess != name:
    print("Oops! You can guess again after you find out the next letter!")
    break
