#fonkisyona default parametre atama işlemi

def greetings(isim="Kullanıcı",mesaj="Merhaba"):
    return f"{mesaj} {isim}"

#merhaab kullnıcı yazar
sonuc = greetings() #biz burada parametrelere değerlerini atadık fakat oldu ki mesaj yerine bir şey yazmadık veya isim yerine işte bu durumda program hata verir
#bu hatayı almak yerine def greetings(isim,mesaj ="merhaba"): yazmak demek eğer programa parametre verilemzse default bunu kullan hata atma demek ama eğer default da var ama biz parametre de gönderiyorsak gönderdiğimiz parametre default değeri ezer.

sonuc = greetings("berra","merhaba") #default değeri ezer ve Merhaba Berra yazar.
print(sonuc)

#us alma fonksiyonu yazalım

def usAlma(taban,us=2): #anlamı : us girilmediği takdirde otomatik 2 atasın ama eğer parametre gönderilirse 2'yi ezsin ve üs değerine göre işlemi yapsın
    return taban**us

print(usAlma(3))#2'ye göre alır üssü
print(usAlma(3,9))#2 olan üssü ezer ve 9'a göre üs alır

#def usAlma(taban,us=2): böyle bir durumda olur default son parametreye atanır eğer il parametreye atansa gelen değerin hangisine ait olduğunu program anlayamaz o yüzden son parametreye atamak gerekir