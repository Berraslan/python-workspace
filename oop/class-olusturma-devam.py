class Product:
    def __init__(self,name,price,isActive): #class'ın ilk methodu başlatıcı metod ya da Consturactor metod da denebilir bu yaptığımıza __init__ etiketi ile başlar ve self parametresini default alır aslında self parametreden ziyade nesneyi temsil eder
      self.name=name #self aslında p1'in isim alanını tutuyor yukarıdaki name ise parametre olarak alınıp p1.name'inin içine atanacak name'i kastediyor yani kullanıcı p1 nesnei için name bilgisi girince bu bilgi p1.name boş kabının name alanını dolduracak
      self.price= price
      self.isActive=isActive #Ürün satışta mı onu yazdıralım ve parametre olarak aldığımız bilgiyi nesen içinde isActive alanına atalım

    #instance metod denir
    def get_product(self):#bu normal bir metoddur ve nesne üzerinden iş yaptığı için bir self parametresi alır self demek nesnenin temslili demektir self yani nesne demektir metodda nesneyi temsil eder ve ona ulaşmayı mümkün kılar
        return f"ürün adı: {self.name} ürün fiyatı: {self.price} olan kdv'li fiyatı {self.kdv_calculator()} ürün stokta mevcuttur." #self bizim nesnemizi temsil ettiği için self.name aslında p1 veya p2 veya p3.name demektir

    #self ile nesnenin price'ına ulaşırız ve 1.20 ile çarparız return ile yapmamızın sebebi ise retun olunca kullanılabilirilik her yerde artıyor
    def kdv_calculator(self):
        return self.price*1.20


p1=Product("iPhone 11",19000,True)  #Product() class'ını p1 isimli nesnesi oluşturuldu artık p1 Product class'ı içindeki tüm method ve attributes erişimi vardır. name ve price parametrelerini alır ve p1 nesnseinin ilgili attributes kısımlarını doldurur
p2=Product("iPhone 15 Pro Max",80000,False)
p3=Product("iPhone 14 Pro ",70000,False)




products=[p1,p2,p3] #Product class'ının nesnelerini tutan liste tanımladık

for product in products:
    if product.isActive==True:
         print(product.get_product()) #get_product() metodu çağrılır get_product() metodu içine metod self.kdv_calculator() çağrılabilir







#
#
# sonuc=p1.name #p1 nesnesinin name attribute kısmı sonuc değikenine atandı ve print ile bastırıldı bazen neseninin değerlerini direk yazdırmayıp başka bir değişkene atarız ki yapacağımız değişiklikler nesne'yi etkilemesin
#
#
# print(sonuc)