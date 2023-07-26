from random import randint
from colorama import Fore

grid_size = 10
grid = [['O'] * grid_size for _ in range(grid_size)]
enemy_grid = [['O'] * grid_size for _ in range(grid_size)]

def create_grid(grid , show_ships=False):
    for row in grid:
        for column in row:
            if not show_ships and column in ['S', 'D']:
                print('O', end=' ')
            else:
                print(column, end=' ')
        print()
print("Welcome to the game, Battleship!")

def get_valid_ship_coordinate(prompt):
    while True:
        try:
            coordinate = int(input(prompt)) - 1
            if 0 <= coordinate < grid_size:
                return coordinate
            raise ValueError
        except ValueError:
            print("Please enter a valid coordinate on the grid!")

def place_ship(grid, ship_length, ship_marker, ship_name):
    print(f"Place your '{ship_name}' ({ship_length} indices long)")
    while True:
        while True:
            user_ship_row = get_valid_ship_coordinate("Please enter a row (1-10): ")
            user_ship_col = get_valid_ship_coordinate("Please enter a col (1-10): ")

            if grid[user_ship_row][user_ship_col] != 'O':
                print("You can't place a ship there. Try again.")
                continue
            break

        orientation = input("Choose orientation (H for horizontal, V for vertical): ").upper()
        if orientation not in ['H', 'V']:
            print("Invalid orientation. Try again.")
            continue

        valid_placement = True
        if orientation == 'H' and user_ship_col + ship_length <= grid_size:
            for i in range(ship_length):
                if grid[user_ship_row][user_ship_col + i] != 'O':
                    valid_placement = False
                    break
            if valid_placement:
                for i in range(ship_length):
                    grid[user_ship_row][user_ship_col + i] = ship_marker
                break

        elif orientation == 'V' and user_ship_row + ship_length <= grid_size:
            for i in range(ship_length):
                if grid[user_ship_row + i][user_ship_col] != 'O':
                    valid_placement = False
                    break
            if valid_placement:
                for i in range(ship_length):
                    grid[user_ship_row + i][user_ship_col] = ship_marker
                break

        print("Invalid placement. Try again.")

def random_ship_placement(grid, num_ships, ship_length, ship_marker, ship_name):
    ship_length  = 2
    while True:
        ship_row = randint(0, grid_size - 1)
        ship_col = randint(0, grid_size - 1)

        orientation = randint(0, 1)  # 0 for horizontal, 1 for vertical
        valid_placement = True
        if orientation == 0 and ship_col + ship_length <= grid_size:
            for i in range(ship_length):
                if enemy_grid[ship_row][ship_col + i] != 'O':
                    valid_placement = False
                    break
            if valid_placement:
                for i in range(ship_length):
                    enemy_grid[ship_row][ship_col + i] = ship_marker
                break

        elif orientation == 1 and ship_row + ship_length <= grid_size:
            for i in range(ship_length):
                if enemy_grid[ship_row + i][ship_col] != 'O':
                    valid_placement = False
                    break
            if valid_placement:
                for i in range(ship_length):
                    enemy_grid[ship_row + i][ship_col] = ship_marker
                break

if __name__ == "__main__":
    num_ships_per_player = 2
    ship_length = 2

    user_ship_marker = Fore.GREEN + "S" + Fore.WHITE
    user_ship_name1 = input("Enter the name for your first ship: ")   
    place_ship(grid, ship_length, user_ship_marker, user_ship_name1)

    user_ship_marker = Fore.GREEN + "D" + Fore.WHITE
    user_ship_name2 = input("Enter the name for your second ship: ")
    place_ship(grid, ship_length, user_ship_marker, user_ship_name2)

    computer_ship_marker = "C"
    computer_ship_name1 = "Enemy Ship 1"
    random_ship_placement(enemy_grid, num_ships_per_player, ship_length, computer_ship_marker, computer_ship_name1)

    computer_ship_marker = "D"
    computer_ship_name2 = "Enemy Ship 2"
    random_ship_placement(enemy_grid, num_ships_per_player, ship_length, computer_ship_marker, computer_ship_name2)

    print("Let's play Battleship!")
    print("Your grid:")
    create_grid(grid, show_ships=True)  # Show user's grid with their ships

    user_ships_remaining = num_ships_per_player * 2
    computer_ships_remaining = num_ships_per_player * 2
    computer_ships = [computer_ship_marker, computer_ship_marker]
    
    turn = 0
    for turn in range(8):
        print("Turn", turn + 1)
        while True:
            guess_row = get_valid_ship_coordinate("Which row do you want to strike? (1-10): ")
            guess_col = get_valid_ship_coordinate("Which column do you want to strike? (1-10): ")
            
            computer_guess_row = randint(0, 9)
            computer_guess_col = randint(0, 9)
            
            if enemy_grid[guess_row][guess_col] in ['X', 'M']:
                print("You've already guessed this spot. Try again.")
            else:
                break
        if enemy_grid[guess_row][guess_col] not in ("C","D"):
            print(f"You struck at {guess_row + 1} , {guess_col + 1} and missed!")
            enemy_grid[guess_row][guess_col] = "X"
        else:
            print(f"You hit the enemy's {computer_ship_name1}!")
            enemy_grid[guess_row][guess_col] = "X"
            computer_ships_remaining = computer_ships_remaining - 1

        if grid[computer_guess_row][computer_guess_col] in ('S', 'D'):
            print('\n')
            grid[computer_guess_row][computer_guess_col] = Fore.BLACK + 'H' + Fore.WHITE
            print("Computer hit your ship!")
            user_ships_remaining -= 1
            
            if user_ships_remaining == 0:
                print("All your ships have sunk! You lose!")
                break
                    
        elif grid[computer_guess_row][computer_guess_col] not in ("S", "D"):
                print()
                grid[computer_guess_row][computer_guess_col] = Fore.RED + 'M' + Fore.WHITE
                print("Computer missed!")
                
            
                

        print("Your grid:")
        create_grid(grid, show_ships=True)
        print('\n')
        

        if turn == 7 or (user_ships_remaining == 0 or computer_ships_remaining == 0):
            print("\nGAME OVER")
            if user_ships_remaining != 0 and computer_ships_remaining != 0:
                print("It's a tie! Both players couldn't sink any ships.")
            elif user_ships_remaining == 0:
                print("You lost! The enemy sunk your ships.")
            else:
                print("Congratulations! You sunk all enemy ships!")
            break      
