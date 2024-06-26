#dongüler ve kullanım alanları

#FOR DONGUSU =NE ZAMAN BİR LİSTE ÜZERŞNDE İŞLEM YAPMAK İSTESEM FOR DONGUSU KULLANILIR
#WHILE DONGUSU =NE ZAMAN BİR KOŞULA GÖRE BİR DONGÜ KULLANMAK İSTERSEK WHILE DONGÜSÜ

#NOT =FOR DONGUSU BİR LİSTEYE İHTİYAÇ DUYAR

sayilar = [1,2,3,4,547,4536,8679,78,456,34,3,45,4567]

for i in sayilar: #sayilar listeindeki her bir elemanı geçici olarak i olarak adlandırdığıız geçici bir değişken içine kopyalar. neden i diye geçici değşken çğnkü hani biz bir şeyi kerana bastırırken onu bir değişkene atıyım print yapıyorsuz ya bunu defalarca yapmamak için bir değişkene atama döngüsü gibi düşün
    print(i) #her gezdiği elemanı ekrana printe eder

 #listenin kaç elemanlı olduğunu merak ediyorsak

for x in sayilar: #sayilar listesinin eleman sayısı kadar BTK akademi ekrana print edilir
     print("BTK Akademi")


isimler = ["Ayşe","Fatma","Hayriye","Umut"]

for isim in isimler: #isimler listesindeki elemanları isim adlı yeni oluşturulmuş değişkenin içine kopyalar print eder
    print(isim)

for isim in isimler: #isimleri tek tek gezip print ederken Naber ekleyerek print eder
    print(isim+" Naber ! ")


my_tuple= [(1,2),(3,4),(5,6)] #aslında bir liste ama listenin elemanları birer tuple'dır.

for a,b in my_tuple:  #yukarıdak, listenin elemanları birer tuple olduğu için listenin tuple elemanlarına böyle a,b isminde geçici değişken tanımlayıp içine gezdiği değerleri copy edebiliriz
    print(a,b)

my_dictionary = {"41":"Kocaeli",
                 "53":"Rize",
                 "35":"izmir"
                }
for keys in my_dictionary.keys(): # my_dictionary liste tipinin keys() metodu ile keys değerlerini alıp keys adlı değişkene kopyalayıp print ile kopyaladığımız değişkenin içindeki keys çağırıyoruz
    print(keys)

for values in my_dictionary.values(): # my_dictionary liste tipinin values() metodu ile value değerlerini alıp values adlı değişkene kopyalayıp print ile kopyaladığımız değişkenin içindeki values'ları çağırıyoruz
    print(values)

for x,y in my_dictionary.items(): #items metodu key valuları bir tuple'a dönüştürür
    print(x,y)
    print(type(x,y))