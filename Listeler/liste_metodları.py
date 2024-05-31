numbers= [4,6,45,43,23,23,23,23,54,76,7]
isimler= ["büşra","ayşe","fatma","hayriye","çiçeksu"]
# minBulListeden= min(numbers) #min metodu default gelen pyhton class'ları sayesinde min() metdounu kullanımımıza sunar
# print(minBulListeden)
#
# #liste'ye yeni eleman ekleme metodu append()
#
# numbers.append(12) #append() listenin sonuna eleman ekler
#
#
# #insert() metodu istediğin konuma eleman eklemek için kullanılır
# numbers.insert(0,100) #0.indise 100 sayısnı ekle demek
#
# numbers.insert(-1,8)#listede en sona eleman eklemesini bekleriz ama sondan bir önceye ekler
#
# numbers.insert(len(numbers),8)# işte asıl bu listenin en sonuna gider ve ekler
# print(numbers)
#
# # #eleman silme pop() metodu indis numarasına göre siler. (index numarası vermezsek sondaki number otomatik silinir)
# #
# # numbers.pop()
# # print(numbers)
# #
# # numbers.pop(0)
# # print(numbers)#0.indis 100 değeri silinir
#
# #silme işlemini listedeki elemanı direk verekerk silme remove() value göre siler
# isimler.remove("çiçeksu") #çiçeksu ismini siler
# print(isimler)
#
#
# #sıralama metodu sort() -> isimse alfabetik sıralar, sayı ise küçükten büyüğe sıralar.
# numbers.sort()
# print(numbers) # MİN --> MAX
#
# isimler.sort()
# print(isimler) # A --> Z
#
# #TERSTEN SIRALMAK İÇİN reverse() metodu
#
# numbers.reverse()
# print(numbers) #max--> min
#
# isimler.reverse()
# print(isimler) # Z --> A
#
# # count metodu bir listede bir eleman ne kadar tekrarlandıysa bunun sayısını gösterir
# neKadarVar=numbers.count(23) #23 değeri listede kaç adet var onu döndürür
# print(neKadarVar)
#
#
# #index metodu listede aranan değerin hangi indiste bulundupu bilgisini döndürür

hayriyeNerede=isimler.index("hayriye")
print("Hayriye ismi "+ str(hayriyeNerede) +"'de")