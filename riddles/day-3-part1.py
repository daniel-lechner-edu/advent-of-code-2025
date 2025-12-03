import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from utils.utils import read_input

def get_max_joltage(bank):
    max_val = 0
    for i in range(len(bank)):
        for j in range(i + 1, len(bank)):
            joltage = int(bank[i] + bank[j])
            max_val = max(max_val, joltage)
    return max_val

def solve(data):
    banks = data.strip().split('\n')
    total = sum(get_max_joltage(bank) for bank in banks)
    return total

if __name__ == "__main__":
    data = read_input("day-3.txt")
    result = solve(data)
    print(f"Part 1: {result}")
