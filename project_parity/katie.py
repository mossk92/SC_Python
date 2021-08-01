grid = [
    ["x","b","c"],
    ["x","x","o"],
    ["o","o","x"],
    ["x","o","x"],
]

choose_column = input(f"Please select a number from 1 to {len(grid[0])}?   ")
choose_row = input(f"Please select a number from 1 to {len(grid)}?   ")

print(choose_column)
print(choose_row)

