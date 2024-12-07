def valid(goal, nums, allow_concat=False):    
    if len(nums) == 1:
        return goal == nums[0]

    a, b, rest = nums[0], nums[1], nums[2:]
    if valid(goal, [a + b] + rest, allow_concat):
        return True
    elif valid(goal, [a * b] + rest, allow_concat):
        return True
    elif allow_concat:
        if valid(goal, [int(str(a) + str(b))] + rest, allow_concat):
            return True
    return False


def solve():
    with open('7.real') as fin:
        cases = [(int(line.split(':')[0]),
                  list(map(int, line.split(':')[1].strip().split(' '))))
                 for line in [e.strip() for e in fin.readlines()]]
        print(sum([_[1] for _ in [(valid(g, ints), g) for (g, ints) in cases] if _[0]]))
        print(sum([_[1] for _ in [(valid(g, ints, allow_concat=True), g) for (g, ints) in cases] if _[0]]))


if __name__ == '__main__':
    solve()
