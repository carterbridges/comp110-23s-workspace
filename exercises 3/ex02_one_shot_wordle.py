"""One Shot Wordle, working with loops."""

__author__: "730563367"

SECRET: str = "python"
playing: bool = True
guess: str = str(input("What is your 6-letter guess? "))
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while playing :
    if guess == SECRET: 
        print("Woo! You got it! ")
        print(GREEN_BOX+GREEN_BOX+GREEN_BOX+GREEN_BOX+GREEN_BOX)
        playing: False
        exit()
    else:
        if len(guess) != len(SECRET):
            playing = True
            guess = str(input("That was not 6 letters! Try again: "))
        else:
            guess != SECRET and len(SECRET) == len(guess)
            print("Not quite. Play again soon! ")
            guess = str("Not quite. Play again soon! ")