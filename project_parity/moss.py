grid = [
    ['A','O','X','O'],
    ['X','O','X','O'],
    ['X','O','O','O'],
]
print(grid[0])

grid[0][0] = 'X'

print(grid[0])

def flip_cell(x_pos, y_pos, grid):
    if grid[y_pos][y_pos] == "X":
        grid[x_pos][y_pos] = "O"
    else:
        grid[x_pos][y_pos] = "X"

    return(grid)

# print(flip_cell(0,0,grid))