a, b ,c  = 4 ,8, (12 ,2)
# #soru1
sayi1 =  int(input("  Sayı giriniz : "))
sayi2 =  int(input("  Sayı giriniz : "))

carpim = sayi1*sayi2

toplam = a+b+c[0]+c[1]

soru1Cevap = carpim-toplam
print(soru1Cevap)

#soru2 kalansız bölme işlem // ile yapılır
sonuc = (c[0]+c[1]) // b  #c bir tuple olduğu için indisleri toplayıp sonucu bölüyoruz
print(sonuc)


#soru3 a,b,c toplamının mod 7'si nedir?
allToplam = (a+ b + (c[0]+c[1])) % 7
print(allToplam)

#soru4 b'ni a.kuvveti
us = b**a
print(us)

#soru5 a,b,*c
