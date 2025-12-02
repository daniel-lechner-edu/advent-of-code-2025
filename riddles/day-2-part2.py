from utils import read_input

def is_invalid_id(num):
    s = str(num)
    n = len(s)
    for pattern_len in range(1, n):
        if n % pattern_len == 0:
            repeats = n // pattern_len
            if repeats >= 2:
                pattern = s[:pattern_len]
                if pattern * repeats == s:
                    return True
    return False

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
    print(f"Part 2: {result}")
