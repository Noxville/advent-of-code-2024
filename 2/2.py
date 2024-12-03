def valid(line):
    if line[0] == line[1]:
        return 0
    deltas = [y - x for (y, x) in zip(line, line[1:])]
    if all(_ in (1, 2, 3) for _ in deltas) or all(_ in (-1, -2, -3) for _ in deltas): 
        return 1
    return 0


def valid_with_removal(line):
    for idx in range(-1, len(line)):
        case = line if idx == -1 else [_ for (i, _) in enumerate(line) if i != idx]
        if valid(case):
            return 1
    return 0


def solve():
    with open('2.real') as fin:
        ls = [list(map(int, e.strip().split(' '))) for e in fin.readlines()]
        print(sum([valid(_) for _ in ls]))
        print(sum([valid_with_removal(_) for _ in ls]))


if __name__ == '__main__':
    solve()
