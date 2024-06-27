# # #soru1
# #
# # word =input("Lütfen kelime giriniz: ")
# # kacKezTekrar = int(input("tekrar sayısı giriniz"))
# #
# # def kelimePrint (word,kacKezTekrar):
# #     for i in range(kacKezTekrar):
# #         print(word)
# #
# #
# # kelimePrint(word,kacKezTekrar)
# #
# # #soru2
#
# kisa_Kenar= int(input("kısa kenar giriniz (cm) : )"))
# uzun_Kenar = int(input("uzun kenar giriniz (cm) : ) "))
#
# #alan hesapla
#
# def alanHesapla(kisa_Kenar,uzun_Kenar):
#     alan_Bilgisi = kisa_Kenar*uzun_Kenar
#     return alan_Bilgisi
#
#
# def cevreHesapla(kisa_kenar,uzun_kenar):
#     cevre_bilgisi = 2*(kisa_kenar+uzun_kenar)
#     return cevre_bilgisi #normalde print ile yazdırıp altta sadece fonkisyon ismi ile de çalıştırabiliriz ya d return deriz bu sefer fonksiyon dışında fonskiyonun ismini prinle çağırmak gerekir
#
#
# print(alanHesapla(kisa_Kenar,uzun_Kenar))
#
# print(cevreHesapla(kisa_Kenar,uzun_Kenar))

#soru3 yazı tura uygulaması - random kütüphanesinden rastgele seçm yapmak için kullanıla choice() metodunu kullanmak için import ettik bir liste tanımladık ve bu listeyi fonkisyona verdik
yazi_tura=["Yazı","Tura"]
def yazi_Tura(yazi_Tura):
    import random
    return random.choices(yazi_tura)

print(f"{yazi_Tura(yazi_tura)}")


#kendisine gönderilen sayının tam bölenlerini bulma

def tamBolenleriBul(sayi):
    tamBolenler=[] #boş liste tanımladık ki sayının tam bölenlerini bu liste içine yazıp printlicez

    for i in range(2,sayi): #i burada bölme ihtimali olan sayılar kümesi
        if(sayi%i==0):
            tamBolenler.append(i)
    return tamBolenler

print(tamBolenleriBul(20))