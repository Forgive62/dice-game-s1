import random

def roll_dice():
    return random.randint(1, 6), random.randint(1, 6)

def play_game(starting_player=1):
    print("Welcome to the Two-Player Dice Game!")
    
    current_player = starting_player
    while True:
        print(f"Player {current_player}'s turn!")
        input("Press Enter to roll the dice...")
        
        die1, die2 = roll_dice()
        total = die1 + die2
        
        print(f"Player {current_player} rolled: {die1} and {die2} (Total: {total})")
        
        if total in [7, 11]:
            print(f"Pop! Player {current_player} wins immediately!")
            next_player = current_player
        elif total in [2, 3, 12]:
            print(f"Craps! Player {current_player} loses immediately!")
            next_player = 3 - current_player
        else:
            male = total
            print(f"The Male is {male}. Player {current_player} must roll it again to win!")
            
            while True:
                input("Press Enter to roll again...")
                die1, die2 = roll_dice()
                total = die1 + die2
                
                print(f"Player {current_player} rolled: {die1} and {die2} (Total: {total})")
                
                if total == male:
                    print(f"Player {current_player} wins!")
                    next_player = current_player
                    break
                elif total == 7:
                    print(f"Player {current_player} loses! Player {3 - current_player} wins!")
                    next_player = 3 - current_player
                    break
        
        print("Starting a new game with the previous winner!")
        current_player = next_player

if __name__ == "__main__":
    play_game()
