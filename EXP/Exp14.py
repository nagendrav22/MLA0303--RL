grid = [
    [0, 0, 0],
    [0, 1, 0],   
    [0, 0, 2]    
]

row = 0
col = 0

print("Grid World")
for r in grid:
    print(r)

print("\nRobot Path:")

while grid[row][col] != 2:

    if col < 2 and grid[row][col + 1] != 1:
        col += 1
    elif row < 2 and grid[row + 1][col] != 1:
        row += 1

    print("(", row, ",", col, ")")

print("\nGoal Reached!")
