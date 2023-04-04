"""One Shot Wordle, working with loops."""

__author__: "730563367"

SECRET: str = "python"
playing: bool = True
guess: str = str(input("What is your 6-letter guess? "))
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
count = 0
emoji: str = ""

while playing:
    if guess == SECRET:
        print("Woo! You got it! ")
        print(GREEN_BOX+GREEN_BOX+GREEN_BOX+GREEN_BOX+GREEN_BOX+GREEN_BOX)
        playing = False
    else:
        if len(guess) != 6:
            guess = str(input("That was not 6 letters! Try again: "))
        else:
            while count < 6:
                if guess[int(count)] == SECRET[int(count)]:
                    emoji = emoji + GREEN_BOX
                else:
                    emoji = emoji + WHITE_BOX
                count = count + 1
            print(emoji)
            print("Not quite. Play again soon! ")
            playing = False

