score = 0

def instructions():
    # Ask user if they have played before
    show_instructions = input("Have you played before?").lower()

    # if they say yes, output 'program  contiune'
    if show_instructions == "yes" or show_instructions == "y":
        print("Program continues!")

    # if they say No, output 'program  contiune'
    if show_instructions == "no" or show_instructions == "n":
        print("Welcome to Zoot's basic maths! You will be learning math in 4 sections, each section has 5 questions. Remeber to have fun! ZOOT ZOOT!")

    # if they say other, output 'Please answer the question'
    elif show_instructions == "maybe":
        print("Please answer the question with yes or no!")


def divsion():
    score = 0
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
    score = 0
    print("Next we will move on to the Times questions questions!")
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


instructions()
divsion()
times()
