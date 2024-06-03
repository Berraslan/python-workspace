#bu dictionary metodları default olarak dictionary class'ı ile birlikte gelmektedir.
#not liste'nin içide dictionary veya dictionary içinde list tanımlanabilir.

#dictionary metodları

yemekTarifi = {

    "yemekAdi" : "Musakka",
    "yemekTarifi" : "tarif açıklaması",
    "resim" : "1.jpg"
}

#Aşağıdaki metodlar bizim access items ( verilere erişim ) metodlarımızdır.
sonuc=yemekTarifi["resim"] #arama için key verirken mutlaka [] içinde key yaz
print(sonuc)

sonuc1 = yemekTarifi.get("yemekAdi") #veya [] kullanmak yerine dictionary metodu olan get() kullanılabilir.
print(sonuc1)

sonuc2 = yemekTarifi.keys() #bu metod sayesinde dictionary yapısı içinde var olan tup key bilgilerini listele
print(sonuc2)

sonuc3 = yemekTarifi.values() #bu metod'da dictionary yapısı içindeki tüm value'ları listele
print(sonuc3)

sonuc4 = yemekTarifi.items() #dictionary yapısını içindeki elemanlala birlikte bir liste'ye çevirir.
print(sonuc4)



#update -güncelleme metodlarımız.
yemekTarifi[

