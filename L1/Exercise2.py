import random

play = True
while play:
    fail = True;
    randNum = random.randint(0, 9) + 1
    tries = 0
    while fail:

        try:
            userInput = input("Guess the random number [1-9] (Enter 'exit' to quit) ")
            if userInput == "exit":
                break
            num = int(userInput)
            if num == randNum :
                print("You're exactly right.!!")
                tries = tries + 1
                fail = False
            else:
                if num > randNum:
                    print("Too high, try again. ")
                elif num < randNum:
                    print("Too low, try again. ")
                tries = tries + 1
        except:
            print("Invalid input")

    if fail:
        print("You lose in " + str(tries) + " tries.")
    else:
        print("You won in " + str(tries) + " tries.")

    userInput = input("Press any key to continue. (Enter 'exit' to leave the game) ")
    if userInput == "exit":
        play = False
    else:
        play = True