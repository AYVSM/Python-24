print( "<<< \t\t PENJUALAN \t\t >>>")

harga = int (input("Masukkan harga \t: "))
qty = int (input ("Masukkan jumlah beli \t:"))

subTotal = harga * qty
if qty >= 12:
    diskon = 0.20 * subTotal
else:
    diskon = 0

Total = subTotal - diskon
print ( f"Subtotal\t:Rp. {subTotal}" )
print ( f"Diskon\t:Rp. {diskon}" )
print ( f"Total\t:Rp. {Total}" )
