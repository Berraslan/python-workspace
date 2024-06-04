brand = ["Bmw", "Renault", "Mercedes"]

print(len(brand)) #liste'nin eleman sayısını verir

print(brand[0]) #listenin 1.elemanını bastırır
print(brand[-1]) #listenin sondan 1.elemanını bastırır

brand[1] = "Togg"  #renault markasını togg ile değiştirdik
sonuc=brand




sonuc = "Togg" in brand #togg brand listesinin içinde var mı sorugusu yapar TRUE veya FALSE döndürür
print(sonuc)

#Listenin ilk iki elemanını alma
sonuc= brand[0:2]
print(sonuc)

#listenin sonuna ford ve citroen ekleme
sonuc= brand +["Ford","Citroen"] #bu eklenen elamanlar sonuc değişkeni içerisinde eklendi ana listeye değil ana liste hala 3 elemanlı
print(sonuc)
print(len(sonuc))
print(len(brand))


#analistenin son elemanını silme

del brand[-1]
print(brand)


#aşağıdaki verileri liste içinde saklayınız

#öğrenci1: Yiğit Bilgi 2010 [70,80,90]
#öğrenci2: Ada Bilgi 2012 [70,70,80]
#öğrenci3: Çınar Turan 2017 [60,60,90]

ogrenci1 = ["Yiğit","Bilgili",2010,[70,80,90,100]] #bu bir iç içe listedir yiğit [0], bilgili [1], 2010 [2], [70,80,90] not bilgisi ise [3].elemandır notlar içinde gezmek için ogrenci1[3][0]'demek gerekir bu bizi 3.elemanın 1.elemanına götürür yani 80
ogrenci2 = ["Ada","Bilgili",2012,[70,70,80]]
ogrenci3= ["çınar","turan",2017,[60,60,90]]

dersSayısıOgrenenci1=len(ogrenci1[3][0:4])
dersSayısıOgrenenci2=len(ogrenci1[3][0:3])
dersSayısıOgrenenci3=len(ogrenci1[3][0:3])

tumOgrenciler =[ogrenci1,ogrenci2,ogrenci3]
ogrenciSayısı = len(tumOgrenciler)


#ogrenci1 yas hesaplama
ogrenci1Yas= 2024-ogrenci1[2]
ogrenci2Yas= 2024-ogrenci2[2]
ogrenci3Yas= 2024-ogrenci3[2]


print("bu Yiğitin yaşıdır: "+str(ogrenci1Yas))
print("bu adanın yaşıdır: "+str(ogrenci2Yas))
print("bu çınarın yaşıdır: "+str(ogrenci3Yas))

#öğewncilere ait not ortalaması
ogrenci1NotOrt= (ogrenci1[3][0]+ogrenci1[3][1]+ogrenci1[3][2]+ogrenci1[3][3])/dersSayısıOgrenenci1
ogrenci2NotOrt= (ogrenci1[3][0]+ogrenci1[3][1]+ogrenci1[3][2])/dersSayısıOgrenenci2
ogrenci3NotOrt= (ogrenci1[3][0]+ogrenci1[3][1]+ogrenci1[3][2])/dersSayısıOgrenenci3

print(f"{ogrenci1[0]} isimli öğrenci {ogrenci1Yas} yaşındadır. NOT BİLGİSİ : {ogrenci1[3][0:3]} ayrıca {ogrenci1[0]}'ın not ortlaması : {ogrenci1NotOrt}")
print(f"{ogrenci2[0]} isimli öğrenci {ogrenci2Yas} yaşındadır. NOT BİLGİSİ : {ogrenci2[3][0:3]} ayrıca {ogrenci1[0]}'ın not ortlaması : {ogrenci2NotOrt}")
print(f"{ogrenci3[0]} isimli öğrenci {ogrenci3Yas} yaşındadır. NOT BİLGİSİ : {ogrenci3[3][0:3]} ayrıca {ogrenci1[0]}'ın not ortlaması : {ogrenci3NotOrt}")

#ogrencilerin ortalama yası
ogrenciYasOrt = (ogrenci1Yas+ogrenci2Yas+ogrenci3Yas)/ogrenciSayısı
print(ogrenciYasOrt)

#öğrencilerin not ortalamaları

