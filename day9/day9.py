inp = [[int(i) for i in s.split()]
       for s in open('input').read().split('\n') if s.strip()]


def n(line):
    if sum(i != 0 for i in line) == 0:
        return 0
    m = []
    for i in range(len(line)-1):
        m.append(line[i+1]-line[i])
    return line[-1] + n(m)


print(sum(n(i) for i in inp))
print(sum(n(i[::-1]) for i in inp))
