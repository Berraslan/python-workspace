#class'ın bulundurabileceği ögeler:
#attributes(veya properties'de denebilir bazen-özellikler)
#method(iş yapan)

#eğer bir class'ın içini doldurusak verilerle bu o class'dan örnek almak demektir veya instance'da denebilir
#class'dan örnek alınıp oluşturulan her bir yapıya da nesne(object) denebilir

#class aslında bir şablondur.

"""Önemli Not: Sınıf(class) içine tanımlanan fonksiyonlar'a method() denir ama eğer class dışında bir fonksiyon tanımlanıyorsa aynı fonksiyon denir."""

class Product: #CLASS İSİMLERİ BÜYÜK YAZILIR
    #attributes
    #method
    def __init__(self):

        print("nesne oluşturuldu")

#class'dan nesne oluşturma veya örnek alma (instance alma veya örnek alma denir bu işleme)

#p1 ve p2 tamamiyle değişken ismiyle aynı aslında anlamı p1 isminde bir nesne
p1 =Product()
p2=Product()

print(type(p1))#p1 nesnesinin product isimli bir sınıfın nesnesi olduğunu söyler

sonuc =p1 #p1'i sonuc değişkeni içine attık

print(p1) #çıktı bize p1'nesenesinin hangi bellek adrsinde tutulduğunu gösterir ayrıca nesneler class'ın kopyası da denebilir aynı örnek alma ile aynı anlamıdır sadece önüne çıkarsa şaşırma aynı anlam
#nesne oluşturma = classdan kopya alma=classdan örnek alma'dır

"""ayrıca bir class içinde tanımlanan tüm yetenekler özellikler onların nesnelerine de aktarılır ve kullanımına sunulur."""