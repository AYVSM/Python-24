num = int((input("Masukkan nilai 10-15 atau 20-25 atau 35-40 : ")))

a = num > 10 and num < 15 #11, 12, 13, 14, 15
b = num > 20 and num < 25 #21, 22, 23, 24, 25
c = num > 35 and num < 45 #36, 37, 38, 39, 40

while int(a or b or c):
    num = int((input("Masukkan nilai 10-15 atau 20-25 atau 35-40 : ")))
    print("Salah...")
else:
    print("Benar...")