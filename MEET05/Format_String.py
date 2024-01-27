#3 cara untuk membuat Format string :
#1. format ( % )
#2. Format String
#3. f.String

umur = 17 #tipe data : Integer (i/6
nama = " Budi " #tp : String (s)
ukuran_sepatu = 41.5 # tp : Float (f )
# Dengan Format %
print( "Hei nama saya %s, umur dia %d dan memiliki ukuran sepatu %0.2f " %(nama, umur, ukuran_sepatu) )

print( "-"*15, "Format String")
print("1.Array : Hei nama saya {0} umur saya {1} dan memiliki ukuran sepatu {2}" .format( nama, umur, ukuran_sepatu) )

print("2.initial : Hei nama saya {nm} umur saya {u} dan memiliki ukuran sepatu {us}" .format( nm = nama, u = umur, us = ukuran_sepatu) )

print( "-"*15, ">f.String")
print( f"Dengan f.string : Hei nama saya {nama} umur saya {umur} dan memiliki ukuran sepatu {ukuran_sepatu} ")

print("-"*15, " Alignment dengan Format String ")
print( "nama : [ {0} ]" .format(nama) )
print( "nama : [ {} ]" .format(nama) )
print( "nama : [ {:<15} ]" .format(nama) )
print( "nama : [ {:>15} ]" .format(nama) )
print( "nama : [ {:^15} ]" .format(nama) )

print( "-"*15, " Alignment dengan f.string")
print( f"nama : [ {nama} ]" )
print( f"nama : [ {nama:<15} ]" )
print( f"nama : [ {nama:>15} ]" )
print( f"nama : [ {nama:^15} ]" )
print( f"nama : [ {nama:+<15} ]" )

print("-"*15, "Alignment dengan %")
print( "nama : [ %s ]" %(nama))
print( "nama : [ %-15s ]" %(nama))
print( "nama : [ %+15s ]" %(nama))