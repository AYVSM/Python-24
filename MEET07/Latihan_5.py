x = int (input("Masukkan koordinat x :"))
y = int (input("Masukkan koordinat y :")) 

if (x > 0 and y > 0):
    print(f"Koordinat {x,y} berada di Kuadran I")
elif (x < 0 and y > 0):
    print(f"Koordinat {x,y} berada di Kuadran II")
elif (x < 0 and y < 0):
    print(f"Koordinat {x,y} berada di kuadran III")
elif (x > 0 and y < 0):
    print(f"Koordinat {x,y} berada di Kuadran IV")
else:
    print("Koordinat pusat")