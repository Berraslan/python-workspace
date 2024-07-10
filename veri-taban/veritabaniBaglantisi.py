import sqlite3

#alttaki satırın açıklaması sqlite3 modülü üzerinden connect() fonksiyonuna eriştik ve deneme.db isimli veritabanına bağlandık ve bu bağlantı işlemini connection adlı değişkene atadık bu bizim bağlantımızı taşıyacaak değişken ve proje içinde bunu çağırabiliriz bağlantıyı sorgulamak için;
connection = sqlite3.connect("chinook.db")#sqlite3 modülü üzerinden connect() fonksiyonuna eriştik.deneme.py veritabanı mutlaka kullanılan package içinde olmalı erişmek için

"""connect fonksiyonunun döndürdüğü bağlantı nesnesi,
 connection adlı değişkene atanır. Bu nesne, veritabanına yapılan bağlantıyı temsil eder ve veritabanı üzerinde işlem yapmak için kullanılır."""
cursor = connection.cursor()
"""connection.cursor():
Bağlantı nesnesi (connection) üzerinden cursor metodunu çağırır. Bu metod, veritabanı üzerinde işlem yapmamıza olanak tanıyan bir cursor nesnesi döndürür.
cursor:
Döndürülen cursor nesnesi, cursor adlı değişkene atanır. Bu nesne, veritabanı üzerinde sorgular çalıştırmak için kullanılır.
cursor nesnesi, SQL sorgularını yürütmek, veritabanından veri almak ve diğer veritabanı işlemlerini gerçekleştirmek için kullanılır."""

"""execute fonksiyonu, cursor nesnesi üzerinden SQL sorgularını çalıştırmak için kullanılır. Bu fonksiyon, SQL sorgusunu veritabanına gönderir ve sorgunun sonuçlarını döner.
 execute fonksiyonu, veri ekleme, güncelleme, silme ve seçme gibi çeşitli SQL işlemlerini gerçekleştirmek için kullanılabilir."""

cursor.execute("select * from customers where city='Oslo'") #exectute methodu içine sql sorguları yazılır mesela sadece oslo city olan müşterileri getir demektir bu kod
result = cursor.fetchall() #cursor içine olan tüm verileri gitip getirir

for customer in result:#result içindeki tüm verileri customer'e atar ve tane tane gezer bastırır
    print(customer[1]+" "+customer[2]) #1.ve 2.kolondaki bilgiler gelir

#not =eğer tek bir değer varsa o zaman for döngüsüne gerek yoktur fetchone() methodu ile kolayca yapılır
 #veritabanı ile iş bitince aynı dosyalama sistemlerinde olduğu gibi veritabanı bağlantısını kesmeliyiz
print("veritabanı bağlantısı hazır ...")