def mark_line(p1, p2, underwater_map):
    x_diff = abs(int(p1[0]) - int(p2[0]))
    if x_diff > 0:
        x_start = p1[0] if int(p1[0]) < int(p2[0]) else p2[0]
        for x in range(x_diff + 1):
            next_val = str(int(x_start) + x) + ":" + p1[1]
            # print("X: ", next_val)
            if next_val not in underwater_map:
                underwater_map[next_val] = 0
            underwater_map[next_val] += 1
    y_diff = abs(int(p1[1]) - int(p2[1]))
    if y_diff > 0:
        y_start = p1[1] if int(p1[1]) < int(p2[1]) else p2[1]
        for y in range(y_diff + 1):
            next_val = p1[0] + ":" + str(int(y_start) + y)
            # print("Y: ", next_val)
            if next_val not in underwater_map:
                underwater_map[next_val] = 0
            underwater_map[next_val] += 1
    return underwater_map


def extract_line(line):
    points = line.split()
    return [point.split(',') for point in points if ">" not in point] 


def is_line(p1, p2):
    return p1[0] == p2[0] or p1[1] == p2[1]

def is_diagonal_line(p1, p2):
    x_diff = abs(int(p1[0]) - int(p2[0]))
    y_diff = abs(int(p1[1]) - int(p2[1]))
    return p1[0] == p2[0] or p1[1] == p2[1] or x_diff == y_diff

def mark_line2(p1, p2, underwater_map):
    x_diff = abs(int(p1[0]) - int(p2[0]))
    y_diff = abs(int(p1[1]) - int(p2[1]))
    if x_diff == y_diff:
        start, end = [p1, p2] if int(p1[0]) < int(p2[0]) else [p2, p1]
        grad = 1 if (int(end[1]) - int(start[1])) > 0 else -1
        x_start, y_start = start
        for y in range(y_diff + 1):
            next_val = str(int(x_start) + y) + ":" + str(int(int(y_start) + int(y * grad)))
            if next_val not in underwater_map:
                underwater_map[next_val] = 0
            underwater_map[next_val] += 1
        return underwater_map
    elif x_diff > 0:
        x_start = p1[0] if int(p1[0]) < int(p2[0]) else p2[0]
        for x in range(x_diff + 1):
            next_val = str(int(x_start) + x) + ":" + p1[1]
            if next_val not in underwater_map:
                underwater_map[next_val] = 0
            underwater_map[next_val] += 1
        return underwater_map
    elif y_diff > 0:
        y_start = p1[1] if int(p1[1]) < int(p2[1]) else p2[1]
        for y in range(y_diff + 1):
            next_val = p1[0] + ":" + str(int(y_start) + y)
            if next_val not in underwater_map:
                underwater_map[next_val] = 0
            underwater_map[next_val] += 1
        return underwater_map


def draw_map(underwater_map):
    max_x = int(max([point.split(":")[0] for point in list(underwater_map.keys())]))
    max_y = int(max([point.split(":")[1] for point in list(underwater_map.keys())]))
    new_map =  [["." for i in range(max_x + 1)] for j in range(max_y + 1)]
    for i in range(max_x + 1):
        for j in range(max_y + 1):
            val = f"{i}:{j}"
            if val in underwater_map:
                new_map[j][i] = str(underwater_map[val])
    for row in new_map:
        print(row)

def find_dangerous_vent(input):
    underwater_map = {}
    for i in input:
        p1, p2 = extract_line(i)
        # print("Draw: ", p1, p2)
        if is_line(p1, p2):
            underwater_map = mark_line(p1, p2, underwater_map)
    return len([x for x in list(underwater_map.values()) if x > 1])


def find_dangerous_vent_diagonal(input):
    underwater_map = {}
    for i in input:
        p1, p2 = extract_line(i)
        if is_diagonal_line(p1, p2):
            underwater_map = mark_line2(p1, p2, underwater_map)
    return len([x for x in list(underwater_map.values()) if x > 1])


if __name__ == "__main__":
    with open('part1.txt') as f:
        input = f.read().splitlines()
        ans = find_dangerous_vent(input)
        print(f'Part 1: {ans}')

    with open('part2.txt') as f:
        input = f.read().splitlines()
        ans = find_dangerous_vent_diagonal(input)
        print(f'Part 2: {ans}')
