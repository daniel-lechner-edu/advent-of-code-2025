import os

def solve_safe_dial(instructions):
    position = 50
    zero_count = 0

    for instruction in instructions:
        direction = instruction[0]
        distance = int(instruction[1:])

        if direction == 'R':
            for i in range(1, distance + 1):
                if (position + i) % 100 == 0:
                    zero_count += 1
            position = (position + distance) % 100
        else:
            for i in range(1, distance + 1):
                if (position - i) % 100 == 0:
                    zero_count += 1
            position = (position - distance) % 100

    return zero_count

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(script_dir, "..", "inputs", "day-1.txt")

    with open(input_path, 'r') as f:
        instructions = [line.strip() for line in f.readlines()]
        result = solve_safe_dial(instructions)
        print(f'Part 2: {result}')
