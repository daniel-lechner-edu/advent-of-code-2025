def is_invalid_id_part1(num):
    s = str(num)
    if len(s) % 2 != 0:
        return False
    mid = len(s) // 2
    return s[:mid] == s[mid:]

def is_invalid_id_part2(num):
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

def solve(input_file, part=1):
    with open(input_file) as f:
        data = f.read().strip()

    ranges = data.split(',')
    total = 0
    check_fn = is_invalid_id_part1 if part == 1 else is_invalid_id_part2

    for r in ranges:
        start, end = map(int, r.split('-'))
        for num in range(start, end + 1):
            if check_fn(num):
                total += num

    return total

if __name__ == "__main__":
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(script_dir, "input.txt")

    result_part1 = solve(input_path, part=1)
    print(f"Part 1 - Sum of invalid IDs: {result_part1}")

    result_part2 = solve(input_path, part=2)
    print(f"Part 2 - Sum of invalid IDs: {result_part2}")
