score = 0


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


addition()
