def score():
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


name = "Jeff"
