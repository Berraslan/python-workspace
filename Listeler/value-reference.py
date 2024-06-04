#value types :  değiken sadece o değeri int'se int string'se string'i tutar

x= 10
y=20


x=y # y'nin 20 değeri artık x'e de kopyalandı

y=30 # y'nin içeriğini 30 yapınca sistem değer tuttuğu için x'de değişiklik olmaz

print(x,y)

#reference tip : list gibi veri tipleri referans tiplidir referans tip ise değer yerine atanan değişkenin bellekteki adresini tutuar yani eğer atanan değerde bir değişiklik olursa atama yapılan değikende de aynı değişiklik görülür artık
# a =b olduğunda referans tipde normalde a farklı bir bellek adresini b FARKLI BİR BELLEK ADRESİNİ TUTUYORDU AMA ARTIK İKİ Sİ DE B'NİN BELLEK ADRESİNİ TUTUYOR YANİ BU ŞU DEMEK A 'DA VEYA B'DE BİR GÜNCELLLEME OLDUĞU ZAMAN İKİSİ DE AYNI SONUÇTAN ETKİLENECEKTİR


A= ["ELMA","ARMUT"]
B=["pORTAKAL","ÇİLEK"]

A=B # B İÇİNDEKİ DEĞERLER BELLEK ADRESİ OLARAK A'YA ATANDI BUDA ŞU DEMEK ARTIK B'DEKİ HER GÜNCELLEME A'YI ETKLİLER AYNI ŞEKİLDE A'DAKİ DEĞİŞİKLİKLER DE ETKİLER B'Yİ

A[0] = "kIRMIZI"
print(B) #A'nın 0.indisine atanan kIrmızı değeri aynı bellek adresini gösterdiği için B'nin 0.indisini de etkiler


#liste kopyalama : normalde referans tip olan veri yapılarını aslında copy() metodu ile value type haline çevirdik. yani bu şu demek

listA = [10,20]
listB = listA.copy() #bu copy metodu sayesinde listA B içine atanınca bellekte farklı bir yere A'nın listesini saklıyor ve bundan sonra B üzerinde olan hiçbir değişiklik A'yı etkilemiyor

listB[0] = 30
print(listA,listB)






















