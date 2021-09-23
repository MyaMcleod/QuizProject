play = yes_no("Have you played the game before? ")

if play == "no" or play == "n " or play == "No ":
    instructions()

else:
    print("*** Game starting ***")
