score = 0


def name():
    name = input("What is your name? ")


def yes_no(question):
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
    print("*** How to play ***")
    print()
    print("*** Welcome to Zoot's basic maths! "
          "You will be learning math in 4 sections, each section has 5 questions."
          " Remeber to have fun! ZOOT ZOOT!***")
    print()
    return ""

play = yes_no("Have you played the game before? ")

if play == "no" or play == "n" or play == "No":
        instructions()
else:
    print("*** Game starting ***")

def division():
    print("We will start with the 5 division questions!")
    print("Question One! ")
    answer = int(input("What is  4 divided by 2?"))
    if answer == 2:
        print("correct!")
        score += 1
    else:
        print("Incorrect, good try tho!")

    print("Question Two! ")
    answer = int(input("What is  6 divided by 6?"))
    if answer == 1:
        print("correct!")
        score += 1
    else:
        print("Incorrect, good try tho!")

    print("Question Three! ")
    answer = int(input(" What is  8 divided by 2?"))
    if answer == 4:
        print("correct!")
        score += 1
    else:
        print("Incorrect, good try tho!")

    print("Question Four! ")
    answer = int(input(" 10 divided by 2?"))
    if answer == 5:
        print("correct!")
        score += 1
    else:
        print("Incorrect, good try tho!")

    print("Question Five! ")
    answer = int(input(" 20 divided by 1?"))
    if answer == 20:
        print("correct!")
        score += 1
    else:
        print("Incorrect, good try tho!")
        print("Thats all the division questions, great work!")


def times():
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
        print("Thats all the times questions, great work!")


def takeaway():
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
        print("Thats all the take away questions, great work!")


def addition():
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
        print("Thats all the Addition questions, great work!")


def score():
    score


name()
instructions()
division()
times()
takeaway()
addition()
