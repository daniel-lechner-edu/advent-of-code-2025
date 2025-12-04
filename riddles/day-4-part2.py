import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from utils.utils import read_input_lines

def count_adjacent_rolls(grid, row, col):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0
    for dr, dc in directions:
        nr, nc = row + dr, col + dc
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == '@':
            count += 1
    return count

def solve(data):
    grid = [list(line) for line in data]
    total_removed = 0

    while True:
        to_remove = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '@':
                    adjacent_count = count_adjacent_rolls(grid, row, col)
                    if adjacent_count < 4:
                        to_remove.append((row, col))

        if not to_remove:
            break

        for row, col in to_remove:
            grid[row][col] = '.'
        total_removed += len(to_remove)

    return total_removed

if __name__ == "__main__":
    data = read_input_lines("day-4.txt")
    result = solve(data)
    print(f"Part 2: {result}")
