import tkinter as tk
from tkinter import ttk as tema
import ttkbootstrap as tk
from tkinter import messagebox
from math import sqrt
root = tk.Window("Vapor")

a = tk.IntVar()
b = tk.IntVar()
c = tk.IntVar()
S = tk.IntVar()
Area = tk.IntVar()

def Heron():
    length_a = a.get()
    length_b = b.get()
    length_c = c.get()

    if length_a + length_b > length_c and length_a + length_c > length_b and length_b + length_c > length_a:
        
        S = (length_a+length_b+length_c)/2

        area = sqrt(S*(S-length_a)*(S- length_b)*(S-length_c))

        Area.set(f"{area:.2f}")
    else:
        messagebox.showerror("tidak memenuhi ketaksamaan segitiga")
        
root.title("Rumus Heron")
root.geometry("400x400")
root.resizable(True, True)
root.config(bg="gray")

frame = tema.Frame(root)
frame.pack(padx=10, pady=10, fill="both", expand=True)

label_a = tema.Label(frame, text="Masukkan Panjang sisi A")
label_a.pack(padx=10, fill="x", expand=True)
entry_a = tema.Entry(frame, textvariable=a)
entry_a.pack(padx=10, fill="x", expand=True)

label_b = tema.Label(frame, text="Masukkan Panjang sisi B")
label_b.pack(padx=10, fill="x", expand=True)
entry_b = tema.Entry(frame, textvariable=b)
entry_b.pack(padx=10, fill="x", expand=True)

label_c = tema.Label(frame, text="Masukkan Panjang sisi C")
label_c.pack(padx=10, fill="x", expand=True)
entry_c = tema.Entry(frame, textvariable=c)
entry_c.pack(padx=10, fill="x", expand=True)

button_hitung = tema.Button(frame, text="Start", command=Heron)
button_hitung.pack(padx=10, pady=10, fill="x", expand=True)

label_Area = tema.Label(frame, text="Luas Segitiga:")
label_Area.pack(padx=10, pady=5, fill="x", expand=True)
entry_Area = tema.Entry(frame, textvariable=Area, state="readonly")
entry_Area.pack(padx=10, pady=5, fill="x", expand=True)

root.mainloop()
