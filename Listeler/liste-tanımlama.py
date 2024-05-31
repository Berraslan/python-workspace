programlama_dilleri= ["python","c#","java","javascript"]


sonuc= programlama_dilleri
sonuc= type(programlama_dilleri)
print(sonuc)

sonuc = programlama_dilleri[0:2]#0.indisten başlar 2.indise kadar ama ikinci indis dahil değildir
sonuc = programlama_dilleri[-1]#sondaki ilk indisi alır
print(sonuc)

#update yapma listede

programlama_dilleri[-1] ="PHP"

print(programlama_dilleri[-1])

print(len(programlama_dilleri)) #len() metodu ile listenin eleman sayısı döner

#liste concrate
sonuc3=programlama_dilleri+["go","delphi"] #programlama_dilleri listesine yeni iki eleman ekledik aslında mantıken iki listeyi topladık
print(sonuc3)

print(len(sonuc3))



#listelerde koşula bağlı arama
sonuc4= "python" in programlama_dilleri #aynı ingilizce gibi düşün programlama_dilleri listesi içinde "python" stringi var mı sorgusudur.
sonuc5="go" in programlama_dilleri #bunu false döner çünkü go dilii biz ana listeye değil sonuc3 adli bir değişkene ekleyip atadık ana listede güncellemedik o yüzden false bu durumda ana listeye eklersek ancak görebiliriz
arama= "go" in sonuc3 #buna true döner çünkü "go" dilini programlama_dilleri listesi il bu değişken içinde birlerşitirdik
print(arama)


#listelerde döngü kurma

for i  in programlama_dilleri: #progamlama_dilleri listesi içinde i ile geziyoruz i bizim dillerimizi tek tek kopyalayım gezen değişkenimiz
    print(i)


#liste'den eleman silme del() metodu ile olur

del programlama_dilleri[1] #programlama dilleri listesi içinden 1.indiste bulunan elamanı silecektir.Yani C# silinir.
print(programlama_dilleri)