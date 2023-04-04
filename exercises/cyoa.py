"""Choose your own adventure game. Travel through time."""

__author__ = "730563367"

points: int = 0
# 1 point is added everytime the player steps through a new portion of the game (when they make a decision)
player: str = ""
# Player name from their input
BAD_EMOJI: str = "\U0001F7E5"
GOOD_EMOJI: str = "\U0001F7E9"


def main() -> None:
    """Main function."""
    greet()
    global points
    points = 0
    playing = True
    while playing is True:
        if playing is True: 
            print(f"Your point total is {points}. ")
            print(f"{player}, you have the choice to go to three different time periods, 1941, 1863, or 1775. Make your choice. ")
            userinput = input(f"Please choose one of the following for your time period, 1941/1863/1775. {GOOD_EMOJI}: ")
        if userinput == "1941":
            playing_1 = True
            print(f"You are in Germany, the year is 1941, you are an infantry solider for the U.S. Army. Good luck solider. {GOOD_EMOJI}")
            while playing_1 is True:
                world_war = input(f"{player}, Do you want to drive a tank or fly an airplane?: ")
                if world_war == "tank":
                    print(f"You have became a tank driver, good luck. That is 10 points since it is very dangerous. {GOOD_EMOJI}")
                    points += 10
                    another_choice = input("Would you like to attack the enemy or prey on them from far away: ")
                    if another_choice == "attack":
                        print(f"You defeted the enemy, well done solider! That is 50 points! {GOOD_EMOJI}")
                        points += 50
                    if another_choice == "prey" or "prey on them" or "prey on them from far away":
                        print(f"A German fighter plane found you and wiped out the whole platoon, Sorry solider. 0 points. {BAD_EMOJI}")
                        points += 0
                playing_1 is False
                if world_war == "airplane":
                    print(f"You have became an airplane pilot, good luck. That is 5 points. {BAD_EMOJI}")
                    points += 5
                    airplane_choice = input("Would you like to attack the enemy or prey on them from far away: ")
                    if airplane_choice == "attack":
                        print(f"You defeted the enemy, well done solider! That is 50 points! {GOOD_EMOJI}")
                        points += 50
                    if airplane_choice == "prey" or "prey on them" or "prey on them from far away":
                        print(f"A German fighter plane found you and wiped out the whole platoon, Sorry solider. 0 points. {BAD_EMOJI}")
                        points += 0
            playing_1 is False
        if userinput == "1863":
            playing_2 = True
            print("You are in the southern United States fighting for the Union Army in the civil war. ")
            while playing_2 is True:
                civil_war = input(f"{player}, Do you want to be in Virginia or New York?: ")
                if civil_war == "Virginia" or "virginia":
                    print("You are stationed as an infantry solider for the Union Army in Virginia, this is a hard job and very dangerous. You gained 30 points. ")
                    points += 30
                    another_choice_1 = input("Would you like to be on the front lines of stay behind?: ")
                    if another_choice_1 == "front lines":
                        print(f"Great decision. Thanks to you and your group the Union Army had a decisive win over the confederacy. You gained 20 points. {GOOD_EMOJI}")
                        points += 20
                    if another_choice_1 == "stay behind": 
                        print(f"The army needed you today and lost a key battle, dissappointed solider. 0 Points. {BAD_EMOJI}")
                        points += 0
                playing_2 is False
                if civil_war == "New York" or "new york":
                    print(f"You are stationed in upstate New York. The conditions are tough but this could be very rewarding for the Union. 40 points. {GOOD_EMOJI}")
                    points += 30
                    new_york_choice = input("Great decision this will be awesome for the Army. Do you want to go to the front lines or stay behind?: ")
                    if new_york_choice == "front lines:":
                        print(f"Poor decision, it actually turned out to be a bad loss for the Union Army. 0 Points. {BAD_EMOJI}")
                        points += 0
                    if new_york_choice == "stay behind":
                        print(f"That was a good decision. The entire Army almost got wiped out and you would have been too. 20 points. {GOOD_EMOJI}")
                        points += 20
            playing_2 is False
        if userinput == "1775":
            playing_3 = True
            while playing_3 is True:
                rev_war = input(f"{player}, Do you want to be George Washington or Paul Revere?: ")
                if rev_war == "George" or "George Washington":
                    print(f"You are the leader of the colonial army. Go defeat the British. For such a great choice you gained 75 points! {GOOD_EMOJI}")
                    points += 75
                    another_choice_2 = input("Would you like to take your army across the Delaware River? Yes or No?: ")
                    if another_choice_2 == "Yes" or "yes":
                        print(f"Great decision, this was the right move and you caught the British by surprise! Plus 20 points! {GOOD_EMOJI}")
                        points += 20
                    if another_choice_2 == "no" or "No": 
                        print(f"The British had time to prepare and beat you. Move on to the next battle. Plus 0 points. {BAD_EMOJI}")
                        points += 0
                playing_3 is False
                if rev_war == "Paul" or "Paul Revere":
                    print(f"You have a pivotal role in letting the minutemen know the British are coming. Get on it! Plus 40 points. {GOOD_EMOJI} ")
                    points += 40
                    paul_revere_choice = input("Will you go and warn everyone that the British are coming? Yes or no?: ")
                    if paul_revere_choice == "Yes" or "yes":
                        print(f"Great decision, the minute men knew to get ready. Plus 60 points! {GOOD_EMOJI}")
                        points += 60
                    if paul_revere_choice == "no" or "No":
                        print(f"We wish you would have warned us, the British were upon us in no time. 0 points. {BAD_EMOJI} ")
                        points += 0
            playing_3 is False
        playing is False
    print(f"Thanks for playing. You did great. Your final score was: {points}. {GOOD_EMOJI}")
    end_score()
    player_performance()


def greet() -> None:
    """Greeting function."""
    print("Welcome to Adventure Through Time, an interactive game where you choose where you want to go back in time! What is your name? ")
    global player
    player = input("Print your name here: ")
    print(f"{player}, Welcome, your game is about to start. ")
    

def end_score(score: int = 0) -> int:
    """End score function."""
    global points
    points = score
    print(points)


def player_performance() -> None:
    """Player performance function."""
    global points
    if points < 70:
        print("Good try but you did not choose the right tasks to complete the game and win. ")
    if points > 70:
        print("Great job you completed the game and won! ")


if __name__ == "__main__":
    main()