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
        
        # Track results of each game
        first_game_won = False
        
        # Check if guess matches the dice roll
        if guess == first_dice_roll:
            # Player wins first game!
            winnings = bet * 2
            print(f"Congratulations, you won {winnings}")
            first_game_won = True
        else:
            # Player loses first game
            print(f"You lost {bet}")
            first_game_won = False
        
        # Offer to play again with double the bet
        print()
        double_bet = bet * 2
        play_again = input(f"We can play again if you bet {double_bet}? (yes/no) ")
        
        if play_again == "yes":
            # Second round begins
            second_guess = int(input("You know the game, guess the die number? (1-6) "))
            
            # Check second round result
            if second_guess == second_dice_roll:
                # Won second game
                second_game_won = True
            else:
                # Lost second game
                second_game_won = False
            
            # Calculate total and display outcome based on both games
            if first_game_won and second_game_won:
                # Win-Win: bet*2 + double_bet*2
                total_winnings = (bet * 2) + (double_bet * 2)
                print(f"Lucky you, two wins! Total winnings {total_winnings}")
            elif not first_game_won and second_game_won:
                # Lose-Win: -bet + double_bet*2
                total_winnings = -bet + (double_bet * 2)
                print(f"Lost first bet, but won second bet! Total winnings {total_winnings}")
            elif not first_game_won and not second_game_won:
                # Lose-Lose: -bet - double_bet
                total_loss = bet + double_bet
                print(f"You lost both bets. Total loss {total_loss}")
            elif first_game_won and not second_game_won:
                # Win-Lose: bet*2 - double_bet
                print("Won first bet, but lost second bet. You are even.")
        else:
            # Player declines second round
            if first_game_won:
                winnings = bet * 2
                print(f"Thank you, you won {winnings}")
            else:
                print(f"Thank you, you lost {bet}")
        
elif play_choice == "no":
    print("Okay you don't want to play. Game Over.")
else:
    print("Invalid input. Game Over.")