#Menggunakan loop
print("\n<< Prima dan Komposit >>")
print("-"*15)

min = int(input("Masukkan angka minimum: "))
max = int(input("Masukkan angka maksimum: "))

prime = []
composite = {}

for number in range(min, max + 1):
    if number > 1:
        is_prime = True
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_prime = False
                composite[number] = None  
                break
        if is_prime:
            prime.append(number)

print("-"*15)
print("\n<< Prima >>")
print("-"*15)

print("Bilangan Prima:")
print(prime)

print("\n<< Komposit >>")
print("-"*15)

print("Bilangan Komposit:")
print(list(composite.keys()))