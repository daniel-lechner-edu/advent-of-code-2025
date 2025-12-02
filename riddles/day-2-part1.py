from utils import read_input

def is_invalid_id(num):
    s = str(num)
    if len(s) % 2 != 0:
        return False
    mid = len(s) // 2
    return s[:mid] == s[mid:]

def solve(data):
    ranges = data.split(',')
    total = 0

    for r in ranges:
        start, end = map(int, r.split('-'))
        for num in range(start, end + 1):
            if is_invalid_id(num):
                total += num

    return total

if __name__ == "__main__":
    data = read_input("day-2.txt")
    result = solve(data)
    print(f"Part 1: {result}")
