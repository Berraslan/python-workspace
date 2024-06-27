# #fonksiyonaları dinamik hale getirmek için fonkisyona dışarıdan parametre gönderme
#
# isimGir = input("İsminizi giriniz: ")
# soyisimGir = input("Soyisim giriniz : ")
#
#
# def greetings(isimGir, soyisimGir):
#     return (f"Merhaba {isimGir} {soyisimGir} ! ")
#
#
# print(greetings(isimGir,soyisimGir))#burada mutlaka parametre bilgilerini buraya yazmamış gerekiyor ve bu durum bizim string tabanlı değil de daha dinamik ve değişken bir yapı kurmamızı sağlar.
#
# def greetings(isim):
#     return 'Merhaba,'+ isim
#
#
# print(greetings("berra"))#yukarıdaki ilk örenkten farklı olarak greetins içide isim değişkeni oluşturduk ve print ile bastırırkende isim değişkenine parametre gönderiyoruz
#
# #dinamik tabanlı bir toplama işlemi yapalım

def sum(sayi1, sayi2):
    return sayi1 + sayi2


print(sum(10,
          20))  #burada sum() fonskiyonu içine yadığımız parametreler gider ve gereken işlem yapıldıktan sonra printle ekrana bastırılır.


#doğum yılını dianmik bir şekilde hesaplama

#bilgisayar yılını aldık gidip oraya 2024-birthdate de diyebilirdik ama bu şekilde fonksiyon tanımlayarak yapmak çom daha dinamik oldu.
def year():
    import datetime
    return datetime.datetime.now().year


def calculateAge(birthDate):
    return year() - birthDate  #year normalde bir fonksiyon olmasına rağmen retun ile değer döndürme kullanılınca artık bi nevi değer tutucu değişken gibi davraıp içinde tuttuğu değerle işlem yapılabiliyor


#ayrıca birtDate parametre olark kullanıcıdan print ekranında sorulur içeri gönderilir hesaplar ve sonuç kullanıcını gönderdiği parameetre ye göre sonuç verir
print(calculateAge(2001))


def whenRetirment(birtDate, isim):
    age = calculateAge(birtDate)
    leftTime = 65 - age

    if leftTime>0:
        return f"{isim} emekliliğinize {leftTime} yıl kaldı"
    else:
        return f"{isim} ,zaten {abs(leftTime)} yıl önce emekli oldunuz" #abs burada mutlak değer alır mesela kişi 80 yaşında ise |65-80| mutlak değere alınıp pozitif değer çıkar ve kaç yıl önce emekli olduğunu söyler.


print(whenRetirment(2001, "berra"))
