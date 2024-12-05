def check(st, ins_str):
    ins = list(map(int, ins_str.split(',')))
    for i, n in enumerate(ins):
        for j, m in enumerate(ins[i + 1:]):
            if (m, n) in st:
                while True:
                    for x in range(len(ins)):
                        for y in range(x + 1, len(ins)):
                            if (ins[y], ins[x]) in st:
                                ins[x], ins[y] = ins[y], ins[x]
                    return 0, ins[len(ins) // 2]
    return ins[len(ins) // 2], 0


def solve():
    pairs = set()
    with open('5.real') as fin:
        tot = (0, 0)
        for line in [e.strip() for e in fin.readlines()]:
            if '|' in line:
                pairs.add(tuple(map(int, line.split('|'))))
            elif ',' in line:
                tot = tuple(map(sum, zip(tot, check(pairs, line))))
        print(tot)


if __name__ == '__main__':
    solve()
