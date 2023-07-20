from colorama import Fore
from random import randint
grid = []
enemyGrid = []

while True:
    try:
        boardSize =int(input("Enter the size of the board that you want to play on: "))
        
        if boardSize < 3 or boardSize > 10:
            raise ValueError
            
        
        break
    
    except ValueError:
        print("Please choose a board size between 3 - 10")
    
        
for x in range(boardSize):
    grid.append(["O"] * boardSize)

def createGrid(grid):
    for rows in grid:
        for column in rows:
            print(column, end=" ")
        print()
        

while True:
    try:
        Placement = int(input("How do you want the battleship to be placed?" "\n" "1. I want to place it" "\n" "2. Random" "\n"))
        
        if Placement < 1 or Placement > 2:
            raise ValueError
        
        break 
    except ValueError:
        print("Enter either choice 1 or 2")
            

if Placement == 1:
    while True:
        try:
            user_ship_row = int(input("PLease enter a row indexed at 1: ")) - 1
            user_ship_col = int(input("PLease enter a col indexed at 1: ")) - 1
            
            if user_ship_row < 0 or user_ship_row > len(grid) - 1:
                raise ValueError
            
            elif user_ship_col < 0 or user_ship_col > len(grid) - 1:
                raise ValueError
            
        except ValueError:
            print("Please enter a valid coordinate on the grid!")
            continue
        grid[user_ship_row][user_ship_col] =(Fore.LIGHTBLACK_EX + "B" + Fore.WHITE)
        print()
        break
        

def ran_row(grid):
        return randint(0, len(grid) - 1)
    
def ran_col(grid):
        return randint(0, len(grid[0]) - 1)

    
if (Placement == 2):      
    user_ship_row = ran_row(grid)
    user_ship_col = ran_col(grid)
    grid[user_ship_row][user_ship_col] =(Fore.LIGHTBLACK_EX + "B" + Fore.WHITE)
    print()

print("Let's play Battleship!")
createGrid(grid)

turn = 1
computerTurn = 1

computerShipRow = randint(0, len(grid) + 1)
computerShipColumn = randint(0, len(grid) + 1)

while turn in range(6):
    print("Turn",turn)

    computerRowGuess= randint(0, len(grid) - 1)
    computerColumnGuess = randint(0, len(grid) - 1)
    
    while True:
        try:
            guessRow = int(input("Which row do you want to strike: ")) - 1
            guessColumn = int(input("Which column do you want to strike: ")) - 1
            
            if guessRow < 0 or guessRow > len(grid) - 1:
               raise ValueError
                
            elif guessColumn < 0 or guessColumn > len(grid) - 1:
                raise ValueError
            break 
        except ValueError:
            print('Please enter a number between 0 -', len(grid) - 1)
            
            
            
    if guessRow not in range(len(grid)):
        print("Row not in range of board")
        print('Please enter a number between 0 -', len(enemyGrid) - 1)
    
    elif guessColumn not in range(len(grid)):
        print("Col not in range of board")
        print('Please enter a number between 0 -', len(enemyGrid) - 1)

    
    else:
        if (guessRow == computerShipRow) and (guessColumn == computerShipColumn):
            print("Yay! You sunk the enemy's battleship!")
            break


        elif guessRow in range(0, len(grid)) and guessColumn in range (0, len(grid)):
            print(f"You guessed ({str(guessRow)}, {guessColumn})", "and missed the opponents ship!")
            turn = turn + 1


    while computerTurn in range(6):
        print()
        print("Enemy turn ", computerTurn)

        if computerRowGuess in range(0, len(grid)) and computerColumnGuess in range(0, len(grid)):
            grid[computerRowGuess][computerColumnGuess] = (Fore.RED + "X" + Fore.WHITE)
            print (f"Computer guessed ({str(computerRowGuess + 1)},{computerColumnGuess + 1})")
            computerTurn += 1
       

        if computerRowGuess == user_ship_row and computerColumnGuess == user_ship_col:
            createGrid(grid)
            print()
            print("You lost! The enemy sunk your battleship")
            print(f"The opponent's battleship was located at: ({computerShipRow + 1}, {computerShipColumn + 1}).")
            exit()
        break


    if (turn == 6) or (computerTurn == 6):
        createGrid(grid)
        print()
        print("GAME OVER")
        print("No one could sink a ship!")
        print(f"The opponent's battleship was located at: ({computerShipRow + 1}, {computerShipColumn + 1}).")
        exit()
    
    createGrid(grid)
