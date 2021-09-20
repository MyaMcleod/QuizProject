
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

times()
