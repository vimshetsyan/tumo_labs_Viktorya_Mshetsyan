import random


def roll_dice():
    return random.randint(1, 6), random.randint(1, 6)


def play_game():
    roll1, roll2 = roll_dice()
    sum_of_rolls = roll1 + roll2
    print(f"You rolled {roll1} + {roll2} = {sum_of_rolls}")

    if sum_of_rolls == 7 or sum_of_rolls == 11:
        print("You win!")
    elif sum_of_rolls == 2 or sum_of_rolls == 3 or sum_of_rolls == 12:
        print("Casino wins!")
    else:
        print(f"{sum_of_rolls} is your goal.")
        goal = sum_of_rolls
        while True:
            roll1, roll2 = roll_dice()
            sum_of_rolls = roll1 + roll2
            print(f"You rolled {roll1} + {roll2} = {sum_of_rolls}")
            if sum_of_rolls == 7:
                print("You lose!")
                break
            elif sum_of_rolls == goal:
                print("You win!")
                break


while True:
    input("Press enter to roll the dice!")
    play_game()
    if input("If you wanna play again press (y)\n").lower() != "y":
        break

print("Thanks for playing!")
