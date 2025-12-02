from utils import read_input_lines

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
    instructions = read_input_lines("day-1.txt")
    result = solve_safe_dial(instructions)
    print(f'Part 2: {result}')
