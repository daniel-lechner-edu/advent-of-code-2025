import os

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

def solve(input_file):
    with open(input_file) as f:
        data = f.read().strip()

    ranges = data.split(',')
    total = 0

    for r in ranges:
        start, end = map(int, r.split('-'))
        for num in range(start, end + 1):
            if is_invalid_id(num):
                total += num

    return total

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(script_dir, "..", "inputs", "day-2.txt")
    result = solve(input_path)
    print(f"Part 2: {result}")
