def instructions():

        #Ask user if they have played before
    show_instructions = input("Have you played before?").lower()

    #if they say yes, output 'program  contiune'
    if show_instructions == "yes" or show_instructions == "y":
        print("Program continues!")

    #if they say No, output 'program  contiune'
    if show_instructions == "no" or show_instructions == "n":
        print("Welcome to Zoot's basic maths! You will be learning math in 4 sections, each section has 5 questions. Remeber to have fun! ZOOT ZOOT!")

    #if they say other, output 'Please answer the question'
    elif show_instructions == "maybe":
        print("Please answer the question with yes or no!")



instructions()
