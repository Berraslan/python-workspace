#Eğer başka bir modlude olan bilgileri farklı bir modul içinde kullanmak istersek import modulAdi YAZARIZ
#modul == dosya adı ya da .py uzantılı olan hepsi aslında bir module'dür.


import modul

sonuc = modul.sayi #farklı moduldeki değişkene fonksiyona erişmek için o modlulun adı verilir . denir ve erişilmek istenen değer,fonksiyon,obje ne ise o yazılır
sonuc =modul.urun["urunAdi"] #urun dictionary içinden ürünAdi geldi
sonuc =modul.sayilar


print(modul.toplama(a=8,b=8)) #farklı bir modludeki fonksiyona yine o dosyanın adı ve . diyerek erişiriz


"""Not : modül ismi uzun olduğu zaman modüle takma isim (alias) verilir ki kod dah atemiz ve açık dursun
örneğin : import module as m (anlamı modulu main içinde m olarak çağır)
"""

import modul as m #m burada takma isim (alias)

sonuc = m.sayilar

print(sonuc) #modul isimindeki modulden sayi değişkenine erişitik

"""veya m veya modul diye eklemek istemiyosan farklı sayfadaki fonksiyon,değişken vs. o zaman

from module import sayi,sayilar,urun (sadece kullncaklarını belirtip import edebilirsin)
böyle from kullanarak eklersen m. veya modul. diye sayfa ismi vermene gerek kalmaz

"""

from modul import sayi,sayilar,urun

sonuc =sayi #modul.py içindeki sayi değişkeninin içindeki değeri sonuc içinde atar. from olan kullanımda m.sayi veya module.sayi demeye gerek yok direk sayi değişkeni burada kullanılır

print(sonuc)


"""Modul dosyası olamadan diğer dosyadaki yapılara erişmek için
from module import * dersek tüm yapılara erişiriz

"""
from modul import *

sonuc =sayi #böyle direk tanımlayabiliriz

toplama=toplama(7,9)
print(toplama)
