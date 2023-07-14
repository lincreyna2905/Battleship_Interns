grid =[]

for x in range(5):
    grid.append(["0"] * 5)

def createGrid(grid):
    for rows in grid:
        for column in rows:
            print(column, end=" ")
        print()


print("Let's play Battleship!")
    
createGrid(grid)


while True:
    guessRow = int(input("Which row do you want to strike: "))
    guessColumn = int(input("Which column do you want to strike: "))
    
    if grid[guessRow][guessColumn] == "x":
            print("You already guessed right there, try again")
            
    elif guessRow in (0, 1, 2, 3, 4) and guessColumn in (0, 1, 2, 3, 4):
        grid[guessRow][guessColumn] = "x"
        print("you struck at ", guessRow, ",", guessColumn)
        
    else:
        if guessRow != (0, 1, 2, 3, 4):
            print("Please enter a number between 0-4")
            guessRow = int(input("Which row do you want to strike: "))
            
        if guessColumn != (0, 1, 2, 3, 4):
            print("PLease enter a number between 0-4")
            guessColumn = int(input("Which column do you want to strike: "))
    
    createGrid(grid)        
    
    
                
            


    

