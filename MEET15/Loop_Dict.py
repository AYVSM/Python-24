dataDict = {
    "plm" : "Palembang",
    "em" : "Muara Enim",
    "pr" : "Prabumulih",
    "llg" : "LubukLinggau",
}
for i in dataDict:
    print(f"i = {i}")

print(f"-"*15, "KEYS")
print(f"Keys in dataDict = {dataDict.keys()}")
for z in dataDict.keys():
    print(f"z = {z}")

print(f"-"*15, "Value")
print(f"Values in dataDict = {dataDict.values()}")
for x in dataDict.values():
    print(f"x = {x}")

print(f"-"*15, "items")
print(f"items in dataDict = {dataDict.items()}")
for x, v in dataDict.items():
    print(f"x = {x} = {v}")