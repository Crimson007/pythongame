# Dice Game Double Play  First game + offer second round

# Provided die rolls 
first_dice_roll = 1
second_dice_roll = 1

print("Welcome to the Dice Game, you can choose to play twice!")
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
        
        # Track total winnings/losses
        total = 0
        
        # Check if guess matches the dice roll
        if guess == first_dice_roll:
            # Player wins first game!
            winnings = bet * 2
            total += winnings
            print(f"Congratulations, you won {winnings}")
        else:
            # Player loses first game
            total -= bet
            print(f"You lost {bet}")
        
        # Offer to play again with double the bet
        print()
        double_bet = bet * 2
        play_again = input(f"We can play again if you bet {double_bet}? (yes/no) ")
        
        if play_again == "yes":
            # Stage 2 will add the second game logic here
            print("Second round coming in Stage 2...")
        else:
            # Player declines second round
            if total > 0:
                print(f"Thank you, you won {total}")
            else:
                print(f"Thank you, you lost {abs(total)}")
        
elif play_choice == "no":
    print("Okay you don't want to play. Game Over.")
else:
    print("Invalid input. Game Over.")