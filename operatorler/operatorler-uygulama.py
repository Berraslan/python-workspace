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

#soru5 a,*b,c = (2,4,6,8,13) işlemine göre c'nin küpü nedir?

a,*b,c = (2,4,6,8,13) # *'ın anlamı şudur a = 2 , b= 4,6,8 c =13 'u kapsar demektir yıldız ortadaki 4,6,8 yapısnı liste olarak alır
print(c)


#soru6 a,b,*c = (2,4,6,8,13) işlemine göre c'nin değerler toplamı nedir?
#a = 2 ,b =4 c= 6,8,13 'dür ve c bir liste olur ve indis numaraları ile erişilir
a,b,*c = (2,4,6,8,13)
print(c[0]+c[1]+c[2])
