

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

# ogrenciNo= int(input("Öğrenci numarası giriniz : "))
#
# ogrenci = ogrenciler[ogrenciNo]
# ortalama = (ogrenci["notlar"][0] + ogrenci["notlar"][1] + ogrenci["notlar"][2]) / 3
#
# print(f'{ogrenciNo} numaralı {ogrenci["Ad"] } {ogrenci["Soyad"] } ismindeki öğrencinin yaşı {2024 - ogrenci["DogumYili"]} ve not ortlaması {ortalama}')
#
# #klavyeden okunan bilgilere göre dictionary'e eleman ekleme

ogrenciName = input("İsim giriniz : ")
ogrenciSurname = input("Soyad giriniz : ")
ogrenciBornDate = int(input("Doğum Yılı Giriniz : "))
ogrenciNote = input("Not Bilgisi Giriniz : ")



ogrenciBilgisineUlas = int(input("Öğrenci no : "))

ogrenci = ogrenciler[ogrenciBilgisineUlas]

print(f"{ogrenciBilgisineUlas} {'Ad'} , {'Soyad'} , {'DogumYili'}, {'notlar'} ")
