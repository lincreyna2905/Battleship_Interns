grid =[]

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

Placement = input("How do you want the battleship to be placed?" "\n" "1. I want to place it" "\n" "2. Random" "\n")

if Placement == 1:
    print()
    
if (Placement == 2): 
    print()

print("Let's play Battleship!")
    
createGrid(grid)
while True:
    
    
    while True:
        try:
            guessRow = int(input("Which row do you want to strike: "))
            guessColumn = int(input("Which column do you want to strike: "))
            
            
            if guessRow < 0 or guessRow > len(grid) - 1 or guessColumn < 0 or guessColumn > len(grid) - 1:
                raise ValueError
            
            break  
        
        except ValueError:
            print('Enter a number between 0 -', len(grid) - 1)
            
            
    while True:
        
        if grid[guessRow][guessColumn] == "X":
                print("You already guessed right there, try again")
                
        elif guessRow in range(0, len(grid)) and guessColumn in range(0, len(grid)):
            grid[guessRow][guessColumn] = "X"
            print("you struck at ", guessRow, ",", guessColumn)
            
        else:
            if guessRow != (range(0, len(grid))):
                print("Please enter a number between 0 -", len(grid) - 1)
                guessRow = int(input("Which row do you want to strike: "))
                
            if guessColumn != (range(0, len(grid))):
                print("PLease enter a number between 0 -", len(grid) - 1)
                guessColumn = int(input("Which column do you want to strike: "))
                
        break
        
    createGrid(grid) 