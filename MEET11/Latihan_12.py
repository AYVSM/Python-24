List = [ "Do", "Re", "Mi", "Fa", "So", "La", "Ti"]
print(f"Sebelum diubah{List}")

print("<------------------------>")

#Cara Pertama
New_List = List[2:3] + List[:1] + List[3:7] + List[1:2]
print(f"Sesudah diubah(cara pertama){New_List}")

#Cara Kedua
New_List_1 = List[2], List[0], List[3], List[4], List[5], List[6], List[1]
print(f"Sesudah diubah(cara kedua){New_List_1}")

