print("\n<<< FIBONACCI >>>\n")
print("-"*20)

data = int(input("Masukkan angka: "))
print("-"*20)

Data1 = [1, 2]  
[Data1.append(Data1[i-1] + Data1[i-2]) for i in range(2, data)] 
print(Data1)

print("-"*5, "Cara Kedua", "-"*5)

Data2 = int(input("Masukkan angka: "))
print("-"*20)

DataList = [1, 2]  
for i in range(2, Data2):
    DataList.append(DataList[i-1] + DataList[i-2])  

print(DataList)
