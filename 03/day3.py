from collections import Counter
from functools import reduce

# Gamma rate = most frequent
# Epsilon rate = least frequent
# Power = Gamma rate * Epsilon rate
def calc_power_consumption(input):
    measure_len = len(input[0])
    gamma_r = int(''.join([Counter([measure[i] for measure in input]).most_common(1)[0][0] for i in range(measure_len)]), 2)
    epsilon_r = int(''.join([str(1 - int(Counter([measure[i] for measure in input]).most_common(1)[0][0])) for i in range(measure_len)]), 2)
    return gamma_r * epsilon_r


def calc_life_support(input):
    measure_len = len(input[0])
    oxygen_r = int(reduce(get_oxygen_r, list(range(measure_len)), input)[0], 2)
    print(oxygen_r)
    co2_r = int(reduce(get_co2_r, list(range(measure_len)), input)[0], 2)
    print(co2_r)
    return oxygen_r * co2_r

def get_most_frequent(counter, defaultVal="1"):
    most_frequent_key = counter.most_common(1)[0][0] if counter.most_common(2)[0][1] > counter.most_common(2)[1][1] else defaultVal
    return most_frequent_key

def get_least_frequent(counter, defaultVal="0"):
    least_frequent_key = counter.most_common(2)[1][0] if counter.most_common(2)[1][1] < counter.most_common(2)[0][1] else defaultVal
    return least_frequent_key

def get_oxygen_r(remained, current):
    if len(remained) == 1:
        return remained
    target = get_most_frequent(Counter([measure[current] for measure in remained]))
    leftover = [x for x in remained if x[current] == target]
    return leftover

def get_co2_r(remained, current):
    if len(remained) == 1:
        return remained
    target = get_least_frequent(Counter([measure[current] for measure in remained]))
    leftover = [x for x in remained if x[current] == target]
    return leftover


if __name__ == "__main__":
    with open('part1.txt') as f:
        input = f.read().splitlines()
        ans = calc_power_consumption(input)
        print(f'Part 1: {ans}')

    with open('part2.txt') as f:
        input = f.read().splitlines()
        ans = calc_life_support(input)
        print(f'Part 2: {ans}')
