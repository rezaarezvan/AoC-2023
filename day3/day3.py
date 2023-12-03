import re
from collections import defaultdict
board = [line.strip() for line in open('input').readlines()]
p1 = 0
p2 = 0
gears = defaultdict(list)


def is_adj(r, c, dr, dc, num):
    global gears
    for i in range(r, dr+1):
        for j in range(c, dc+1):
            if 0 <= i < len(board) and 0 <= j < len(board[i]):
                if board[i][j] not in '0123456789.':
                    if board[i][j] == '*':
                        gears[(i, j)].append(num)
                    return True
    return False


for r in range(len(board)):
    for m in re.finditer(re.compile('\d+'), board[r]):
        if is_adj(r-1, m.start()-1, r+1, m.end(), int(m.group(0))):
            p1 += int(m.group(0))
print(p1)

for _, v in gears.items():
    if len(v) == 2:
        p2 += v[0] * v[1]
print(p2)
