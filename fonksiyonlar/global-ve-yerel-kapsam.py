# #local scope - yerel kapsam
# #global scope - genel kapsam
#
# #bir fonkisyon tanımlandığı zaman içindeki değişkenlerin tanımlandığı ayrı bir alan var
#
# #her fonksiyon kendi localindeki değişkeni kullanır yani fonksiyon dışında da aynı isimli değişken olsa bile içerisindeki değişkeni kullanır
#
# x = "Global scope"
#
# def my_func():
#     x="local scope"
#     print(x)
#
# print(x) #global'deki x değişkeni kullanıldı
# my_func() #fonkisyon içindeki x değişkeni kullanıldı
#
#
# name ="Çınar"
#
# def change_name(new_name): #new_name adında bir parametre tanımladık bu demek oluyor ki func çağrıldığı zaman mutlaka new_name adında bir parametre geçilmeli fonksiyona; bazen parantez içi başka yerlerden gelen değişkenleri kullanmak için de buraya tanımlanabilir
#     name=new_name #parametre olarak aldığımız new_name değişkenini name adlı değişkene atadık
#     print(name)
#
# print(name) #burada globaldeki name print edildi
# change_name("berra") #burada fonksiyona içindeki name print edildi
#
# #ama eğer fonksiyon içinde'de global değişkeni kullanmak istersek global etiketini name değişkeni önüne etiketlemek gerekir
#
# name ="Çınar"
#
# def change_name(new_name):
#     global name #burada artık globaldeki name kullanılır yani yani buranın içinde yapılacak değişiklik dışarıdaki name değişkeninini de değiştirecek
#     name=new_name
#     print(name)
#
# change_name("berra") #eğer change_name fonksiyon çağrısını print(name)'den sonra yazarsam name içinde Çınar yazar ama önce fonksiyonu çalıştırır argümanı atıp name'i değiştirisem artık globaldeki name'de değişecektir
# print(name)
#
#
# #aşağıdaki kodun açıklaması
# name = "global string"#en dışa bir global değişken atandı
#
# def greetings():
#     name="Çınar"  #greetings() fonksiyonu içine name adına Çınar atandı
#     def hello(): #hello() adında greetings() fonksyonu altında fonkisyon yazıldı
#         name ="Ada"  #ada isimli değişken eklendi
#         print("hello",name) # buradaki name bastırılması için greetings() fonkisyonu içinde hello() fonkisyonunu çağırmak gerekiyor ve çağrıldığı zaman Ada çağrılır sonra eğer onu slersek çınar eğer çınar'ıda silersek global string print bastırllır
#
#     hello()
#
# greetings()
#
#
# #
# x=50
#
# def test(x):
#     print(f"x: {x}") #globaldeki x'i alır ama onda herhangi bir değişiklik yapmaz sadece değerini alır
#
#     x=100
#     print(f"changed to {x}")
#
# test(x) #100
# print(x) #50
#
#
#
#

x=50

def test():
    global x
    print(f"x: {x}") #50

    x=100
    print(f"changed to {x}")

test() #100
print(x) #100





