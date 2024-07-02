#Not Uygulaması

#1-Menü
   #1-Not Gir
   #2-Ortalamaları Göster (90-100 -> AA, 85-89 -> BA)
   #3-NotlarI kaydet
   #4-Çıkış

"""
90-100 -> AA
80-89  -> BA
75-79  -> BB
70-74  -> CB
65-69  -> CC
60-64  -> DC
50-59  -> DD
40-49  -> FD
0-39   -> FF

"""

def not_Gir():
    ad = input("Adınızı giriniz : ")
    soyad = input("Soyadınızı giriniz : ")
    not1 = input("not 1 : ")
    not2 = input("not 2 : ")
    not3 = input("not 3 : ")
    #Girilen notarı ve isim bilgisini sinav_notlari.txt içine yazar.
    with open("sinav_notlari.txt","a",encoding="utf-8") as file: # a modu eğer böyle bir dosya yoksa kendi açar.eklenen yenilikler dosyanın sonuna eklenecektir
        file.write(ad+' '+soyad+':'+ not1+','+not2+','+not3+'\n')# + ile stringeleri tek bir yerde birleşitirebiliyoruz ve başka bir öğrenci girilmesine geçileceği zaman \n ile bir alt satıra geçiyoruz.



def not_hesapla(satir): #satir değikenini burada kullanabilri artık bu fonksiyona parametre olarak atadığımız zaman
    satir = satir[:-1] #-1'e kadar hespsini oku demeketir bu da iki satır arasına \n ile konulan n'i kaldırır ve aradaki boşluğu kaldırır yani \n okumaz
    liste = satir.split(":") # bu demek oluyor ki : 'nın geçtiği yerden itibaren böl elemanı demek ikiye ayır demek yani ad soyad : notlar olarak ayıracak

    ogrenciAdi= liste[0]
    notlar= liste[1].split(",")#notları da kendi içinde , olan yerden itibaren ayırıyoruz not1 not2 not3 diye de notları split edecek

    not1 = int(notlar[0]) #notlar listesinin 0.indisi not1'e karşılık gelir hesaplamada kullanılacağı için int'e dönüşüm yapmak gerekir
    not2 = int(notlar[1]) #notlar listesinin 1.insisi not2'ye karşılık gelir
    not3 = int(notlar[2]) #notlar listeisinin 2.indisi not3'e karşılık gelir

    ortalama= (not1+not2+not3)/3

    if ortalama >=90 and ortalama<=100:
        harf ="AA"
    elif ortalama >=80 and ortalama<=89:
        harf ="BA"
    elif ortalama >=75 and ortalama<=79:
        harf ="BB"
    elif ortalama >=70 and ortalama<=74:
        harf ="CB"
    elif ortalama >=65 and ortalama<=69:
        harf ="CC"
    elif ortalama >=60 and ortalama<=64:
        harf ="DC"
    elif ortalama >=50 and ortalama<=59:
        harf ="DD"
    elif ortalama >=40 and ortalama<=49:
        harf ="FD"
    elif ortalama >=0 and ortalama<=39:
        harf ="FF"

    return f"{ogrenciAdi} : {harf}-({ortalama})\n" #her if içine print dmek çok otonom bişey değil return içinde yazdırırsak bu dönüşü her yerde effective bir şekilde kullanabiliriz
def notlari_Oku() :
    with open("sinav_notlari.txt","r",encoding="utf-8") as file:
        for satir in file:#her satır bir öğrenciyi temsil ediyor satırları tek tek gezebiliriz for ile
            print(not_hesapla(satir))#satirin anlık tutuğu değerleri sırayla  for ile gezer ve not_hesapla fonksiyonu satır değişkenini alır ve her satırdaki not bilgisi için not ortalaması hesaplar


def notlari_Kaydet():
    with open("sinav_notlari.txt","r",encoding="utf-8") as file:
        liste=[] #sinav_notlari.txt içerisinden okunan tüm veriler bu listenin içerisine yazılacak
        for satir in file:#her bir satir file üzerinden okunacak file aslında sinav_notlari.txt'yi tutan değişkenimiz aslında yani biz txt2mizden tek tek satıralrı okucaz
            liste.append(not_hesapla(satir)) #her okuduğumuz satiri not hesapla fonkisyonunu çağırıp o formatta satie bilgisine göre listeye eklicez aslında back up almış olacağız

    with open("sonuclar.txt","w",encoding="utf-8") as file2:
        file2.writelines(liste)
        print("Notlar sonuclar.txt dosyasına kayıt edildi.")
        #okunan ve hazıralan liste elemanlarını file2 diye sonuclar.txt dosyasını tutan referans aracılığı ile içine yazdık liste
        # içindeki bilgileri yani bilgiler hem sınav_sonucları hem de sonuclar.txt içinde ayrı ayrı tutuluyor file 2 olarak açmamın sebebi sınav_notlari.txt adlı dosyayı file referas olarak tutuyor
        #file2'de artık sonuclar.txt adlı txt dosyasını referans olarak tutuyor eğer ikisine de aynı file ismini verseydik en son gelen txt diğerini ezerdi.






#While kullanımamızın sebebi true oldukça sürekli bize devam eden menü döndürecek ta ki break olana yada çıkış tuşlaması yapılana kadar
while True:
    islem=input("1-Not Gir\n2-Notları Oku\n3-Notları Kaydet\n4-Çıkış\nLütfen Tuşlama yapınız : ")

    if islem =="1":
        not_Gir()
    elif islem=="2":
        notlari_Oku()
    elif islem== "3":
        notlari_Kaydet()
    elif islem=="4":
        break
