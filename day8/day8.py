import math

inp = [x for x in open("input").read().strip().split('\n\n')]
inst = list(inp[0])
map = {}

for l in inp[1].split("\n"):
    a = l.split(" ")[0]
    b = l.split("(")[1].split(",")[0]
    c = l.split(" ")[3].split(")")[0]
    map[a] = (b, c)

pos = 'AAA'
p1 = 0
while pos != 'ZZZ':
    d = inst[p1 % len(inst)]
    pos = map[pos][0 if d == 'L' else 1]
    p1 += 1


def calcstep(start):
    pos = start
    idx = 0
    while not pos.endswith('Z'):
        d = inst[idx % len(inst)]
        pos = map[pos][0 if d == 'L' else 1]
        idx += 1
    return idx


p2 = 1
for start in map:
    if start.endswith('A'):
        p2 = math.lcm(p2, calcstep(start))

print(p1)
print(p2)
