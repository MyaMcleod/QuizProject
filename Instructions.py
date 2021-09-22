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

played_before = yes_no("Have you played the game before? ")

if played_before == "no" or played_before == "n" or played_before == "No":
        instructions()
else:
    print("*** Game starting ***")
