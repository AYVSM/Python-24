#__main__
print(f"__name__ yang di main : {__name__}")

import fungsi

def tambah(a, b):
    return a + b

import Module

if __name__ == "__name__":
    a = 6
    b = 8
    print(f"result : { tambah(a,b)}")