ogrenciler = {
    101 : {
        "Ad" : "Yiğit",
        "Soyad": "Bilgi",
        "DogumYili" : 2010,
        "notlar" : (40,80,90), #dictionary yapısının içinde her türde veri tipi tanımlanabilir ; int;string ;list;dictionary;tuple
    },
    102 : {
        "Ad" : "Ada",
        "Soyad": "Bilgi",
        "DogumYili" : 2012,
        "notlar" : [80,80,80],#tuple tanımladık
    },
    103 : {
        "Ad" : "Çınar",
        "Soyad": "Turan",
        "DogumYili" : 2017,
        "notlar" : [70,70,70],#tuple tanımladık
    },
}

ogrenciNo =(input("Öğrenci no giriniz : "))
ogrenci = ogrenciler[int(ogrenciNo)]

yasHesapla = 2024-int(ogrenci['DogumYili'])

#klavyeden girilen değerlere göre listeye eleman ekle

tellMeYourName = input("İsmini söyle : ")
tellMeYourSurname = input("Soyismini söyle : ")
tellMeYourBornDate = input("Doğum tarihini söyle : ")
tellMeYourNotes =input("Notlarını söyle : ")

# ogrenciler[104]= {
#     "Ad" : tellMeYourName,
#     "Soyad":tellMeYourSurname,
#     "DogumYili": tellMeYourBornDate,
#     "notlar":tellMeYourNotes,
#
# }

print(f"{ogrenciNo} no'lu {ogrenci['Ad']} {ogrenci['Soyad']} {ogrenci['DogumYili']} {yasHesapla} {ogrenci['notlar']}")



