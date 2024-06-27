#enumaerate metodu ve zip metodları
#not : eğer zip ve enumarate metodlarını for haricinde kullanıyorsak mutlaka list veri tipine çevirmeliyiz for'da kendi otomatik yapıyor.
from typing import List

brands = ["opel","bmw","togg"]


index = 1

for brand in brands:
    print(f"{index},{brand}")
    index +=1

#enumarate bize listedeki elemamları indexleme işinde yarar yukarıdakş gördüğünüz kodun çalışma mantığında ama tek metodla bu işi kolayca yapabiliyoruz

obj1 =enumerate(brands,1) #burada brands listesini enumarate metodu kullanarak indexledik fakat daha sonrasında bunun tipi enumarate olduğu için list veri tipine çevirmemiz gerek
#enumarate defult olarak indekslemeye 0'dan başlar ,koyup başlamasını istediğiniz sayıyı yazabilirsiniz
print(type(obj1))
print(list(obj1)) #list veri tipine çevirdik


#enumarate metodunu for ile kullanma

for index,marka in enumerate(brands,1):
    print(f"{index}-{marka}")


#zip metodu kullanımı
#elimizde birden fazla liste varsa bu listeleri birleştirmeye yarar

numara = [100,200,300]
ogrenci =["Ali","Ayşe","Fatma"]

print(list(zip(numara,ogrenci))) #100-ali, 200-ayşe , 300 -fatma , yı list veri tipine çevirip printledik


#yukarıdaki işlemin aynısını for ile kullanımı

for no,isim in zip(numara,ogrenci):
    print(no,isim)

