import re


def mul(match):
    return int(match[0]) * int(match[1])


def solve():
    with open('3.real') as fin:
        ins = ''.join([e.strip() for e in fin.readlines()])

        matches = [(x.groups(), x.span()) for x in re.finditer(r'mul\((\d?\d?\d),(\d?\d?\d)\)', ins)]

        print(sum([mul(_[0]) for _ in matches]))

        enabled, total, queue = True, 0, []
        for ele in [(x.groups(), x.span()) for x in re.finditer(r"(don\'t\(\))", ins)]:
            queue.append((ele[1][0], 'dont'))
        for ele in [(x.groups(), x.span()) for x in re.finditer(r"(do\(\))", ins)]:
            queue.append((ele[1][0], 'do'))
        for ele in matches:
            queue.append((ele[1][0], 'add', mul(ele[0])))

        for obj in sorted(queue, key=lambda x: x[0]):
            if obj[1] == 'do':
                enabled = True
            elif obj[1] == 'dont':
                enabled = False
            elif obj[1] == 'add':
                if enabled:
                    total += obj[2]
        print(total)


if __name__ == '__main__':
    solve()
