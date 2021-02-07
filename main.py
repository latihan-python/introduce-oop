from geometry.persegipanjang import PersegiPanjang
from geometry.segitiga import Segitiga


p1 = PersegiPanjang(10, 3)
print(p1.info())
print(p1.hitung_luas())

s1 = Segitiga(10, 3)
print(s1.info())
print(s1.hitung_luas())

# Polymorphism merupakan objek yang merespon metode dengan implementasi berbeda - beda
print('\nPolymorphism')
daftar_bangun_ruang = []
daftar_bangun_ruang.append(p1)
daftar_bangun_ruang.append(s1)

for objek_bangun_ruang in daftar_bangun_ruang:
    print(objek_bangun_ruang.info())