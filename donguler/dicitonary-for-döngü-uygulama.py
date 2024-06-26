# products bir listedir ve elemanları birer dictionary'dir ayrıca dictionary içinde ise urun adı ve fiyat adlı keyler ve onlarında karşısında value değerleri vardır
products = [
    {"urunAdi":"Hp Victus 1","fiyat": 32999},
    {"urunAdi":"Lenova ThinkPad","fiyat": 25499},
    {"urunAdi":"Apple Macbook","fiyat": 49999},
    {"urunAdi":"Huawei MateBook","fiyat": 26999},
    {"urunAdi":"Casper Nirvana","fiyat":20000},
    {"urunAdi":"Hp Victus 2","fiyat":30000}
   ]
# #not FOR İÇİNDE BİR İŞLEM YAPICAKSAN MUTLAKA GEÇİCİ ATATDIĞIN DEĞİŞKEN ÜZERİNDEN LİSTEYE ERİŞİRSİN ÇÜNKÜ O LİSTE ELEMANLARINI HER BİR ÇALIŞMA ZAMANINDA TEK SEFERDE ALIR İSTENENE  GÖRE İŞLER VE BU İŞLEM ŞARTLAR SAĞLANANA KADAR DEVAM EDER
# for product in products:
#     print(f"{product['urunAdi']} marka ürünün fiyatı {product['fiyat']} dır")

#SORU 2 ÜRÜNLERİN FİYAT TOPLAMALARI NEDİR
totalAmount = 0;
for product in products:
    totalAmount += int(product["fiyat"]);
print(f"Ürünlerin toplamaları : {totalAmount}")

#soru3

for product in products:
    if (product["fiyat"] >=25000 and product["fiyat"]<=40000):
        print(f"25000 ile 40000 arasında mevcut olan ürün : {product['urunAdi']} fiyat : {product['fiyat']}")

#soru4 input ile alınan word değişkeni find metodu ile word verilerek aranır -1 den büyükse ürün adlarını yazdır
word= input("aramak istediğiniz ürünü giriniz: ")

for product in products:
    if(product["urunAdi"].lower().find(word.lower()) > -1):
        print(f"{product['urunAdi']}")