# #sets'ler indekslenmez yani indeks numarası ile verilere erişilmez bu özellikle depolamadan kar elde edilir
# #sıralanamaz (not order_by) : elemanlar sıralanamazlar
# #güncellenemezler : zeten elemanlara erişemediğimiz için 1. kuraldaki sebepten ötürü bu sebeple de o elemanları güncelleyemeyiz
# #elemanlar tekrarlanamazalar listede bir tane APPLE İSMİ VARSA BİR DAHA APPLE EKLERSEN YİNE 1 TANE APPLE GÖRÜRÜSÜN
# #yeni eleman eklenebilir veya silinebilir ama GÜNCELLENEMEZ.
# #elelmanlar her çalıştıırlmada farklı sırlama ile gelir
#
#
# #NOT: LİSTE TANIMLAMA ->  variableName =[.... , .... , .... ]
# #NOT: TUPLE TANIMLAMA ->  variableName =(.... , .... , .... )
# #NOT: DICTIONARY TANIMLAMA ->  variableName ={"...": ....  ,  KEY : VALUE
# #                                             "....": .... ,
# #                                             "....": .... ,
# #                                             }
#
# #NOT: SETS TANIMLAMA ->  variableName ={.... , .... , .... }
#
#
# fruits = {"apple", "pear", "cheery", "apple", True, False, 5}
#
# sonuc = fruits  # fruits sets-list yapısını sonuc adlı değişkene atadık ama fruits ismi debaşlı başına bir değişken sadece yapıla değişiklikler ana listeyi etkilemesin diye yeni bir varriable oluşturulur
#
# print(sonuc)
#
# #bir elemanın liste de olup olmadığını kontrol etmek için
#
# varMiListeDe = 5 in fruits  # bool bir sonuç verir true or false
# print(varMiListeDe)
#
# # PEKİ INDEKSLEME YAPMIYORSA BİZ ELEMEANLARA NASIL ERİŞİCEZ -> FOR ile
#
# for x in fruits:  #burada yapılan işlem tanımlanan x değeri sayesinde listenin içi gelilir ve ekrana print edilir
#     print(x)
#
# #nasıl eleman eklenir .add() metodu ile
#
# fruits.add(9)
# listNewAdding = fruits
# print(listNewAdding)
#
#
# #iki listeyi birleştirme update() metodu ile olur ve dikkat et eğer bir listedeolan eleman öbürnünde de varsa tekrarlanan eklenmez
# #set ,tuple , dictionary birer listedir

ogrencilerA = {"AYŞE","FATMA","HAYRİYE","MUSTAFA","KEMAL","BERK","TAMER"}
ogrencilerB = {"SELİN","NAZLI","PELİN","ALİ","AHMET","TAMER","TAMER"}

sonuc= ogrencilerA.update(ogrencilerB) #ogrencilerA Listesi ogrencilerB listesi ile birleştirilir ama update() metodu değer döndüren bir metod olmadığı için eğer print içine sonuc yazdırırsan
#none döner çünkü update() birleştirme işlemini yapar ve geri çekilir sen değişikliği ogrencilerA listesini printleyi görebilisin
#normalde sonuc= ogrencilerA.update(ogrencilerB) yapısında sonucun sonuc değişkenine atanmasına gerek yoktur ama update() metodunun none döndürdüğünü gör diye
print(ogrencilerB)

#listeden eleman silme metodu remove()

ogrencilerA.remove("AYŞE") #listeden AYŞE ismini siler
print()









