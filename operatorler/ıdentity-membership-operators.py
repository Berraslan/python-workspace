# is ; is not ; in ; not in operatorleri

# is operatörü : nesne benzerliğini kontrol eder   ; x is y
# is not operatörü : nesne benzerlik kontrolü yapar ; x is not y
# in : listede varlık kontrolü yapar ; x in y
# Not in : listede varlık kontrolü yapar ; x not in y


#identity operatorleri

#burada x ve y her ne kadar da içerisindeki değerler aynı görünse de asslında farklı bellek alanlarında saklanan farklı nesnelerdir
x = [2,4,6]
y =[2,4,6]

z=y

print (x==y) #elemanların birbirine benzer mi olduğu sorgusu atılır (true döner)
print(x is y) # burada x ve y aynı eleman ları mı temsil eder sorgusu atılır yani x'in tuttuğu liste aslında y'nin tuttuğu referans ile aynı mı hayır false döner çünkü x ve y farklı bellek adreslerinde tutuluyor

print(y is z) #burası true döner çünkü y listesinin referans tuttuğu değer olduğu gibi z ile aynıdır ona copy yapılmamıştır direk referansı atanmıştır yani z ve y aslında aynı elemanları tutar


#membership
print (2 in x) #sorgunun anlamı 2 x listesinde var mı
print(6 not in y) #y listesinin içinde 6 yok mu sorgusudur bu da False döner