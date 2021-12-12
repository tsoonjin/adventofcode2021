from statistics import median
from sympy import *

def find_horizontal_least_fuel(input):
    horizontal_pos = [int(i) for i in input[0].split(",")]
    optimal_pos = median(horizontal_pos)
    fuel = sum([abs(i - optimal_pos) for i in horizontal_pos])
    return fuel

def find_horizontal_least_fuel_derivative(input):
    x = symbols('x', real=True)
    horizontal_pos = [int(i) for i in input[0].split(",")]
    y = Abs(horizontal_pos[0] - x) * (Abs(horizontal_pos[0] - x) + 1) / 2
    for i in horizontal_pos[1:]:
        y += Abs(i - x) * (Abs(i - x) + 1) / 2
    optimal = solve(y.diff(x), x)
    print(optimal)
    # optimal_pos = median(horizontal_pos)
    # fuel = sum([abs(i - optimal_pos) for i in horizontal_pos])
    return 1

if __name__ == "__main__":
    with open('part1.txt') as f:
        input = f.read().splitlines()
        ans = find_horizontal_least_fuel(input)
        print(f'Part 1: {ans}')

    with open('part2.txt') as f:
        input = f.read().splitlines()
        ans = find_horizontal_least_fuel_derivative(input)
        print(f'Part 2: {ans}')
