import re
inp = [l.strip() for l in open('input')]
p1 = 0
p2 = 0
for game in inp:
    colors = re.findall(r'(\d+) (\w+)', game)
    if all([int(n) <= 12 for (n, c) in colors if c == 'red']) and all([int(n) <= 13 for n, c in colors if c == 'green']) and all([int(n) <= 14 for n, c in colors if c == 'blue']):
        p1 += int(re.findall(r'(\d+)', game)[0])
    p2 += max([int(n) for (n, c) in colors if c == 'red']) * max([int(n) for (n, c) in colors if c == 'green']) * max([int(n) for (n, c) in colors if c == 'blue'])
print(p1)
print(p2)
