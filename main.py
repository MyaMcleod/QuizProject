score = 0


# *** Ask for player name ***
player = input("*** What is your name? ***")


def yes_no(question):
    # *** Ask user if played before ***
    valid = False
    while not valid:
        response = input(question).lower().strip()
        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "No"
            return response
        else:
            print("*** Please choose yes or no! ***")


def instructions():
    # *** Game Instructions ***
    print("*** How to play *** ")
    print()
    print("*** Welcome to Zoot's basic maths! "
          "You will be learning math in 4 sections, each section has 5 questions. "
          "Remember to have fun! ZOOT ZOOT!*** ")
    print()
    return ""


def division():
    global score
    # *** Divison Questions ***
    print("*** We will start with the 5 division questions! ***")
    print("*** Question One! ***")
    answer = input("*** What is  4 divided by 2? *** ")
    if answer == "2":
        print("*** correct! ***")
        score += 1
    else:
        print("*** Incorrect, good try tho! ***")

    print("*** Question Two! ***")
    answer = input("*** What is  6 divided by 6? ***")
    if answer == "1":
        print("*** correct! ***")
        score += 1
    else:
        print("*** Incorrect, good try tho! ***")

    print("*** Question Three! ***")
    answer = input("*** What is  8 divided by 2? ***")
    if answer == "4":
        print("*** correct! ***")
        score += 1
    else:
        print("*** Incorrect, good try tho! ***")

    print("*** Question Four! ***")
    answer = input("*** 10 divided by 2? ***")
    if answer == "5":
        print("*** correct! ***")
        score += 1
    else:
        print("*** Incorrect, good try tho! ***")

    print("*** Question Five! ***")
    answer = input("*** 20 divided by 1? ***")
    if answer == "20":
        print("*** correct! ***")
        score += 1
    else:
        print("*** Incorrect, good try tho! ***")
        print("*** That's all the division questions, great work! ***")


def times():
    global score
    # *** Times Questions ***
    print("*** Next we will move on to the Times questions! ***")
    print("*** Question One! ***")
    answer = input("*** What is 8 times 2? ***")
    if answer == "16":
        print("*** correct! ***")
        score += 1
    else:
        print("*** Incorrect,good try tho! ***")

    print("*** Question Two! ***")
    answer = input("*** What is  5 times 5? ***")
    if answer == "25":
        print("*** correct! ***")
        score += 1
    else:
        print("*** Incorrect, good try tho! ***")

    print("*** Question Three! ***")
    answer = input("*** What is 3 times 4? ***")
    if answer == "6":
        print("*** correct! ***")
        score += 1
    else:
        print("*** Incorrect, good try tho! ***")

    print("Question Four! ")
    answer = input("*** What is 5 times 2? ***")
    if answer == "10":
        print("*** correct! ***")
        score += 1
    else:
        print("*** Incorrect, good try tho! ***")

    print("*** Question Five! ***")
    answer = input("*** What is 4 times 8? ***")
    if answer == "32":
        print("*** correct! ***")
        score += 1
    else:
        print("*** Incorrect, good try tho! ***")
        print("*** That's all the times questions, great work! ***")


def takeaway():
    global score
    # *** Takeaway Questions ***
    print("*** Next we will move on to the take away questions! ***")
    print("*** Question One! ***")
    answer = input("*** What is 8 take away 2? ***")
    if answer == "6":
        print("*** correct! ***")
        score += 1
    else:
        print("*** Incorrect,good try tho! ***")

    print("*** Question Two! ***")
    answer = input("*** What is 5 take away 5? ***")
    if answer == "0":
        print("*** correct! ***")
        score += 1
    else:
        print("*** Incorrect, good try tho! ***")

    print("*** Question Three! ***")
    answer = input("*** What is 3 take away 4? ***")
    if answer == "0":
        print("*** correct! ***")
        score += 1
    else:
        print("*** Incorrect, good try tho! ***")

    print("*** Question Four! ***")
    answer = input("*** What is 5 take away 2? ***")
    if answer == "3":
        print("*** correct! ***")
        score += 1
    else:
        print("*** Incorrect, good try tho! ***")

    print("*** Question Five! ***")
    answer = input("*** What is 4 take away 8? ***")
    if answer == "4":
        print("*** correct! ***")
        score += 1
    else:
        print("*** Incorrect, good try tho! ***")
        print("*** That's all the take away questions, great work! ***")


def addition():
    global score
    # *** addition Questions ***
    print("*** Lastly we will move on to Addition! ***")
    print("*** Question One! ***")
    answer = input("*** What is 7 plus 8? ***")
    if answer == "15":
        print("*** correct! ***")
        score += 1
    else:
        print("*** Incorrect,good try tho! ***")

    print("*** Question Two! ***")
    answer = input("What is 5 plus 5?")
    if answer == "10":
        print("*** correct! ***")
        score += 1
    else:
        print("*** Incorrect, good try tho! ***")

    print("*** Question Three! ***")
    answer = input("*** What is 6 plus 4? ***")
    if answer == "10":
        print("*** correct! ***")
        score += 1
    else:
        print("*** Incorrect, good try tho! ***")

    print("*** Question Four! ***")
    answer = input("*** What is 5 plus 3? ***")
    if answer == "8":
        print("*** correct! ***")
        score += 1
    else:
        print("*** Incorrect, good try tho! ***")

    print("*** Question Five! ***")
    answer = input("*** What is 4 plus 8? ***")
    if answer == "12":
        print("*** correct! ***")
        score += 1
    else:
        print("*** Incorrect, good try tho! ***")
        print("*** That's all the Addition questions, great work! ***")


# **** Main Routine *****
play = yes_no("*** Have you played the game before? ***")
play = play.strip().lower()

if play == "no" or play == "n":
    instructions()

else:
    print("*** Game starting ***")

# *** Calling the functions in order ***

instructions()
division()
times()
takeaway()
addition()

# *** Completed **
print(" *** You have completed the quiz! "
      "Congratulations {}! *** ".format(player))

 # *** Score Results ***
if score < 5:
    print("*** Good try!{} ***".format(player))
    print("*** But you could improve a little more! ***")
    print("*** You scored {} out of 20 ***".format(score))
elif score >= 5 <= 10:
    print("*** Good try!{} ***".format(player))
    print("*** You are are so close to half way! ***")
    print("*** You scored {} out of 20 ***".format(score))

elif score >= 10 <= 15:
    print("*** Good try!{} ***".format(player))
    print("*** You almost got them all correct! ***")
    print("*** You scored {} out of 20 ***".format(score))

elif score >= 15 <= 20:
    print("*** Good try!{} ***".format(player))
    print("*** You almost got them all correct! ***")
    print("*** You scored {} out of 20 ***".format(score))

elif score == 20:
    print("*** Good try!{} ***".format(player))
    print("*** You almost got them all correct! ***")
    print("*** You scored {} out of 20 ***".format(score))
