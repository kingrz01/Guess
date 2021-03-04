def game():
    '''Game for guessing three numbers at random'''
    import random
    digits = list(range(10))
    random.shuffle(digits)
    y=digits[:3]
    game_on = True
    print('Guess 3 numbers and try to understand the guess made by the game!')
    while game_on:
                
        guess = input("\nWhat is your guess? ")

        while len(guess) !=3 or guess[0]==guess[1] or guess[0]==guess[2] or guess[1]==guess[2]:
            guess = input("\nWrong input! There must be 3 different. Try again!\nWhat is your guess? ")
        counter = 0      
        for x in guess:
            if int(x) in y:
                counter += 1
        if counter == 0:
            print("\nNope: You haven't guess any of the numbers correctly. Guess again!")
        elif counter == 3:
            if ''.join(map(str,y)) == guess:
                print("\nFull Match: You've guessed ALL the correct numbers in the correct position!\nYOU HAVE WON!")
                game_on = False
            else:
                print("\nClose: You've guessed the correct numbers but in the wrong order. Guess again!")
        elif counter == 1:
            if guess[0] == str(y[0]) or guess[1] == str(y[1]) or guess[2] == str(y[2]):
                print("\nOne match: You've guessed one correct number in the correct position. Guess again!")
            else:
                print("\nClose: You've guessed one correct number but in the wrong position. Guess again!")
        else:
            if (guess[0] == str(y[0]) and guess[1] == str(y[1])) or (guess[0] == str(y[0]) and guess[2] == str(y[2])) or (guess[1] == str(y[1]) and guess[2] == str(y[2])):
                print("\nDouble match: You've guessed two correct numbers and all in the correct position. Guess again!")
            elif guess[0] == str(y[0]) or guess[1] == str(y[1]) or guess[2] == str(y[2]):
                print("\nClose double match: You've guessed two numbers and one in the correct position. Guess again!")
            else:
                print("\nClose double match: You've guessed two numbers but in the wrong position. Guess again!")

game()
