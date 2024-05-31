import tkinter as tk
import ttkbootstrap as tb

root = tb.Window( themename = "cosmo")

class tester:
    def __init__(self, master):
        self.master = master
        master.title("klik..")
        master.geometry("400x400")
        self.label1 = tb.Label(text="KLIK SAJA", font=("arial", 25, 'bold'))
        self.label1.pack()
        self.kata1 = tb.Button(text="KATA 1", command=self.defkata1, bootstyle="success")
        self.kata1.pack()
        self.kata2 = tb.Button(text="KATA 2", command=self.defkata2, bootstyle="info")
        self.kata2.pack()
        self.DTY = tb.Button(text="EXIT", command=master.destroy , bootstyle="warning")
        self.DTY.pack()
        self.labelT1 = tb.Label(text="KLIK SAJA", font=("arial", 15, 'italic'))
        self.labelT1.pack()

        self.count_kata1 = 0
        self.count_kata2 = 0

    def defkata1(self):
        self.labelT1.config(text="KATA SATU")
    def defkata2(self):
        self.labelT1.config(text="KATA DUA")

    def defkata1(self):
        self.count_kata1 += 1
        self.labelT1.config(text="Kata1 diklik sebanyak: " + str(self.count_kata1))

    def defkata2(self):
        self.count_kata2 += 1
        self.labelT1.config(text="Kata2 diklik sebanyak: " + str(self.count_kata2))

if __name__== "__main__":
    tester(root)
    root.mainloop()