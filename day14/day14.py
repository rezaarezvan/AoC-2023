import re
inp = open('input').read().replace('\n', ' ')


def rot(b): return ' '.join(map(''.join, zip(*(b.split())[::-1])))


def beam_calc(b): return sum(i for r in b.split()
                             for i, c in enumerate(r[::-1], 1) if c == 'O')


def cycle(d): return re.sub('[.O]+', lambda m: ''.join(sorted(m[0])[::-1]), rot(d))


def pcycle(data, n, cache={}):
    for r in range(n):
        data = cycle(cycle(cycle(cycle(data))))
        if s := cache.get(data, 0):
            return cache[(n-s) % (r-s) + (s-1)]
        cache |= {data: r, r: beam_calc(rot(data))}


x = rot(rot(inp))

print(beam_calc(cycle(x)))
print(pcycle(x, 1000000000))
