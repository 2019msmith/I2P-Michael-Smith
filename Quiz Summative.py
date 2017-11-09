#defining time and allowing it to be set later on with the time.sleep command
import time

#defining the first fuction that introduces the quiz taker to the quiz
def intro():
#introducing a while loop to make it so that no matter what they want, they have to say 'y' in order to continue the quiz
    while True:
#defining a variable play and make it all lowercase in order to control the possible outputs, and then defining the possible solutions
        play = input("  Do you wanna take my quiz? Y or N?:\n")
        playy = str.lower(play)
#introducing an if/elif statement in order to give multiple outputs different outcomes
        if playy == "y":
            print ("\nGreat! Let's begin!\n\nThe rules are simple: I ask questions, and you answer them.\n\nI will keep score, and you will find out what your score is at the end of the quiz.\n\nGood Luck!")
            break
        if playy == "n":
            print("\nWell, you don't really have a choice")
        else:
            print("\nI'm sorry, I don't recognize your input. Press 'Y' if yes, and 'N' if no.")

#defining the function that asks the math questions
def math():
#setting mathscore = 0 so that for every right answer, they gain a point
    mathscore = 0
#setting mathscore1 equal to a string so that even if the quiz taker
    mathquestion1 = str(input("\nWhat is the answer to the following:\n\n5 * 8 - 4 / 4\n\n"))
    if mathquestion1 == "39":
        mathscore = mathscore + 1
        print("\nCorrect!")
    else:
        print("\nYou're off the goop on this one chief")
    mathquestion2 = str(input("\nWhat is the answer for the following, if x = 14:\n\nf(x) = (x + 4)(2x - 9)(x/7 - 2)\n\n"))
    if mathquestion2 == "0":
        mathscore = mathscore + 1
        print("\nCorrect!")
    else:
        print("\nYou done goofed")
    mathquestion3 = str(input("\nWhat is the answer for the following:\n\n50% of: 6 * 3 + 6 * 6\n\n"))
    if mathquestion3 == "27":
        mathscore = mathscore + 1
        print("\nCorrect!")
    else:
        print("\nWrong!")
    mathquestion4 = str(input("\nWhat is the answer for the following:\n\nThe square root of 144\n\n"))
    if mathquestion4 == "12":
        mathscore = mathscore + 1
        print("\nCorrect!")
    else:
        print("\nThat's quick maths! You should know better")
    mathquestion5 = str(input("\nWhat is the answer for the following:\n\n2 + 2 - 1\n\n"))
    if mathquestion5 == "3":
        mathscore = mathscore + 1
        print("\nCorrect!")
    else:
        print("\nBig Shaq would be disappointed")
    global finalmathscore
#calculating the final score for the math section
    finalmathscore = float(mathscore)/5 * 100
    print("\nOkay, you've finished the Math section, with a score of:\n\n", finalmathscore, "%!\n\nHopefully you're happy with you're score!\n")

#defining the function that asks the sports questions
def sports():
    sportsscore = 0
    sportsquestion1 = str(input("\nWhat is the answer for the following:\n\nWho was the MVP of the NBA in the 2016-2017 season?:\n\n1 for James Harden\n2 for LeBron James\n3 for Stephen Curry\n4 for Russell Westbrook\n5 for Giannis Antetokounmpo\n\n"))
    if sportsquestion1 == "4":
        sportsscore = sportsscore + 1
        print("\nCorrect!")
    else:
        print("\nOh no! No no no no no no no!")
    sportsquestion2 = str(input("\nWhat is the answer for the following:\n\nWhat European football team holds the record for the most Champions League Cup wins?:\n\n1 for Barcelona\n2 for Bayern Munich\n3 for Real Madrid\n4 for Juventus\n5 for Manchester United\n\n"))
    if sportsquestion2 == "3":
        sportsscore = sportsscore + 1
        print("\nCorrect!")
    else:
        print("\nWas that a serious attempt?")
    sportsquestion3 = str(input("\nWhat is the answer for the following:\n\nWhich team does the best Quarter Back in the NFL, Aaron Rodgers, play for?:\n\n1 for the New Orleans Saints\n2 for the Green Bay Packers\n3 for the Pittsburgh Steelers\n4 for the New York Giants\n5 for the New England Patriots\n\n"))
    if sportsquestion3 == "2":
        sportsscore = sportsscore + 1
        print("\nCorrect!")
    else:
        print("\nDo you even deserve to get a good score?")
    sportsquestion4 = str(input("\nWhat is the answer for the following:\n\nWhat baseball team in the MLB has the most World Series Titles?:\n\n1 for the New York Yankees\n2 for the San Francisco Giants\n3 for the Boston Red Sox\n4 for the Los Angeles Dodgers\n5 for the Houston Astros\n\n"))
    if sportsquestion4 == "1":
        sportsscore = sportsscore + 1
        print("\nCorrect!")
    else:
        print("\nYou're killing me, Smalls!")
    sportsquestion5 = str(input("\nWhat is the answer for the following:\n\nWho won the 2014 World Cup?\n\n1 for Argentina\n2 for Spain\n3 for Italy\n4 for France\n5 for Germany\n\n"))
    if sportsquestion5 == "5":
        sportsscore = sportsscore + 1
        print("\nCorrect!")
    else:
        print("\nYou ain't got the answers, Sway!")
    global finalsportsscore
    finalsportsscore = float(sportsscore)/5 * 100
    print("\nOkay, you've finished the Sports section, with a score of:\n\n", finalsportsscore, "%!\n\nHopefully you're happy with you're score!\n")

#defining the function that asks the history section
def history():
    historyscore = 0
    historyquestion1 = str(input("\nWhat is the answer for the following:\n\nIn what year did the American Revolution begin?:\n\n1 for 1776\n2 for 1902\n3 for 1802\n4 for 1783\n5 for 1765\n\n"))
    if historyquestion1 == "5":
        historyscore = historyscore + 1
        print("\nCorrect!")
    else:
        print("\nYou know that HKIS is an American school, right?")
    historyquestion2 = str(input("\nWhat is the answer for the following:\n\nWho was the Italian dictator during World War II?:\n\n1 for Benito Mussolini\n2 for Papa John\n3 for Gianluigi Buffon\n4 for Gianni Versace\n5 for Sergio Mattarella\n\n"))
    if historyquestion2 == "1":
        historyscore = historyscore + 1
        print("\nCorrect!")
    else:
        print("\nI can only respect a wrong answer if you picked Papa John")
    historyquestion3 = str(input("\nWhat is the answer for the following:\n\nAround what year was computer programming first implimented?:\n\n1 for 1944\n2 for 2011\n3 for 1998\n4 for 1492\n5 for 1973\n\n"))
    if historyquestion3 == "3":
        historyscore = historyscore + 1
        print("\nCorrect!")
    else:
        print("\nWe're in programming class! What have you been doing in class all this time?")
    historyquestion4 = str(input("\nWhat is the answer for the following:\n\nThe Magna Carta was published by the King of what country?\n\n1 for Italy\n2 for Franch\n3 for Spain\n4 for England\n5 for Germany\n\n"))
    if historyquestion4 == "4":
        historyscore = historyscore + 1
        print("\nCorrect!")
    else:
        print("\nYou should go back to 6th grade and ask for a history lesson!")
    historyquestion5 = str(input("\nWhat is the answer for the following:\n\nStephen Hawking was the creator of the equation E = MC^2, True or False?:\n\n1 for True\n2 for False\n\n"))
    if historyquestion5 == "2":
        historyscore = historyscore + 1
        print("\nCorrect!")
    else:
        print("\nGet out of my kitchen!")
    global finalhistoryscore
    finalhistoryscore = float(historyscore)/5 * 100
    print("\nOkay, you've finished the History section, with a score of:\n\n", finalhistoryscore, "%!\n\nHopefully you're happy with you're score!\n")

#defining the function that calls the previous functions, based on the choices of the quiz taker
def instructions():
    while True:
        firstsection = str(input("\nWhat section would you like to do first?\n\n1 for Math\n2 for Sports\n3 for History\n\n"))
        if firstsection == "1":
            math()
            while True:
                secondsection = str(input("\nWhat section would you like to do next?\n\n1 for Sports\n2 for History\n\n"))
                if secondsection == "1":
                    sports()
                    print("\nFinally, you will complete the History section!\n\nGood luck!\n")
                    history()
                    break
                elif secondsection == "2":
                    history()
                    print("\nFinally, you will complete the Sports section!\n\nGood luck!\n")
                    sports()
                    break
                else:
                    print("\nI'm sorry, you can only choose from 1 for Sports and 2 for History")
            break
        elif firstsection == "2":
            sports()
            while True:
                sectiontwo = str(input("\nWhat section would you like to complete next?\n\n1 for Math\n2 for History\n\n"))
                if sectiontwo == "1":
                    math()
                    print("\nFinally, you will complete the History section!\n\nGood Luck!\n")
                    history()
                    break
                elif sectiontwo == "2":
                    history()
                    print("\nFinally, you will complete the Math section!\n\nGood Luck!\n")
                    math()
                    break
                else:
                    print("\nI'm sorry, you can only choose from 1 for Math and 2 for History")
            break
        elif firstsection == "3":
            history()
            while True:
                sectionsecond = str(input("\nWhat section would you like to complete next?\n\n1 for Math\n2 for Sports\n\n"))
                if sectionsecond == "1":
                    math()
                    print("\nFinally, you will complete the Sports section!\n\nGood luck!\n")
                    sports()
                    break
                elif sectionsecond == "2":
                    sports()
                    print("\nFinally, you will complete the Math section!\n\nGood luck!\n")
                    math()
                    break
                else:
                    print("\nI'm sorry, you can only choose from 1 for Math or 2 for Sports")
            break
        else:
            print("\nI'm sorry, you can only pick from 1 for Math, 2 for Sports, or 3 for History")

#defining the function that tells the quiz taker what their final cumulative score is
def finalscore():
#making a variable that adds all the scores together and averages them to get a final cumulative score
    endscore = float(finalhistoryscore + finalmathscore + finalsportsscore)/3
    print("\nYour final cumulative score is: ", endscore, "%!\n\nI hope you're happy with your final score!\n")
    time.sleep(0.5)

#defining the function that tells the reader who I used as my sources
def sources():
    print("\nI didn't make this quiz completely on my own, I had the help of four different sources:\n\nMs. Mok,\nAditya Kalra,\nSarthak Bajpai, and\nBrian Chiang\n\nSpecial thanks to you guys for helping me get off the ground and get going with my code!\n~ Michael Smith")

#defining the function that asks the reader for their opinion and feeback on how I can improve the quiz
def feedback():
#making a while loop to weed out any bogus responses to my attempt to get feedback
    while True:
#opening a text file so that all scores out of five and their explanations are stored, so that I can see what the quiz takers thought of my quiz later on
        f = open("feedback", "a")
        honestfeedback = input("\nOkay " + name + ", now that you have taken my quiz, what did you think?\n 1 for terrible\n 2 for pretty bad\n 3 for decent\n 4 for pretty good\n 5 for amazing:\n\nWhat will it be?:\n")
        if honestfeedback == "1":
            f.write(honestfeedback)
            f.write("\n")
            f.write(str(input("\nOk, thank you for you honest feedback! Could you give an explanation for your score out of 5, so that I can know how to improve?\n\n")))
            f.write("\n\n")
            f.close()
            break
        elif honestfeedback == "2":
            f.write(honestfeedback)
            f.write("\n")
            f.write(str(input("\nOk, thank you for you honest feedback! Could you give an explanation for your score out of 5, so that I can know how to improve?\n\n")))
            f.write("\n\n")
            f.close()
            break
        elif honestfeedback == "3":
            f.write(honestfeedback)
            f.write("\n")
            f.write(str(input("\nOk, thank you for you honest feedback! Could you give an explanation for your score out of 5, so that I can know how to improve?\n\n")))
            f.write("\n\n")
            f.close()
            break
        elif honestfeedback == "4":
            f.write(honestfeedback)
            f.write("\n")
            f.write(str(input("\nOk, thank you for you honest feedback! Could you give an explanation for your score out of 5, so that I can know how to improve?\n\n")))
            f.write("\n\n")
            f.close()
            break
        elif honestfeedback == "5":
            f.write(honestfeedback)
            f.write("\n")
            f.write(str(input("\nOk, thank you for you honest feedback! Could you give an explanation for your score out of 5, so that I can know how to improve?\n\n")))
            f.write("\n\n")
            f.close()
            break
        else:
            print("\nPlease pick a number 1, 2, 3, 4, or 5 to reflect on how you feel about my quiz!\n")

#calling all the defined functions, after defining name and using it in a print command
print("Welcome to the General Knowledge Quiz!\n")
name = input("What's your name?:\n")
print("\nNice to meet you " + name + "! My name is Pennywise, we aren't strangers anymore!\n")
intro()
instructions()
finalscore()
sources()
feedback()

#allowing the quiz taker to take control of when they want to exit the quiz
input("\nPlease press enter to exit the quiz")
