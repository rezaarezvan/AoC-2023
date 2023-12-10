inp = open('input').read().split()
W = len(inp[0])
H = len(inp)

inp = ''.join(inp)

dmap = {
    'S': [],
    '|': [W, -W],
    '-': [-1, 1],
    '.': [],
    '7': [-1, W],
    'L': [1, -W],
    'J': [-1, -W],
    'F': [1, W]
}

spos = inp.find('S')
path = {spos}
inp = [dmap[c] for c in inp]

for i, offsets in enumerate(inp):
    if spos in (i + o for o in offsets):
        dmap['S'].append(i - spos)

dist = 0
new = None
while 1:
    new2 = new
    new = set()
    for p in (new2 or path):
        for offset in inp[p]:
            if p + offset not in path:
                new.add(p + offset)

    if new:
        path |= new
        dist += 1
    else:
        break
print('Part 1:', dist)

inside = 0
for i in range(len(inp)):
    if i in path:
        continue
    outside_right = outside_left = True
    j = i
    while j > 0:
        if j in path and 1 in inp[j]:
            outside_right = not outside_right
        if j in path and -1 in inp[j]:
            outside_left = not outside_left
        j -= W

    if not (outside_right or outside_left):
        inside += 1

print('Part 2:', inside)
