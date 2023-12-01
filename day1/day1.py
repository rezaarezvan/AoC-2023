inp = [l.strip() for l in open('input')]
nums = []
m = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
     "six": 6, "seven": 7, "eight": 8, "nine": 9}
for w in inp:
    r = ""
    for char in w:
        if char.isdigit():
            r += char

    r = r[0] + r[-1]
    nums.append(int(r))
print(sum(nums))
nums = []
for w in inp:
    r = ""
    for num in m:
        if num in w:
            w = w.replace(num, num + str(m[num]) + num)
    for char in w:
        if char.isdigit():
            r += char
    r = "".join(r)
    r = r[0] + r[-1]
    nums.append(int(r))
print(sum(nums))
