def calc(time, record):
    count = 0
    for x in range(time):
        distance = x * (time - x)
        if distance > record:
            count += 1

    return count


p1 = 1
for time, record in [(34, 204), (90, 1713), (89, 1210), (86, 1780)]:
    p1 *= calc(time, record)


time = 34908986
dist = 204171312101780
p2 = calc(time, dist)

print(p1)
print(p2)
