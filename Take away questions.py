def takeaway():
    score = 0
    print("Next we will move on to the take awayquestions!")
    print("Question One! ")
    answer = int(input("What is 8 takeaway 2?"))
    if answer == 6:
        print("correct!")
        score += 1
    else:
        print("Incorrect,good try tho!")

    print("Question Two! ")
    answer = int(input("What is  5 takeaway 5?"))
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
    answer = int(input(" What is 5 takeaway 2?"))
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
        print("Thats all the takeaway questions, great work!")



takeaway()
