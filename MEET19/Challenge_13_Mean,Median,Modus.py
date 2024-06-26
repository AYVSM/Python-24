import os
print("_"*10, "Nilai Mean, Median, Modus", "_"*10)
def mean_function(*args):
    total = sum(args)
    count = len(args)
    if count == 0:
        return 0
    return total / count

def median_function(*args):
    urutan = sorted(args)
    count1 = len(args)

    #kalau banyak datanya ganjil maka:
    if count1 % 2 == 1:
        median = urutan[count1 // 2]
    #kalau banyak datanya genap maka:
    else:
        mid_left = urutan[(count1 // 2) - 1]
        mid_right = urutan[count1 // 2]
        median = (mid_left + mid_right) / 2

    return median

def modus_function(*args):
    frekuensi = {}
    for angka in args:
        if angka in frekuensi:
            frekuensi[angka] += 1
        else:
            frekuensi[angka] = 1
    
    modus = []
    maks_frekuensi = max(frekuensi.values())
    for ABC, value in frekuensi.items():
        if value == maks_frekuensi:
            modus.append(ABC)
    return modus

def main():
    data = []
    while True:
        inputan = input("Masukkan angka: ")
        os.system('cls' if os.name == 'nt' else 'clear')
        if inputan.isdigit():
            num = int(inputan)
            data.append(num)
        else:
            print("Input tidak valid. Masukkan angka.")
            continue
        
        print("_"*10, "Nilai Mean, Median, Modus", "_"*10)
        Lanjut = input("Lanjut (y/n): ")
        if Lanjut.lower() != "y":
            break

    if data:
        hasil_modus = modus_function(*data)
        hasil_mean = mean_function(*data)
        hasil_median = median_function(*data)
        print("_"*10, "Nilai Mean, Median, Modus", "_"*10)
        print(f"Deret angka = {data}")
        print(f"Hasil mean = {hasil_mean}")
        print(f"Hasil median = {hasil_median}")
        print(f"Hasil modus = {hasil_modus}")
main()
