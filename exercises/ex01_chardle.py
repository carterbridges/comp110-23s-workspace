"""EX01 - Chardle - A Cute Step Towards Wordle."""
__author__ = 730563367

Characters_count: int = 0

word: str = input("Enter a 5 letter word ")
if len(word) != 5:
    print("Error: word must have 5 characters")
    exit()

character_guess: str = input("Enter one character. ")
if len(character_guess) != 1:
    print("Error, enter one character. ")
    exit()
else: len(character_guess) == 1

print("Search for " + character_guess + " in " + word)

count: int = 0 

if word[0] == character_guess:
    print(character_guess + " found at index " + "0")
    count = count + 1

if word[1] == character_guess:
    print(character_guess + " found at index " + "1")
    count = count + 1

if word[2] == character_guess:
    print(character_guess + " found at index " + "2")
    count = count + 1

if word[3] == character_guess:
    print(character_guess + " found at index " + "3")
    count = count + 1

if word[4] == character_guess:
    print(character_guess + " found at index " + "4")
    count = count + 1

if count == 0:
    print("No instances of " + character_guess + " found in " + word)

if count == 1:
    print("1 instance of " + character_guess + " found in " + word)

if count == 2: 
    print("2 instances of " + character_guess + " found in " + word)

if count == 3: 
    print("3 instances of " + character_guess + " found in " + word)

if count == 4: 
    print("4 instances of " + character_guess + " found in " + word)

if count == 5: 
    print("5 instances of " + character_guess + " found in " + word)

# Could I typecast on the 2 above if statements?
# Ex. print(str(count)+ "instances of " .....)