data1 = int( input("Masukkan data1 = "))
hasil = 20 < data1 < 23 or 34 < data1 < 38 or 40 < data1 < 42
print(hasil)

# Cara kedua
a = data1 > 20
b = data1 < 23
hasil1 = a and b

c = data1 > 34
d = data1 < 38
hasil2 = c and d

e = data1 > 40
f = data1 < 42
hasil3 = e and f

hasil = hasil1 or hasil2 or hasil3
print(hasil)