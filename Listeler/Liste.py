kurum = ['BTK','akademi']

print(kurum[-1])

print(type(kurum))


#split metodu'da list yapar

kurum1="BTK Akademi"

sonuc=kurum1.split()#önceden kurum1 strind idi ama artık split ile list oldu
print(type(sonuc))

list= [1,2,3,4,'Ayşe']
print(type(list[4])) #liste'nin 4.elemanının tipi str
print(type(list[1]))#liste'nin 1.elemanının tipi int


ogrenciler= [["Çınar","Turan",60,70,50],["Ali","Turan",90,100,80]]
print(ogrenciler[0][2])  #ögrenciler listesinde 0.elemanın içindeki 2.eleman yani 60 notuna karşılık gelir

ogrenci1=ogrenciler[0][3]

ogrenci2=ogrenciler[1][4]

toplam=ogrenci2+ogrenci1 #ogrenciler listenisnde 0.elemanın içndeki 3.indis yani 60   ve ogrenciler 1.elamının içindeki 4.indise karşılık gelen 100 toplanır
print(toplam)

print(type(ogrenciler[0][3])) #öğrenciler listeninde 0.elemanın içindeki listenin içindeki 3.indisin tipini


sayi1= int(input("Sayı gininiz : "))
sayi2= int(input("Sayı gininiz : "))
sayi3 = int(input("Sayı gininiz :"))
toplam = sayi1+sayi2+sayi3
ortalama = toplam/3

print(f"1.sayı : {sayi1} -  2.sayı: {sayi2} ve -  3.say: {sayi3} -  toplam : {toplam} ortalama: {ortalama} 'dır. ")