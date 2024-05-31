x =9
y=5

print(x+y)
print(x-y)
print(x*y)
print(x/y)#bölmeyi verir virgüllü
print(x//y)#bölmeyi verir virgülsüz
print(x%y) #bölmeden kalanı verir
print(x**y)#üs alır 9 üzeri 5

x = input("ilk sayıyı giriniz" )
y = input("ikinci sayıyı giriniz" )

print(int(x)+int(y)) #int'leri başına yazmazsak program ilk haliyle string algılar ve girilen sayıyı birleştirir

print(round(9.8)) #yuvarlama yapar
print(abs(-9)) # sayının 0'a olan uzaklığını verir.

import math #kütüphane dahil etme kodu

print(math.sqrt(25)) #karekök bulma

enKucuk= min(9, 10, 560)
print(enKucuk)

enBuyuk = max(999,70,60)
print(enBuyuk)


