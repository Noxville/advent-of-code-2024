from collections import defaultdict


def solve():
    mx, my, grid = 0, 0, {}
    with open('4.real') as fin:
        for y, line in enumerate(fin.readlines()):
            for x, c in enumerate(line.strip()):
                grid[(y, x)], mx, my = c, max(mx, x), max(my, y)

    found = 0
    for sx in range(1 + mx):
        for sy in range(1 + my):
            for (dx, dy) in [(1, 1), (-1, -1), (-1, 0), (+1, 0), (0, -1), (0, +1), (+1, -1), (-1, +1)]:
                good, cells = True, []
                for (step, exp) in [(0, 'X'), (1, 'M'), (2, 'A'), (3, 'S')]:
                    yx = (sy + step * dy, sx + step * dx)
                    if grid.get(yx, '') != exp:
                        good = False
                if good:
                    found += 1
    print(found)

    # Part 2
    mas = defaultdict(int)
    for sx in range(1 + mx):
        for sy in range(1 + my):
            for (dx, dy) in [(1, 1), (-1, -1), (+1, -1), (-1, +1)]:
                good, cells = True, []
                for (step, exp) in [(0, 'M'), (1, 'A'), (2, 'S')]:
                    yx = (sy + step * dy, sx + step * dx)
                    if grid.get(yx, '') != exp:
                        good = False
                if good:
                    mas[(sy + dy, sx + dx)] += 1
    print(len([1 for ((x, y), c) in mas.items() if c >= 2]))


if __name__ == '__main__':
    solve()
