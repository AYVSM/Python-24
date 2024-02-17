print("Belah ketupat")
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

print("kupu-kupu :")
for i in range(1, 6):
    print("+" * i + " " * (10 - 2 * i) + "+" * i)
for i in range(4, 0, -1):
    print("+" * i + " " * (10 - 2 * i) + "+" * i)