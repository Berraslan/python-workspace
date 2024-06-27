#temelde bir işi yapan daha öncesinde yazılmış paket halinde duran yapıyı programda çağırma
#sadece çağrıldığında çalışır
#fonksiyon çalışmaya başlamak için dışaıdan parametreye ihtiyaç duyar örneğin : toplama işlemi yapan bir fonksiyon dışarıdan gelecek olan 2 sayıya ihtiyaç duysun

#ille bütün fonksiyonları biz yazacak değiliz dahaönce yazılmış ve bir kütüphane aracılığ ile gelen fonksiyonlarda projede kullanılabilir

#fonskiyonlar(metodlar) 2'ye ayrılır. Built-in ve user-defined
#built-in : hazırdır ve kütüphaneler ile  dahil edilir örneğin liste metodları append(),type()
#user-defined bizim kendimiz tarafından yazılan fonksiyonalardır.

#bir fonskiyon def anahtar kelimesi ile başlar ve sonra fonskiyonun adı yazılır

def say_hello():
    print("merhaba python")


say_hello()  #bir foksiyonun çalışması için onu böyle çağrımamız gerekir

#birden fazla kez yazdırmak için for döngüsü kullanılır range meodu ile birlikte

for i in range(10):  #range metodu sayesinde 0'dan başlar 10'a kadar yazdırı
    say_hello()

#dışarıdan parametre alan iki sayının toplamı

a = int(input("sayı giriniz : "))
b = int(input("sayı giriniz : "))


def sum(a, b):
    total = a + b
    print(total)


sum(a, b)
