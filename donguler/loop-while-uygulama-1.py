#klavyeden girilen n sayıda öğrenci bilgisini liste içerisinde saklayınız.
#** dictionary listesi yapısı (ogrenciNo,ogrenciAdi,ogreciSoyadi) şeklinde olsun.
#** öğrenci ekleme işlemi bitince öğrencileri listeleyiniz.

ogrenciler = [] #buradaki listeler değişkenler geçicidir bellekte saklanır ve her çalıştırmada silinir içindeki bilgiler
#kalıcı olmasını istiyorsak bir veritabanı bir servis veya bir json uzsntılı dosya veya not defteri içindeki bilgiler tanımlanabilir.

devammi = input("ogrenci ekleme başlasın mı ? (e/h)")

while (devammi != "h"):

    ogrenciAdi = input("ogrenci Adı giriniz : ")
    ogrenciSoyadi = input("ogrenci Soyadı giriniz : ")
    ogrenciNo= input("ogrenciNo giriniz : ")

    ogrenciler.append({ "ogrenciAdi": ogrenciAdi,
                        "ogrenciSoyadi": ogrenciSoyadi,
                        "ogrenciNo": ogrenciNo
                       })
    devammi = input("devam edilsin mi? (e/h)")


for ogrenci in ogrenciler:
    print(f"Ogrenci Adı : {ogrenci['ogrenciAdi']} , Ogrenci Soyadı : {ogrenci['ogrenciSoyadi']} , Ogrenci No : {ogrenci['ogrenciNo']}")


#kodun çalışma mantığı : devammi ile ön