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
secretword = "hkis"
guesses = 0
guess =""
lettercount = len(secretword)
print("This word has", lettercount, " letters.")


while guess != secretword:
    guess = str(input("Guess a letter or the secret word:"))
    #input(guess)
    if guess == secretword:
        print("Well done! You got it! It was..", secretword, " You took:", guesses , " guesses.")

    elif guess in secretword:
        print ("Yeah! That letter ", guess ,"is in the word! That letter is in position..",
               (secretword.index(guess)+1))
        print("There is", secretword.count(guess))

    else:
        print("Sorry, that letter is not in the word.")
        guesses = guesses +1
