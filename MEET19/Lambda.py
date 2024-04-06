#Lambda : Statement (costum) Function yang tidak memiliki def

def kuadrat( num ):
    return num **2
print(f"Result Kuadrat : {kuadrat(4)}")

#syntax :
#output = lambda variabel_parameter : expression
ResultKuadrat = lambda abc : abc ** 2
print(f"Result Kuadrat lambda : {ResultKuadrat(4)}")

def pangkat (angka, pangkat ):
    return angka ** pangkat
print(f"Result pangkat : {pangkat(4,3)}")

ResultPangkat = lambda a,b : a ** b