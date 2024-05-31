kursAdi = "Btk Akademi ile Python Programlama Dersleri Çalışma Programı"
webSite ="https://www.btkakademi.gov.tr/"

deneme =' Btk Akademi '.strip()#böyle sadece istenen kısım da eklenip strip yaılabiliri ille de değişken adı yapmaya gerke yok


print(deneme)

deneme2 = kursAdi.lower()
print(deneme2)

deneme3 = kursAdi.count('a') #kursAdi değişkeni içerisinde kaç adet B var onu döner
print(type(deneme3))


sonuc=webSite.startswith('https') #webSite değişkeni https ile mi başlıyor bunu sorgular
print(sonuc)

sonuc1=webSite.endswith('tr')
print(sonuc1)

sonuc2=kursAdi.isalpha() #kurs adı değişkeninin içinde sağladığı değerin tamamı alpahabetic mi sorgusu dur yani içinde ssayı veya boşluk içeriyor mu ?
print(sonuc2)

sonuc3=kursAdi.replace(' ','-').replace('Ç','C').lower() #tüm boşukları - ile değiştir.dikkat eğer '' bitişik yaparsan her harfin araına koyar b-t-k gibi
print(sonuc3)

sonuc4=kursAdi.replace('Python','ReactJS')
print(sonuc4)

#not: find() ve index() string metodları neerdeyse aynıdır ikisde metinde kelime veya karakter arar ama find() bulamzsa -1 döndürür.index() hata objesi atar

sonu5=kursAdi.find('x')
print(sonu5) #-1 döndürdü

#sonuc6=kursAdi.index('x')
#print(sonuc6)#thrown an error (hata fırlattı)


sonuc7=kursAdi.split()#split() metodu ile cümleyi listeye çevirdik
print(sonuc7[2])#liste halinin 2.elemanını bastırdık

