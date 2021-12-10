def find_lanternfish(input, day=80):
    population = [int(i) for i in input[0].split(",")]
    for i in range(day):
        current_population = [(i - 1) if i > 0 else 6 for i in population]
        new_fish = [9 for i in current_population if i == 0]
        population = [*current_population, *new_fish]
        print(f"After {i + 1} Day")
    return len([i for i in population if i != 9])

if __name__ == "__main__":
    with open('part1.txt') as f:
        input = f.read().splitlines()
        ans = find_lanternfish(input)
        print(f'Part 1: {ans}')

    with open('part1.txt') as f:
        input = f.read().splitlines()
        ans = find_lanternfish(input, 256)
        print(f'Part 1: {ans}')
