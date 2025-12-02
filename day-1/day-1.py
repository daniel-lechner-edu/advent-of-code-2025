def solve_safe_dial(instructions):
    position = 50
    zero_count = 0

    for instruction in instructions:
        direction = instruction[0]
        distance = int(instruction[1:])

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

print(f'Example result: {solve_safe_dial(example)}')

with open('input.txt', 'r') as f:
    instructions = [line.strip() for line in f.readlines()]
    password = solve_safe_dial(instructions)
    print(f'Password: {password}')