def solve_safe_dial(instructions, count_passes=False):
    position = 50
    zero_count = 0

    for instruction in instructions:
        direction = instruction[0]
        distance = int(instruction[1:])

        if count_passes:
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
        else:
            if direction == 'L':
                position = (position - distance) % 100
            else:
                position = (position + distance) % 100

            if position == 0:
                zero_count += 1

    return zero_count

example = [
    'L68', 'L30', 'R48', 'L5', 'R60',
    'L55', 'L1', 'L99', 'R14', 'L82'
]

print(f'Example Part 1: {solve_safe_dial(example)}')
print(f'Example Part 2: {solve_safe_dial(example, count_passes=True)}')

with open('input.txt', 'r') as f:
    instructions = [line.strip() for line in f.readlines()]
    password1 = solve_safe_dial(instructions)
    password2 = solve_safe_dial(instructions, count_passes=True)
    print(f'Password Part 1: {password1}')
    print(f'Password Part 2: {password2}')