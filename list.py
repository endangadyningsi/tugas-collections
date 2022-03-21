buah = ["anggur","jeruk","mangga","apek"]
for i in buah:
    print(i)

i = 0
while i < len(buah):
    print (buah[i])
    i += 1

#membuat contoh list
#mengupdate

buah = ["anggur","jeruk","mangga","apel"]
buah[0] = "sirsak"
print(buah)

#membuat contoh list
#menambahkan

buah = ["anggur","jeruk","mangga","apel"]
buah.append("jambu")
print(buah)

buah.extend(["pear","kurma"])
print(buah)

buah.insert(3, "durian")
print(buah)

#membuat daftar contoh
#menghapus

buah = [ "anggur" , "jeruk" , "mangga" , "apel" ]
buah.pop()
print (buah)

del  buah[ 1 ]
print (buah)

buah.remove( "anggur" )
print (buah)