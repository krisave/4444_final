def print_grid(grid):
    for row in grid:
        print(" ".join(str(val) if val != 0 else '.' for val in row))


def is_valid(grid, row, col, num):
    for i in range(9):
        if grid[row][i] == num or grid[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if grid[i][j] == num:
                return False
    return True


def find_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return None


def solve(grid):
    empty = find_empty(grid)
    if not empty:
        return True  
    row, col = empty

    for num in range(1, 10):
        if is_valid(grid, row, col, num):
            grid[row][col] = num
            if solve(grid):
                return True
            grid[row][col] = 0 
    return False

def get_user_input():
    print("Enter your Sudoku puzzle row by row (9 digits per row, use 0 for empty):")
    grid = []
    for i in range(9):
        while True:
            row = input(f"Row {i + 1}: ").strip()
            if len(row) == 9 and all(c.isdigit() for c in row):
                grid.append([int(c) for c in row])
                break
            else:
                print("Invalid input. Please enter exactly 9 digits (0–9).")
    return grid

if __name__ == "__main__":
   puzzle = get_user_input()

print("Initial Sudoku Puzzle:")
print_grid(puzzle)

if solve(puzzle):
        print("\nSolved Puzzle:")
        print_grid(puzzle)
else:
        print("\nNo solution exists.")