i = 0
count = 20
space = int(1/2 * count) - 1
while True:
    if i == count:
        break
    elif i % 2:
        print(f" "*space, "+"*i)
        space -= 1
    i += 1

i = 18
count = 0
space = int(1/2 * count) + 1
while True:
    if i == count:
        break
    elif i % 2:
        print(f" "*space, "+"*i)
        space += 1
    i -= 1