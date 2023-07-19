from random import randint
grid =[]
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
            ship_row = int(input("PLease enter a row indexed at 0: "))
            ship_col = int(input("PLease enter a col indexed at 0: "))
            
            if ship_row < 0 or ship_row > len(grid) - 1:
                raise ValueError
            
            elif ship_col < 0 or ship_col > len(grid) - 1:
                raise ValueError
            
        except ValueError:
            print("Please enter a valid coordinate on the grid!")
            continue
        print()
        break
        

def ran_row(grid):
        return randint(0, len(grid) - 1)
    
def ran_col(grid):
        return randint(0, len(grid[0]) - 1)
    
if (Placement == 2):      
    ship_row = ran_row(grid)
    ship_col = ran_col(grid)
    print()

print("Let's play Battleship!")
createGrid(grid)

turn = 1
computerTurn = 1

while turn in range(6):
    print("Turn",turn)
    while True:
        try:
            guessRow = int(input("Which row do you want to strike: "))
            guessColumn = int(input("Which column do you want to strike: "))
            
            if guessRow < 0 or guessRow > len(grid) - 1:
               raise ValueError
                
            elif guessColumn < 0 or guessColumn > len(grid) - 1:
                raise ValueError
                
            break 
        except ValueError:
            print('Please enter a number between 0 -', len(grid) - 1)
            
            
            
    if guessRow not in range(len(grid)):
        print("Row not in range of board")
        print('Please enter a number between 0 -', len(grid) - 1)
    
    elif guessColumn not in range(len(grid)):
        print("Col not in range of board")
        print('Please enter a number between 0 -', len(grid) - 1)

    
    else:  
        if (guessRow == ship_row) and (guessColumn == ship_col):
            print("Congratulations! You sunk my battleship!")
            break

        elif grid[guessRow][guessColumn] == "X":
            print("You already guessed right there, try again")

        elif guessRow in range(0, len(grid)) and guessColumn in range(0, len(grid)):
            grid[guessRow][guessColumn] = "X"
            print("You missed! You struck at ", guessRow, ",", guessColumn)
            turn = turn + 1

        if (turn == 6):
            print()
            print("Game over, you lost")
            
        
    while computerTurn in range(6):
        print()
        print("Computer turn ", computerTurn)
        
        computerRowGuess= randint(0, len(grid) - 1)
        computerColumnGuess = randint(0, len(grid) - 1)
        
        print("Computer guessed at ", computerRowGuess, ",", computerColumnGuess)
        computerTurn += 1
        
        if computerRowGuess == ship_row and computerColumnGuess == ship_col:
            print("Game over, computer wins.")
        break
            
        
    

    createGrid(grid)          
    
    
    
            
            

        
    
                
            


    

