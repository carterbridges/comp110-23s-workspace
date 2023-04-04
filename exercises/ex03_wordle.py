"""Finished wordle. """

__author__ = "730563367"

def contains_char(long_string: str, single_char: str) -> bool:
    """when given two strings, the first of any length, the second a single character, returns true if character in second string is in first string"""
    assert len(single_char) == 1
    count: int = 0
    while count < len(long_string):
        if long_string[int(count)] == single_char:
            return True
        else:
           count = count + 1 
    return False

def emojified(guess: str, secret: str) -> str:
    """Returns emojis as a string using contains_char to see if a single character is within the long string"""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    count: int = 0
    emojis: str = ""
    count_secret: int = 0
    while count < len(secret):
        if contains_char(secret, guess[count]) == True:
            if secret[int(count_secret)] == guess[int(count)]:
                emojis = emojis + GREEN_BOX
                count_secret = count_secret + 1
            else:
                emojis = emojis + YELLOW_BOX
                count_secret = count_secret + 1 
        if contains_char(secret, guess[count]) == False:
            emojis = emojis + WHITE_BOX
            count_secret = count_secret + 1
        count = count + 1
    return emojis

def input_guess(nbr: int) -> str:
    """Given an integer “expected length” of a guess as a parameter, it will prompt the user for a guess and continue prompting them until they provide a guess of the expected length."""
    guess: str = str(input(f"Enter a {nbr} character word: "))
    while len(guess) != nbr:
            guess = str(input(f"That wasn't {nbr} chars! Try again: "))
    return guess

def main() -> None:
    """The entrypoint of the program and main game loop."""
    SECRET: str = "codes"
    guess_count: int = 1
    won: bool = False
    while guess_count < 7 and won == False:
        print(f"=== Turn {guess_count}/6")
        guess = input_guess(5)
        print(emojified(guess, SECRET))
        if guess == SECRET:
            print(f"You won in {guess_count}/6 turns! ")
            won = True
        else:
            guess_count = guess_count + 1
    if won == False:
        print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()