grid =[]
row = ""

for x in range(5):
    grid.append(["0"] * 5)

def createGrid(grid):
    for rows in grid:
        for column in rows:
            print(column, end=" ")
        print()


print("Let's play Battleship!")
    
createGrid(grid)

row = int(input("Enter the row that you want to strike: "))

def checkRow(row):
        if row > 4 | row < 0:
            print("Enter a number between 0-4")
            
        
    
    

while True:
    
    row = int(input("Enter the row that you want to strike: ")
    checkRow(row)
   
    column = int(input("Enter the column that you want to strike: "))

   
        
    if grid[row][column] == "x":
        print("You already guessed right there")
        
        



    grid[row][column] = "x"
    createGrid(grid)

