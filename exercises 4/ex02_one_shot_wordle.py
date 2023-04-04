"""One Shot Wordle, working with loops"""

__author__: "730563367"

SECRET: str = "python"
playing: bool = True
guess: str = str(input("What is your 6-letter guess? "))
GREEN_BOX: str = "\U0001F7E9"
WHITE_BOX: str = "\U00002B1C"
YELLOW_BOX: str = "\U0001F7E8"

while playing:

    if guess == SECRET: 
        print("Woo! You got it! ")
        playing = False
        print(GREEN_BOX+GREEN_BOX+GREEN_BOX+GREEN_BOX+GREEN_BOX)
    else:
        if len(guess) != 6:
            playing = True
        else: #guess is 6 letters but not the word
            if guess[0] == SECRET [0]:
                print(GREEN_BOX)
            else:
                print(WHITE_BOX)
            if guess[1] == SECRET[1]:
                print(GREEN_BOX)
            else:
                print(WHITE_BOX)
            print("Not quite play again soon! ")
        
        guess = str(input("That was not 6 letters! Try again: "))