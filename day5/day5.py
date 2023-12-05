inp = open('input').read().strip()
parts = inp.split('\n\n')
seed, *others = parts
seed = [int(x) for x in seed.split(':')[1].split()]


def parse_function(s):
    return [tuple(map(int, line.split())) for line in s.split('\n')[1:]]


def P1(groups, x):
    for (dst, src, sz) in groups:
        if src <= x < src + sz:
            return x + dst - src
    return x


def P2(groups, R):
    A = []
    for (dest, src, sz) in groups:
        src_end = src + sz
        NR = []
        for (st, ed) in R:
            before = (st, min(ed, src))
            inter = (max(st, src), min(src_end, ed))
            after = (max(src_end, st), ed)
            if before[1] > before[0]:
                NR.append(before)
            if inter[1] > inter[0]:
                A.append((inter[0] - src + dest, inter[1] - src + dest))
            if after[1] > after[0]:
                NR.append(after)
        R = NR
    return A + R


Fs = [parse_function(s) for s in others]

P1s = []
P2s = []

for x in seed:
    for groups in Fs:
        x = P1(groups, x)
    P1s.append(x)

pairs = list(zip(seed[::2], seed[1::2]))
for st, sz in pairs:
    R = [(st, st + sz)]
    for groups in Fs:
        R = P2(groups, R)
    P2s.append(min(R)[0])

print(min(P1s))
print(min(P2s))
