ps = list(map(str.split, open('input').read().split('\n\n')))


def solve(p):
    for i in range(len(p)):
        if sum(c != d for l, m in zip(p[i-1::-1], p[i:])
               for c, d in zip(l, m)) == s:
            return i
    else:
        return 0


for s in 0, 1:
    print(sum(100 * solve(p) + solve([*zip(*p)]) for p in ps))
