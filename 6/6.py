import time

dirs = {'N': (0, -1), 'S': (0, +1), 'E': (+1, 0), 'W': (-1, 0)}
turns = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}


def bfs(grid, cur):
    direction, seen = 'N', set()
    while (cur in grid) and ((cur, direction) not in seen):
        seen.add((cur, direction))
        nx, ny = cur[0] + dirs[direction][0], cur[1] + dirs[direction][1]
        if grid.get((nx, ny)) == '#':
            direction = turns[direction]
        else:
            cur = (nx, ny)
    return seen, (cur, direction) in seen  # list of ((x,y), d) and bool for if we terminated from a loop or fell off


def solve():
    with open('6.real') as fin:
        grid = {(x, y): c for y, line in enumerate([e.strip() for e in fin.readlines()])
                for x, c in enumerate(line)}
        start = list(filter(lambda kv: kv[1] == '^', grid.items()))[0][0]
    path = set([_ for _, v in bfs(grid, start)[0]])

    print(len(path))  # part 1
    print(sum([bfs(grid | {obstacle: '#'}, start)[1] for obstacle in path]))


if __name__ == '__main__':
    st = time.perf_counter()
    solve()
    end = time.perf_counter()
    elapsed = end - st
    print(f'Time taken: {elapsed:.6f} seconds')
