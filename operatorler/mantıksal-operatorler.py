#mantıksal operatorler

#and her koşul true olmalı
#or sadece bir koşul bile doğru olsa true döner
#not sonucun tersini alır not(x>5 and x<10)

#AND
x =11

sonuc= (x>5) and (x<10) # x=11 ise sonuc 'false' döner
print(sonuc)

#or
y=8

sonuc1= (y>5) or (y<7)
print(sonuc1) #true döner çünkü en az bir tane true var


#not operator
z=9
sonuc2 = not((z>0) and (z!=10)) #burada iki durumda da parantez içi true olduğu için not'lanır ve true olan değer false olarak sonuc2 içine kaydedilir ve print edilir
print(sonuc2) #false


