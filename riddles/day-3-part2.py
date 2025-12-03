import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from utils.utils import read_input

def get_max_joltage_12(bank):
    result = []
    remaining = 12
    start = 0

    while remaining > 0:
        end = len(bank) - remaining + 1
        max_digit = max(bank[start:end])
        idx = bank.index(max_digit, start, end)
        result.append(max_digit)
        start = idx + 1
        remaining -= 1

    return int(''.join(result))

def solve(data):
    banks = data.strip().split('\n')
    total = sum(get_max_joltage_12(bank) for bank in banks)
    return total

if __name__ == "__main__":
    data = read_input("day-3.txt")
    result = solve(data)
    print(f"Part 2: {result}")
