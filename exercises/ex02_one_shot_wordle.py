"""One Shot Wordle, working with loops."""

__author__ = "730563367"

SECRET: str = "python"
playing: bool = True
guess: str = str(input("What is your 6-letter guess? "))
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
count = 0
emoji: str = ""
character_within_word: bool = False
count_of_secret = 0

while playing:  # 1st while loop (everything is under this one)
    if guess == SECRET:
        print("Woo! You got it! ")
        print(GREEN_BOX + GREEN_BOX + GREEN_BOX + GREEN_BOX + GREEN_BOX + GREEN_BOX)  # concatanates 6 greenboxes since this will always be the right guess is guess = secret
        playing = False
    else:
        if len(guess) != 6:  # need 6 letters as an input so we can continue to see which letters are right, wrong, or in the wrong place
            guess = str(input("That was not 6 letters! Try again: "))
        else:
            while count < 6:  # adds green emojis (boxes) while repeating in the while loop until the length is 6
                if guess[int(count)] == SECRET[int(count)]:
                    emoji = emoji + GREEN_BOX
                else:
                    character_within_word = False
                    count_of_secret = 0
                    while count_of_secret < 6 and character_within_word == True:  # puts limit at 6 so it will only print 6 boxes and not go on forever
                        if guess[int(count)] == SECRET[int(count_of_secret)]:
                            character_within_word = True
                        else: 
                            count_of_secret = count_of_secret + 1
                    if character_within_word == True:  # if the character at an index is within the guess and the SECRET variables but it is not at the correct index in context of out SECRET word
                        emoji = emoji + YELLOW_BOX
                    else:  # if the chacter at a certain index is not within the word established as out SECRET variable
                        emoji = emoji + WHITE_BOX
                count = count + 1
            print(emoji)
            print("Not quite. Play again soon! ")
            playing = False