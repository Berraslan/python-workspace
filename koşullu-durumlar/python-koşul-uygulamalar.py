
#soru1
benzinLitreFiyat= 39.35
dizelLitreFiyat =41.71
lpgLitreFiyat = 20.28

ortalamaYakitTuketimi = float(input("Aracınız 100 km'de ne kadar yakıt harcıyor Litre cinsinden : "))
hangiTür= input("Hangi tür araç kullanıyorsunuz : 'benzin','dizel,'lpg'  ")
kaçKmGidildi= float(input("Kaç kilometre gidildi ? "))

benzinKmMasrafHesapla = ortalamaYakitTuketimi*benzinLitreFiyat*kaçKmGidildi
dizelKmMasrafHesapla = ortalamaYakitTuketimi*dizelLitreFiyat*kaçKmGidildi
lpgKmMasrafHesapla = ortalamaYakitTuketimi*lpgLitreFiyat*kaçKmGidildi

if (hangiTür =='benzin'):
    print(f"100 km'de ortalama {ortalamaYakitTuketimi} yakan {hangiTür} ile çalışan aracınız için hesaplanan masraf {benzinKmMasrafHesapla/100}'dır.")

elif (hangiTür =='dizel'):
    print(f"100 km'de ortalama {ortalamaYakitTuketimi} yakan {hangiTür} ile çalışan aracınız için hesaplanan masraf {dizelKmMasrafHesapla/100}'dır.")

elif (hangiTür =='lpg'):
    print(f"100 km'de ortalama {ortalamaYakitTuketimi} yakan {hangiTür} ile çalışan aracınız için hesaplanan masraf {lpgKmMasrafHesapla/100}'dır.")

else:
    print("Yanlış yakıt tipi.")


l


