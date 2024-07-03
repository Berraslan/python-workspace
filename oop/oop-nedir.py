"""
OOP - Object Orianted Programming = Nesne Odaklı Programlama

Nesne tabanlı programlamanın mantığında CLASS kavramı var

Şöyle düşünelim mesela bir değişken oluşturdunuz ve bunu liste olarak ayarladınız aslında bu arka planda şu demek bu programlama dilinin liste adında bir class'ı var ve bu liste class'ının
içinde barınan onun yapaildiği metodlar ve kabiliyetler tanımlı mesela biz liste1 değişkenine liste1.append() diyip listeye eleman ekliyoruz aslında liste1 liste class'ının bir
instance veya object veya nesne veya örnek denir ve bu sayede bizim liste1 değişkenimiz liste sınıfının içinde barındırdığı özelliklere erişim ve kullanım hakkına sahip oluyor bu metodlar çok fazla örnek
.append(),.sort() vs...
aslında biz liste1 isimli değişkenle çalışırken liste class'ının bir örneğini aldık yani taklitler aslını yaşatıyor diyebiliriz.

Bir class içinde proporties(özellikler) aslında proporties dediğimiz içinin doldurlumasını beklenen boş değişkenler ama değişkenlerden daha yetenekli o yüzden proporties denir ve metodlar(iş yapan) bulunaabilir

Bir sınıfı kullandğımız zaman aslında onun bir örneğini oluşturuyoruz



"""

list1=[1,2,3]
list2=[1,2,3,4]

tip = list1

print(type(tip))