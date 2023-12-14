from functools import cache

inp = [l.split() for l in open("input").read().strip().split("\n")]
rows = [(w1, tuple(map(int, w2.split(",")))) for w1, w2 in inp]


@cache
def solvs(s, sizes, num_done_in_group=0):
    if not s:
        return not sizes and not num_done_in_group
    num_sols = 0
    possible = [".", "#"] if s[0] == "?" else s[0]
    for c in possible:
        if c == "#":
            num_sols += solvs(s[1:], sizes, num_done_in_group + 1)
        else:
            if num_done_in_group:
                if sizes and sizes[0] == num_done_in_group:
                    num_sols += solvs(s[1:], sizes[1:])
            else:
                num_sols += solvs(s[1:], sizes)
    return num_sols


print(sum(solvs(group + ".", sizes) for group, sizes in rows))
print(sum(solvs("?".join([group] * 5) + ".", sizes * 5)
      for group, sizes in rows))
