# Dice Game Double Play  First game + additional second round

first_dice_roll = 1
second_dice_roll = 1

print("Welcome to the Dice Game, you can choose to play twice!")
play_choice = input("Would you like to play? (yes/no) ")

if play_choice == "yes":
    bet = int(input("How much would you like to bet? (enter an integer less than or equal to 100) "))
    
    if bet > 100:
        print("Sorry, bet is too much. Game Over.")
    else:
        potential_win = bet * 2
        print(f"If you guess correctly you win {potential_win}")
        
        guess = int(input("A six sided die will be rolled. Guess the number? (1-6) "))
        
        # Track results of each game
        first_game_won = False
        
        if guess == first_dice_roll:
            # wins first game!
            winnings = bet * 2
            print(f"Congratulations, you won {winnings}")
            first_game_won = True
        else:
            # loses first game
            print(f"You lost {bet}")
            first_game_won = False
        
        # second chance to play
        print()
        double_bet = bet * 2
        play_again = input(f"We can play again if you bet {double_bet}? (yes/no) ")
        
        if play_again == "yes":
            second_guess = int(input("You know the game, guess the die number? (1-6) "))
            
            if second_guess == second_dice_roll:
                # Won second game
                second_game_won = True
            else:
                # Lost second game
                second_game_won = False
            
            # Calculate total and display outcome based on both games
            if first_game_won and second_game_won:

                total_winnings = (bet * 2) + (double_bet * 2)
                print(f"Lucky you, two wins! Total winnings {total_winnings}")
            elif not first_game_won and second_game_won:

                total_winnings = -bet + (double_bet * 2)
                print(f"Lost first bet, but won second bet! Total winnings {total_winnings}")
            elif not first_game_won and not second_game_won:

                total_loss = bet + double_bet
                print(f"You lost both bets. Total loss {total_loss}")
            elif first_game_won and not second_game_won:

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