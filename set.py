#membuat contoh tuple
hewan = ("sapi", "kuda", "kelinci", "buaya", "cicak")

#menampilkan tuple dengan perulangan
for i in hewan :
   print(i)

a = 0
while a < len(hewan):
   print(hewan[a])
   a += 1

hewan = list(hewan)

#mengupdate salah satu tuple
hewan [2] = "ayam"
print(hewan)

#menghapus salah satu tuple
hewan.pop()
print(hewan) 

hewan.remove ("kuda")
print(hewan)

del hewan [0:2]
print(hewan)

#menambahkan tuple
hewan.append ("cacing")
print(hewan)

hewan. extend(["kambing", "semut"])
print(hewan)

hewan.insert(3, "elang")
print(hewan)