# file = open("log.txt",encoding="utf-8")
#
# print(file.read())
#
# file.close() #okuma işlemi b,tince dosyayı kapat ki obj iş bitince bellekten silinsin yoksa boş yere yer kaplar

"""Yukarıdaki kod normalde open() metodu ile yapılan okuma işlemidir ve mutlaka sonda close() etmeliyiz

ama bu işin with ile kolay yolu var with open("dosya_Adi.txt",encoding="utf-8") dediğimiz zaman close() etmemize gerek kalmıyor dosyayı bellekte çünkü with metodu otomatik kapatıyor ve
ama burada şunu  bilmek lazım bu metodlar geriye değer döndürdüğü için bir değişkene atanması gerekiyor bu yüzden bir
with open("dosya_Adi.txt",encoding="utf-8") as file demek gerekiyor. as file mantığı aynı yularıdaki kodda file = open("log.txt",encoding="utf-8") file değiknine atadık ya aynısısır file
değişkeni üzeridnen dosya üzerinden kullanabileceiğim metodalara ulaşırız file bir değişken adıdır istediğin adı verebilirsin"""

"""with open("log.txt",encoding="utf-8") as file:
    print(file.read(10)) #10 byte oku demek 0.indisten 0 diye saymaya başlar eğer okuyacağı indis sayısını belirtmezsek dosyanın sonua kadar okur
    print(file.tell()) #crusor'un durduğu konumu dönüdürür
    print(file.seek(0)) #seek ile en başa getirdik
    print(file.tell())#şimdi artık 0 gösterir bulunduğu konumu"""

"""with open("log.txt",encoding="utf-8") as f: #normalde okuma modu ,r, ile belirtilmeli ama r defult geldiği için eklemye gerek yok eğer farklı bir erişim yapsaydık belirtmek durumunda kalırdık
    for i in f:
        print(i,end="") #f içindeki text tek tek i ile gezlilir ve yazdırılır end="" koyarsak aradaki boşlukları kaldırır satır atlamaz"""



"""bilindiği üzere hata aldığımızda hata mesajını anlamak bazen karmaşık olabiliyor ama try ve except yapısı kullanılarak asıl çalışan kod bloğunu try içine koyarız vve sonra da olası 
karşılaşacak problemleri except içine yazarsız ve excepte özel print yazarız ve hata objesi oluşunca otomatik olarak except içine girer ve excpet kısmı veyazdığımız açıklama terminalde görünür"""

#konuya örnek

try :
    with open("log2.txt",encoding="utf-8") as file:
        for i in file:
            print(i,end="")
#except içine program çalışırken karşılaşılması muhtemel hatalar ve açıklamaları yazılır veya uygulama geliştirici olarak gelen hataları loglayabiliriz
#FileNotFoundError dosya bulunamayınca alınır ve biz bu hataya açıklama ekledik eğer bu hatayı alırsa aşağıdaki except print kısmına girecek program
except FileNotFoundError as e: # as e burada hatayı e değişkenine atadık ve alt satırlarla hata üzreinden işlem yapcaksak e. diğerek erişebiliriz kullanılabilecek metodlara
    print("dosya okuma hatası")












