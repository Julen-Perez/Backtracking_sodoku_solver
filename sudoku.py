#Checks if a guessed number can be introduced in the grid, or if there is already such a number in the column, row or 3x3 square.
def validMove(grid, row, col, guess):
   
#Checks rows and columns
    for i in range(9):
        if grid[i][col] == guess or  grid[row][i] == guess:
            return False
 
   
    startR = row - row % 3
    startC = col - col % 3
    #Checks the 3x3 square
    for i in range(3):
        for j in range(3):
            if grid[i + startR][j + startC] == guess:
                return False
    return True
 

def solver(grid, row, col):

#If we have filled the column, advances the rows and resets the columns to 0.
    if col == 9:
        row += 1
        col = 0

#Checks if we have found the solution. 
    if (row == 9):
        return True
       
   #If the space is not empty, we go forward
    if grid[row][col] > 0:
        return solver(grid, row, col + 1)

    #If it is not empty we use backtracking to find the solution
    else:
        for guess in range(1, 10):
           
            #Checks if the guessed number can be put in the sudoku grid
            if validMove(grid, row, col, guess):
               
                
                grid[row][col] = guess
     
                #Using backtracking checks if it leads to an answer. 
                if solver(grid, row, col + 1):
                    return True
     
            #If it does not lead to an answer it will come back and have another guess.
            grid[row][col] = 0
        return False
 

grid = [[0, 4, 7, 0, 2, 5, 0, 0, 0],
        [3, 5, 8, 6, 1, 7, 0, 0, 0],
        [6, 0, 2, 8, 4, 3, 0, 0, 7],
        [0, 0, 0, 7, 0, 1, 3, 0, 6],
        [2, 6, 5, 4, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 9, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 4],
        [0, 1, 0, 5, 0, 0, 2, 6, 9],
        [0, 0, 0, 3, 0, 6, 0, 0, 8]]
 


if (solver(grid, 0, 0)):
    for i in range(9):
        for j in range(9):
            print(str(grid[i][j]) ,end=" ")
        print()
else:
    print("No posible solution ")
 
