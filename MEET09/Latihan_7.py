num = int(input("Masukkan angka ganjil > 20 :"))

while num % 2 == 0 or num < 20:
    num = int(input("Masukkan angka ganjil :"))
else:
    print("True..")
