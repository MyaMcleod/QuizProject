

def name():
# *** Ask for player name ***
    player = input("What is your name? ")


def yes_no(question):
# *** Ask user if played before ***
    valid = False
    while not valid:
        response = input(question).lower().strip()
        if response == "yes" or response == "y":
            response = "yes"
            return  response

        elif response == "no" or response == "n":
            response = "No"
            return response
        else:
            print("Please choose yes or no!")


def instructions():
# *** Game Instructions ***
    print("*** How to play *** ")
    print()
    print("*** Welcome to Zoot's basic maths! "
          "You will be learning math in 4 sections, each section has 5 questions. "
          "Remember to have fun! ZOOT ZOOT!*** ")
    print()
    return ""


def division(score=0):
# *** Divison Questions ***
        print("We will start with the 5 division questions!")
Question = ["What is  4 divided by 2?","What is  6 divided by 6?"," What is  8 divided by 2?"," 10 divided by 2?",
             "20 divided by 1?"]
Answer = ["2","1","4","5","20"]

question_num = 0
for i in Question:
    answer_input = input(Question[question_num])
    if answer_input == Answer[question_num]:
        print("correct")
        question_num += 1


def times():
# *** Times Questions ***
    print("Next we will move on to the Times questions!")
    print("Question One! ")
    answer = int(input("What is 8 times 2?"))
    if answer == 16:
        print("correct!")
        score += 1
    else:
        print("Incorrect,good try tho!")

    print("Question Two! ")
    answer = int(input("What is  5 times 5?"))
    if answer == 25:
        print("correct!")
        score += 1
    else:
        print("Incorrect, good try tho!")

    print("Question Three! ")
    answer = int(input(" What is 3 times 4?"))
    if answer == 6:
        print("correct!")
        score += 1
    else:
        print("Incorrect, good try tho!")

    print("Question Four! ")
    answer = int(input(" What is 5 times 2?"))
    if answer == 10:
        print("correct!")
        score += 1
    else:
        print("Incorrect, good try tho!")

    print("Question Five! ")
    answer = int(input(" What is 4 times 8?"))
    if answer == 32:
        print("correct!")
        score += 1
    else:
        print("Incorrect, good try tho!")
        print("That's all the times questions, great work!")


def takeaway():
# *** Takeaway Questions ***
    score = 0
    print("Next we will move on to the take away questions!")
    print("Question One! ")
    answer = int(input("What is 8 take away 2?"))
    if answer == 6:
        print("correct!")
        score += 1
    else:
        print("Incorrect,good try tho!")

    print("Question Two! ")
    answer = int(input("What is 5 take away 5?"))
    if answer == 0:
        print("correct!")
        score += 1
    else:
        print("Incorrect, good try tho!")

    print("Question Three! ")
    answer = int(input(" What is 3 take away 4?"))
    if answer == 0:
        print("correct!")
        score += 1
    else:
        print("Incorrect, good try tho!")

    print("Question Four! ")
    answer = int(input(" What is 5 take away 2?"))
    if answer == 3:
        print("correct!")
        score += 1
    else:
        print("Incorrect, good try tho!")

    print("Question Five! ")
    answer = int(input(" What is 4 take away 8?"))
    if answer == 4:
        print("correct!")
        score += 1
    else:
        print("Incorrect, good try tho!")
        print("That's all the take away questions, great work!")


def addition():
# *** addition Questions ***
    score = 0
    print("Lastly we will move on to Addition!")
    print("Question One! ")
    answer = int(input("What is 7 plus 8?"))
    if answer == 15:
        print("correct!")
        score += 1
    else:
        print("Incorrect,good try tho!")

    print("Question Two! ")
    answer = int(input("What is 5 plus 5?"))
    if answer == 10:
        print("correct!")
        score += 1
    else:
        print("Incorrect, good try tho!")

    print("Question Three! ")
    answer = int(input(" What is 6 plus 4?"))
    if answer == 10:
        print("correct!")
        score += 1
    else:
        print("Incorrect, good try tho!")

    print("Question Four! ")
    answer = int(input(" What is 5 plus 3?"))
    if answer == 8:
        print("correct!")
        score += 1
    else:
        print("Incorrect, good try tho!")

    print("Question Five! ")
    answer = int(input(" What is 4 plus 8?"))
    if answer == 12:
        print("correct!")
        score += 1
    else:
        print("Incorrect, good try tho!")
        print("That's all the Addition questions, great work!")


def score():
# *** Score Results ***
    if score >= 0 <= 5:
        print("Good try!{}".format(name))
        print("But you could improve a little more!")
        print("You scored {} out of 20".format(score))
    elif score >= 5 <= 10:
        print("Good try!{}".format(name))
        print("You are are so close to half way!")
        print("You scored {} out of 20".format(score))

    elif score >= 10 <= 15:
        print("Good try!{}".format(name))
        print("You almost got them all correct!")
        print("You scored {} out of 20".format(score))

    elif score >= 15 <= 20:
        print("Good try!{}".format(name))
        print("You almost got them all correct!")
        print("You scored {} out of 20".format(score))

    elif score == 20:
        print("Good try!{}".format(name))
        print("You almost got them all correct!")
        print("You scored {} out of 20".format(score))



# **** Main Routine *****
play = yes_no("Have you played the game before? ")
play = play.strip().lower()

if play == "no" or play == "n":
    instructions()

else:
    print("*** Game starting ***")

# *** Calling the functions in order ***
name()
instructions()
division()
times()
takeaway()
addition()

# *** Completed **
print(" *** You have completed the quiz!"
      "Congratulations {}! *** ".format(player))
