#Defining Time
import time

#Intro
while True:
    name = input("\nWhat's your name?:\n")
    print(" Nice to meet you " + name + "! My name is Pennywise, we aren't strangers anymore!")
#Setting Time
    time.sleep(0.5)
#Defining First Variable
    play = input("  Do you wanna play The Wellcome Game? Y or N?:\n")
    playy = str.lower(play)
    if playy == "y":
#Choice0
        choice0 = input("\nGreat! Let's begin!\n I must warn you though, if you get a single question wrong, you will have to start over!\n  Are you SURE you want to play? Y or N?:\n")
        time.sleep(0.5)
        choice00 = str.lower(choice0)
        if choice00 == "n":
            print("\nThat was a test, and you failed.\n You died from being an absolute shrimp of a human being.")
            time.sleep(0.5)
        elif choice00 == "y":
            print("\nI like you already!\n Let's get going, shall we?")
            time.sleep(0.5)
            break
        else:
            print("\nI'm sorry, I don't recognize your input. Press 'Y' if yes, and 'N' if no.")
            time.sleep(0.5)
#Intro
    elif playy == "n":
        print("\nWell you're no fun")
        time.sleep(0.5)
    else:
        print("\nI'm sorry, I don't recognize your input. Press 'Y' if yes, and 'N' if no.")
        time.sleep(0.5)

while True:
#Choice1
    choice1 = input("\nYou wake up in Wellcome across the street from Hong Kong International School.\n For some reason, you cannot leave the store unless you buy the correct items.\n  Are you gonna buy something? Y or N?:\n")
    time.sleep(0.5)
    choice01 = str.lower(choice1)
    if choice01 == "y":

#Choice2
        choice2 = input("\nYou're smart! Ok, let's begin. Your walk into Aisle 1 and you only see two sections which you must choose from:\n Vegetables and Candy.\n  What's it gonna be? V for Veggies and C for Candy:\n")
        time.sleep(0.5)
        choice02 = str.lower(choice2)
        if choice02 == "c":

#Choice3
            choice3 = input("\nYou've got some adventure to you, I like that!\n Ok, so once you chose the Candy section, you obviously focus on ice cream because who doesn't like ice cream?\n  Ok back on topic, there are only two flavors: \n   Rocky Road and Vanilla.\n    What's it gonna be? R for Rocky Road and V for Vanilla:\n")
            time.sleep(0.5)
            choice03 = str.lower(choice3)
            if choice03 == "v":
#Choice4
                choice4 = input("\nHow did you know you were allergic to nuts? Oh well, on to the next scenario.\n You made it to the final choice! Congratulations!\n  After buying the vanilla ice cream in the Candy Section, you feel the urge to buy a pie to accompany it. Luckily, there are only two options to chose from: \n   Apple Pie and Shepherd's Pie.\n    What's it gonna be? A for Apple Pie and S for Shepherd's Pie:\n")
                time.sleep(0.5)
                choice04 = str.lower(choice4)
                if choice04 == "a":
#Choice5
                    choice5 = input("\nCongratulations! You survived the Wellcome Game!\n Click the 'Enter' key to go home and enjoy your Vanilla Ice Cream and Apple Pie with your lovely spouse and two corgis.\n  You could do that, or you could click 'A' to start again!\n   So what's it gonna be: Leave or Again?:\n")
                    time.sleep(0.5)
                    choice05 = str.lower(choice5)
                    if choice05 == "a":
                        print("\nI guess you really liked the Wellcome Game!")
                        time.sleep(0.5)
                    elif choice05 == "":
                        print("\nHave a nice life!")
                        time.sleep(0.5)
                        break
#Choice4
                elif choice04 == "s":
                    print("\nWhat kind of person are you to think that Shepherd's Pie goes with ice cream?\n You deserve to die!")
                    time.sleep(0.5)
                else:
                    print("\nI'm sorry, I don't recognize your input. Press 'A' if apple pie, and 'S' if shepherd's pie.")
                    time.sleep(0.5)
#Choice3
            elif choice03 == "r":
                print("\n You died from a nut allergy you had from birth.\n  How could you be so forgetful?")
                time.sleep(0.5)
            else:
                print("\nI'm sorry, I don't recognize your input. Press 'R' if rocky road, and 'V' if vanilla.")
                time.sleep(0.5)
#Choice2
        elif choice02 == "v":
            print("\nYou died from boredom. R.I.P.")
            time.sleep(0.5)
        else:
            print("\nI'm sorry, I don't recognize your input. Press 'V' if vegetables, and 'C' if candy.")
            time.sleep(0.5)
#Choice1
    elif choice01 == "n":
        print("\nYou died from not fulfilling your burning need to buy something.\n This is what happens when you don't listen to my instructions")
        time.sleep(0.5)
    else:
        print("\nI'm sorry, I don't recognize your input. Press y if yes, and n if no.")
        time.sleep(0.5)

#Feedback
def feedback():
    while True:
        rating = int(input("\nOkay " + name + ", now that you have played my game, what did you think?\n 1 for terrible\n 2 for pretty bad\n 3 for decent\n 4 for pretty good\n 5 for amazing:\n\nWhat will it be?:\n"))
        if rating == 1:
            feedback1 = input("\nI'm sorry my game sucked, what could I have done to make it better?:\n\n")
            if feedback1 == "cbdjskscdjkscndjkscndjsknkjncdjksnskjcnscdskjnscnsjkcnsjkcnsjkcds":
                print("\nThat's pretty lucky that you guessed this sequence. Gold star for you!")
                time.sleep(0.5)
            else:
                print("\nThanks for your feedback!\n Goodbye!")
                time.sleep(0.5)
            break
        elif rating == 2:
            feedback2 = input("\nI'm sorry it was that bad, what about the game do you think I can improve on?:\n\n")
            if feedback2 == "cbdjskscdjkscndjkscndj578217597892759837sknkjncdjksnskjcnscdskjnscnsjkcnsjkcnsjkcds":
                print("\nThat's pretty lucky that you guessed this sequence. Gold star for you!")
                time.sleep(0.5)
            else:
                print("\nThanks for your feedback!\n Goodbye!")
                time.sleep(0.5)
            break
        elif rating == 3:
            feedback3 = input("\nI'm just glad you didn't think it was terrible. What about the game do you think I can improve on?:\n\n")
            if feedback3 == "cbdjskscdjkscndjkscndjs3297589759169knkjncdjksnskjcnscdskjnscnsjkcnsjkcnsjkcds":
                print("\nThat's pretty lucky that you guessed this sequence. Gold star for you!")
                time.sleep(0.5)
            else:
                print("\nThanks for your feedback!\n Goodbye!")
                time.sleep(0.5)
            break
        elif rating == 4:
            feedback4 = input("\nThat's pretty good! Is there anything about the game you think I could improve on?:\n\n")
            if feedback4 == "cbdjskscdjkscndjkscndjsknkjnc3783497598375159174djksnskjcnscdskjnscnsjkcnsjkcnsjkcds":
                print("\nThat's pretty lucky that you guessed this sequence. Gold star for you!")
                time.sleep(0.5)
            else:
                print("\nThanks for your feedback!\n Goodbye!")
                time.sleep(0.5)
            break
        elif rating == 5:
            print("\nThat's great! Thanks for your input!")
            time.sleep(0.5)
            break
        else:
            print("\nI'm sorry, I only accept the answers: 1, 2, 3, 4, or 5. No decimals, negative numbers, or anything fancy, please!")
            time.sleep(0.5)

feedback()
