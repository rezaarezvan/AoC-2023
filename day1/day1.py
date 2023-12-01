inp = [l.strip() for l in open('input')]
nums = []

m = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
     "six": 6, "seven": 7, "eight": 8, "nine": 9}


# Part 1
for word in inp:
    res = ""
    for char in word:
        if char.isdigit():
            res += char

    res = res[0] + res[-1]
    nums.append(int(res))

print(sum(nums))

# Part 2
nums = []
for word in inp:
    res = ""
    for num in m:
        if num in word:
            word = word.replace(num, num + str(m[num]) + num)
    for char in word:
        if char.isdigit():
            res += char

    res = "".join(res)
    res = res[0] + res[-1]
    nums.append(int(res))


print(sum(nums))
