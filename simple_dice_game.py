# Simple Dice Game

# Provided die roll 
first_dice_roll = 1

print("Welcome to the Dice Game")
play_choice = input("Would you like to play? (yes/no) ")

if play_choice == "yes":
    # Get bet amount and convert to integer
    bet = int(input("How much would you like to bet? (enter an integer less than or equal to 100) "))
    
    # Check if bet is valid (must be <= 100)
    if bet > 100:
        print("Sorry, bet is too much. Game Over.")
    else:
        # Show potential winnings
        potential_win = bet * 2
        print(f"If you guess correctly you win {potential_win}")
        
        # Get the guess and convert to integer
        guess = int(input("A six sided die will be rolled. Guess the number? (1-6) "))
        
        # Check if guess matches the dice roll
        if guess == first_dice_roll:
            # Player wins!
            winnings = bet * 2
            print(f"Congratulations, you won {winnings}")
        else:
            # Player loses
            print(f"Sorry, you lost {bet}")
        
elif play_choice == "no":
    print("Okay you don't want to play. Game Over.")
else:
    print("Invalid input. Game Over.")