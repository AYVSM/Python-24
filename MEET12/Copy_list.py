#copy
data1 = [1,2,3,4]
data2 = ["a","b","c"]
dataList1 = data1 
print(f"data1 = {data1}")
print(f"dataList1 = {dataList1}")
data1[-1] = 100
print(f"data1 UPDATE= {data1}")
print(f"dataList1 UPDATE= {dataList1}")
print(f"Memory Address data1 = {hex(id(data1))}")
print(f"Memory Address dataList1 = {hex(id(dataList1))}")

print("-"*15)
dataList2 = data2.copy()
print(f"Memory Address data2 = {hex(id(data2))}")
print(f"Memory Address dataList2 = {hex(id(dataList2))}")
data2[0] = "xyz"
print(f"data2 UPDATE= {data2}")
print(f"dataList2 UPDATE= {dataList2}")

print("-"*15, "Nested List")
data1 = ["I", "G", "S"]
data2 = [10,11,12]
dataList = [data1, "x", "y", "z", data2]
print(f"dataList = {dataList}")
print(f"dataList[0] = {dataList[0]}")
print(f"dataList[0][1] = {dataList[0][1]}")
dataList_copy = dataList.copy()
print(f"Memory Addres dataList = {hex( id(dataList))}")
print(f"Memory Addres dataList_copy = {hex( id(dataList_copy))}")
dataList[-1][-1] = 100
print(f"dataList UPDATE= {dataList}")
print(f"dataList_copy UPDATE= {dataList_copy}")

print("-"*15, "DeepCopy")
from copy import deepcopy
datals = deepcopy(dataList)
print(f"dataList = {dataList}")
print(f"datals = {datals}")
dataList[-1][0] = 777
print(f"datalist UPDATED= {dataList}")
print(f"datals UPDATED= {datals}")

print("-"*15, "Comprehension")
data = [i for i in range(5)]
print(data)