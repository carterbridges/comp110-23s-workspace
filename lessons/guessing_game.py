"""Asks user for a number, goes until they get it right"""

SECRET: int = 4
guess: int = int(input("Guess a number! "))
playing: bool = True
number_of_guesses: int = 0

while playing and number_of_guesses < 3: 
    
    if guess == SECRET: 
        print("Yay, you got it right! ")
        playing = False
    else: 
        print("Wrong number. :(")
        if guess % 2 == 1: #guess is odd
            print("Your guess is an odd number, the answer is even. ")
        if guess > SECRET:
            print("Your guess is too high. ")
        else: #guess < secret
            print("Your guess is too low. ")
        guess = int(input("Make another guess! "))
    
    