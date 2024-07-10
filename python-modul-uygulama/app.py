#app.py dosyamız ise ana main dosyamızdır diğer modüller aslında burada kargaşıklık olmasın hepsi tek bir sayfada yer almasın diye yapıldı burada sadece proje materyallerini çağırıp aksiyon alırız
#burada çok kod yazılmaz.

from methods import *
from db import *

# #methods modulü üzerinden urunEkle() fonksiyonuna erişebiliriz bunu da moduleAdi.fonkisyonAdi() üzerinden farklı bir modulde çağırabilirz
# urunEkle("vestel",900000000)
# print(db.urunler)
#
# #urunleriGetir fonkisyonunu sonuc değişkeni içine atayıp yazdırdık
# sonuc = urunleriGetir()
# #sonuc değeri içine atanmış urunGetir fonksiyonu for döngüsüne girip her i urunAdi değerini geip print edicek
# for  i in sonuc:
#     print(i["urunAdi"])

# urunGuncelle(1,"iphone 16",90000)
#
# for i in urunleriGetir():
#     print(i["urunAdi"])

sonuc = urunleriSil(1)

for i in urunler:
    print(i)