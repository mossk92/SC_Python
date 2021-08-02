grid = [
    ["a","b","c"],
    ["d","e","f"],
    ["g","h","i"],
    ["j","k","l"],
]

choose_y_pos = input(f"Please select a number from 1 to {len(grid[0])}?   ")
choose_x_pos = input(f"Please select a number from 1 to {len(grid)}?   ")

expected_coordinates = [int(choose_x_pos)-1,int(choose_y_pos)-1]

if (grid[int(choose_x_pos)-1][int(choose_y_pos)-1]) == "X":
    (grid[int(choose_x_pos)-1][int(choose_y_pos)-1]) = "O"
else:
    (grid[int(choose_x_pos)-1][int(choose_y_pos)-1]) = "X"

print(grid)