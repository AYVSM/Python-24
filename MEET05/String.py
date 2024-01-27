data = "int string"
print( "data =", type(data))

# Ada 2 cara membuat string di python,
#1. Double Quote
#2. Single Quote
data = " Ini menggunakan Double Quote "
print(data)
data = " Ini menggunakan Single Quote "
print(data)

print( "' Tester 1 '")
print( '" Tester 2 "')

#String dengan simbol \
print( " Hari jum'at " )
print( ' Hari jum\'at ' )

#\n
print( "\nKalimat Pertama \nKalimat Kedua \nKalimat ketiga" )

#Backlash
print( "c:\\user\\Albert " )

#backspace
print("Lebih \bDekat")

#Literal String
print("""
Nama : Albert
Kelas : 10
""")
# raw : untuk mengabaikan simbol apapun yang tampil
print( r"c:\new folder" )

#Literal string dan Raw
print( """
Nama : Budi
Kelas : 9\nine
Alamat : pig
""")