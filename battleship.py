from random import randint

grid = []


for x in range(5):
    grid.append(["0"] * 5)

def createGrid(grid):
    for rows in grid:
        for column in rows:
            print(column, end=" ")
        print()
        


print("Let's play Battleship!")

def ran_row(grid):
    return randint(0, len(grid - 1))
    
def ran_col(grid):
    return randint(0, len(grid[0] - 1))
        
ship_row = ran_row
ship_col = ran_col


createGrid(grid)
for turn in range(5):
    

    while True:
        try:
            guessRow = eval(input("Which row do you want to strike: "))
            guessColumn = eval(input("Which column do you want to strike: "))
            
            
            if guessRow < 0 or guessRow > 4 or guessColumn < 0 or guessColumn > 4:
                raise ValueError
            
            break  
        
        except ValueError:
            print('Please enter a number between 0-4')
            
        
    if grid[guessRow][guessColumn] == "x":
            print("You already guessed right there, try again")
            
    elif guessRow in (0, 1, 2, 3, 4) and guessColumn in (0, 1, 2, 3, 4):
        grid[guessRow][guessColumn] = "x"
        print("you struck at ", guessRow, ",", guessColumn)
        
    elif (guessRow == ship_row) and (guessColumn == ship_col):
        print("Yay! You sunk my battleship!")
        
    else:
        if guessRow != (0, 1, 2, 3, 4):
            print("Please enter a number between 0-4")
            guessRow = int(input("Which row do you want to strike: "))
            
        if guessColumn != (0, 1, 2, 3, 4):
            print("PLease enter a number between 0-4")
            guessColumn = int(input("Which column do you want to strike: "))

    createGrid(grid)              
    
    
    
            
            

        
    
                
            


    

