#args(argümanlar) ile kargs(keyword args) arasındaki fark şudur ;
#args -tuple tipinde geri dönüş verir
#kwargs - dicitionary (key: value) tipinde dönüş verir.

def display_user(*args):
    print(type(args))
    print(args)  #girilen args değerlerini printler

display_user() #veri tipi args sayesinde tuple olur yani bize tuple değer döndürür

def display1_user(**kwargs):
    print(type(kwargs))
    print(kwargs) #girilen kargs değerelerini prinlter

display1_user() #veri tipi **kwargs ssayesinde dictionary olur yani bize dictionary değer döndürür

#burada değişken sayıda argümanı gönderebiliyoru fonksiyona args ve kwargs sayesinde sadece tek fark biri tuple olarak verileri paketliyor diğeri ise dictionary olarak key:value olarak verileri paketler.
display_user(10,20,30)

display1_user(username="berraAslan",email ="yazilim@gmail.com",logDate="10-05-2024",kullaniciYas=24) #burada **kwargs bir dictionary olduğu için bizden key:value değeri alır ve usernamein karşılığı string tanımlandığı için "" içine almaya gerek yoktur

#daha otonom bir hale getirmek için

def display1_user(**kwargs):
    for key,value in kwargs.items(): #kwargs dicitonary listesini items() metodu sayesinde normal listeye çevirdik ve verilen her key value'yi key value değişkenleri içine ekleyip f string kullanarak ekran printledik
        print(f"{key}-{value}") #bu yapı daha güzel görseli olsun diye yapıldı


display1_user(username="berra",yas=23) #buraya istediğimiz kadar argümanı ekleyebiliriz daha sonra da gelip ekleyebiliriz