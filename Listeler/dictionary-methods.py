#bu dictionary metodları default olarak dictionary class'ı ile birlikte gelmektedir.
#not liste'nin içide dictionary veya dictionary içinde list tanımlanabilir.
#dictionary : aynı string gibi bir veri yapısısdıdır


#yemekTarifi isimli bir liste veya bir diğer adıyla dictionary tanımladık
# #not:tuple,dictionary,sets ler birer list veri yapısıdır fakat farklı özellikleri vardır kendi içlerinde
yemekTarifi = {
    #key : value
    "yemek" : "Musakka",
    "yemekTarifi" : "tarif açıklaması",
    "resim" : "1.jpg",

}

sonuc =yemekTarifi["yemek"] # yemekTarifi listesinde yemek böülümüne erişmek için bu kodu yazdık değeri ekrana çıktılamak için sonuc'a attık
print(sonuc) # 'Musakka'

yemekTarifi.update({"yemek":"fasülye"}) # yemek keyinin kaşılığı musakka value'yu fasülye olarak günceller
print(yemekTarifi)

getYemekTarifi=yemekTarifi.get("yemekTarifi") #GET METODU İLE verilen key'in value'si döner
print(getYemekTarifi)

sonuc =yemekTarifi.keys() #sadece listedeki mevcut keys gelir
sonuc =yemekTarifi.values() #listedeki values değerleri gelir
print(sonuc)

 #adding new item

yemekTarifi["yemekAdi2"] = "dolma" #listeye yeni değer ekledi
print(yemekTarifi)
#not : update metodu ile yeni veri de eklenebilir farklı bir key değeri ile

#delete items #burada yemek isimli key ve value'sı silinir
yemekTarifi.pop("yemek")
sonuc =yemekTarifi
print(sonuc)

yemekTarifi.popitem() #listeye son ekleneni popitem() metodu ile sileriz
print(yemekTarifi)

yemekTarifi.clear() #liste içindeki tüm elemanları siler
print(yemekTarifi)



















#
# #dictionary metodları
#
# yemekTarifi = {
#
#     "yemekAdi" : "Musakka",
#     "yemekTarifi" : "tarif açıklaması",
#     "resim" : "1.jpg"
# }
#
# #Aşağıdaki metodlar bizim access items ( verilere erişim ) metodlarımızdır.
# sonuc=yemekTarifi["resim"] #arama için key verirken mutlaka [] içinde key yaz
# print(sonuc)
#
# sonuc1 = yemekTarifi.get("yemekAdi") #veya [] kullanmak yerine dictionary metodu olan get() kullanılabilir.
# print(sonuc1)
#
# sonuc2 = yemekTarifi.keys() #bu metod sayesinde dictionary yapısı içinde var olan tup key bilgilerini listele
# print(sonuc2)
#
# sonuc3 = yemekTarifi.values() #bu metod'da dictionary yapısı içindeki tüm value'ları listele
# print(sonuc3)
#
# sonuc4 = yemekTarifi.items() #dictionary yapısını içindeki elemanlala birlikte bir liste'ye çevirir.
# print(sonuc4)
#
#
#
# #update -güncelleme metodlarımız.
# yemekTarifi[
#
