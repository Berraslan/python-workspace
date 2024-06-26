#soru1

sayilar = [3,5,7,2,12,32,45]
#
# # for x  in sayilar: #sayılar listesindeki tüm elemanları print eder.
# #     print(x)
#
# #soru2
#
# for sayi in sayilar : #sayilar listeindeki tüm elemanları sayi değişkenine atar
#     if (sayi % 3==0) : #sayi değişkenine atılan sayilar içinden 3'e tam bölünen sayılar eğer varsa sayi değişkenine at
#         print(str(sayi)+" sayi 3'ün katıdır.") #sayi değişkenine atılan 3'e bölünen değerleri printle


#soru3

# toplam= 0 #boş bir kap tanımladık aslında
#
# for sayi in sayilar: #sayilar listesindeki elemanlara eriştik
#     toplam += sayi #eriştiğimiz elemanları sayi adlı değişkene atadık ve toplam adını verdiğimiz değişken içine atıp her gelen sayi değeri ile toplamı print'e yazdırırız
# print(toplam) #eğer print'i bir sol yani şu anki konumuna kaydırırsak en son toplamı verir for içinden çıkar ama for içine bir adım sağa kaydırırsak her toplam ve sonucunu gösterir
#             #eğer kaydırmazsak ve içeride kalırsa her seferinde for çalıştıkça toplamı gösterir ama biz nihai (ulitmate) sonucu istiyoruz zaman bu şekilde for dışında kalıcak vesadce bir kere nihai sonucu yazıcak

#soru4 listedeki tüm ürünleri printler
urunler =["samsung","iphone 13 ","iphone 15 ", "iphone ", "samsung", "samsung"]
#
# for urun in urunler: #bu kod satırı sayesinde listede tüm elemanlara erişim sağlamış oluruz
#     print(urun)

#soru5 ürünler listesindeki tüm iphone markalarını listele (find ve index metodları listelerde arama için kullanılan metodlardır)
#find() ve index() metodu aynı mı ? HAYIR çünkü index metdodu eğer aradığınız elemanı bulamazsa 'substirng not found ' hatası verir
#
# for urun in urunler:
#     print(urun.index("iphone"))
#find metodu ise aranan elemanı buluyorsa o elemanın indisini döndürür eğer bulamadıysa -1 döndürür

# for urun in urunler: #kodun açıklaması : URUNLER LİSTESİNDEN URUN ADLI elemanları sırayla gezerken tutulacağı boş değişkendir daha sonra find metodunun döndürüdüğü değerler i,ndex değişkenine atıyıp -1 den büyük olan ürünleri print ile ekrana yazdırdık
#     index = (urun.find("iphone"))
#     if index > -1:
#         print(urun)


#soru 5

amount = 0;
for urun in urunler:
    index = (urun.find("samsung"))
    if index > -1:
        countOfUrun = urun.count("samsung")
        amount += countOfUrun
print(amount) #printi dışarı yazdım çünkü her seferinde çalışma'nın totoalini değil nihai totali görmek istiyoruz




