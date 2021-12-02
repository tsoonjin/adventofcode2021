# Calculate number of increase from previous line
def count_increase(input):
    num_increase = 0
    # Index starts at 1
    for index, value in enumerate(input):
        previous_depth = int(input[index - 1].rstrip())
        current_depth = int(value.rstrip())
        if (current_depth - previous_depth > 0):
            num_increase += 1
    return num_increase


# Calculate number of increase taking 3 measurements sliding window
def count_increase_sliding_window(input, window_size):
    num_increase = 0
    for index, value in enumerate(input[1:]):
        if index + window_size == len(input):
            break
        previous_sum_depth = sum([int(depth.rstrip())
                                 for depth in input[index - 1: index + window_size - 1]])
        current_sum_depth = sum([int(depth.rstrip())
                                for depth in input[index: index + window_size]])
        if (current_sum_depth - previous_sum_depth > 0):
            num_increase += 1
    return num_increase


if __name__ == "__main__":
    with open('part1.txt') as f:
        input = f.readlines()
        ans = count_increase(input)
        print(f'Part 1: {ans}')

    with open('part2.txt') as f:
        input = f.readlines()
        ans = count_increase_sliding_window(input, 3)
        print(f'Part 2: {ans}')
