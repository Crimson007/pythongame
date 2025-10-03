# Simple Dice Game

# Provided die roll 
first_dice_roll = 1

print("Welcome to the Dice Game")
play_choice = input("Would you like to play? (yes/no) ")

if play_choice == "yes":
    print("Great! Let's play...")
    # We'll add the game logic in next stage
elif play_choice == "no":
    print("Okay you don't want to play. Game Over.")
else:
    print("Invalid input. Game Over.")
    