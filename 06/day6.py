def find_lanternfish(input):
    pass

if __name__ == "__main__":
    with open('part1.txt') as f:
        input = f.read().splitlines()
        ans = find_lanternfish(input)
        print(f'Part 1: {ans}')
