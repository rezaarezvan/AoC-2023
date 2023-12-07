from collections import Counter
inp = [i for i in open('input').read().split('\n') if i.strip()]


def eval_hand(h, part1):
    h = h.replace('J', 'X') if part1 else h
    handval = ['J23456789TXQKA'.index(c)for c in h]
    max_rank = 0
    for c in 'J23456789TQKA':
        pairs = sorted(Counter(h.replace('J', c)).values())
        rank = [[1, 1, 1, 1, 1], [1, 1, 1, 2], [1, 2, 2],
                [1, 1, 3], [2, 3], [1, 4], [5]].index(pairs)
        max_rank = max(max_rank, rank)
    return (max_rank, handval)


for part in (True, False):
    hands = sorted((eval_hand(h, part), int(b))
                   for h, b in (l.split() for l in inp))
    print(sum((index + 1) * bet for index, (_, bet) in enumerate(sorted(hands))))
