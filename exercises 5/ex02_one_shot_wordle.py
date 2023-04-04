"""One Shot Wordle, working with loops."""

__author__: "730563367"

SECRET: str = "python"
playing: bool = True
guess: str = str(input("What is your 6-letter guess? "))

while playing:
    if guess == SECRET:
        print("Woo! You got it! ")
        playing = False
    else:
        if len(guess) != 6:
            guess = str(input("That was not 6 letters! Try again: "))
        else:
            print("Not quite. Play again soon! ")
            playing = False