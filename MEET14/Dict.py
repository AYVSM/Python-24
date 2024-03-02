#Dictionary = Assosiation Array
#key : value
#1
dataDict1 = {
    "nama" : "Albert",
    "kelas": "10.1",
    "alamat": "PLG",
    "nama" : "budi"
}
print(f"Dict 1 = {dataDict1}")
#2
dataDict2 = dict(
    nama = "Albert",
    kelas = "10.1",
    alamat = "PLG",
    mapel = ["PJOK","IPS","IPA"]
    #nama = "budi" tidak bisa
)\

print(f"Dict 2 = {dataDict2}")
print(f"1.Nama = {dataDict2["nama"]}")
print(f"2.Nama = {dataDict1.get("nama","tidak ditemukan!")}")
print(f"1.Mapel = {dataDict2["mapel"]}")
print(f"2.Mapel = {dataDict2["mapel"][1]}")
print(f"3.Mapel = {dataDict2.get("mapel")[-1]}")

print("-"*15, "UPDATE & ADD")
dataDict2["nama"] = "Indah"
print(f"Dict 2 = {dataDict2}")
dataDict2["agama"] = "Islam"
print(f"Dict 2 UPDATED 1.= {dataDict2}")
dataDict2.update({"nama" : "Pinky"})
print(f"Dict 2 UPDATED 2.= {dataDict2}")
dataDict2.update(dict(nama = "Kiki", agama = "Kristen"))
print(f"Dict 2 UPDATED 3.= {dataDict2}")
print("-"*15, "remove")
del dataDict2["nama"]
print(f"Dict 2 DEl 1.= {dataDict2}")
dataDict2.clear()
print(f"Dict 2 DEl 2.= {dataDict2}")
print("-"*15, "Empty Dict.")
data = dict()
data.update(dict(a = "Abc", b = "xyz"))
print(data)