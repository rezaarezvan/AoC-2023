inp = [l.strip() for l in open('input')]
p1 = 0
p2 = {}

for i, card in enumerate(inp):
    if i not in p2:
        p2[i] = 1
    card = card.split('|')
    wins = card[0].split()
    have = card[1].split()
    x = len(set(wins) & set(have))
    if x > 0:
        p1 += 2 ** (x - 1)
    for j in range(i + 1, min(len(inp), i + x + 1)):
        p2[j] = p2.get(j, 1) + p2[i]
print(p1)
print(sum(p2.values()))
