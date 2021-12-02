import math

# Calculate final position given series of commands
# Final horizontal * final depth
def calculate_final_position(input):
    pos = [0, 0]
    position_mult = {
        "forward": (1, 0),
        "up": (0, -1),
        "down": (0, 1)
    }
    for command in input:
        print(command.strip())
        [direction, magnitude] = command.strip().split(" ")
        pos[0] += position_mult[direction][0] * int(magnitude)
        pos[1] += position_mult[direction][1] * int(magnitude)

    return math.prod(pos)

# Calculate final position given series of commands
# Final horizontal * final depth
def calculate_final_position_with_aim(input):
    # horizontal, aim, depth
    pos = [0, 0, 0]
    position_mult = {
        "forward": (1, 0, 1),
        "up": (0, -1, 0),
        "down": (0, 1, 0)
    }
    for command in input:
        [direction, magnitude] = command.strip().split(" ")
        pos[0] += position_mult[direction][0] * int(magnitude)
        pos[1] += position_mult[direction][1] * int(magnitude)
        pos[2] += position_mult[direction][2] * int(magnitude) * pos[1]

    return pos[0] * pos[2]


if __name__ == "__main__":
    with open('part1.txt') as f:
        input = f.readlines()
        ans = calculate_final_position(input)
        print(f'Part 1: {ans}')

    with open('part2.txt') as f:
        input = f.readlines()
        ans = calculate_final_position_with_aim(input)
        print(f'Part 2: {ans}')
