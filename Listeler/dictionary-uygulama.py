
#not: ogrenciler burada bizim dictionary liste adımız
#not : 101,102,103'ler bizim key kısmımızdır.
#not : key'lere karşılık gelen { } içindeiler ise keylere tekrar dicitonary tanımladık önemli not biz key karşısına value olarak sadece 'string', 'int'  tanımlamayız bu valuelar buradaki gibi dictionary olabilir,list olabilir,tuple olabilir
#yani key 101'e karşılık gelen istedğiğiniz veri türü olabilir
# ogrenciler aslında yine bir list'dir ve
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

ogrenciNo = input('öğrenci no: ') #klavyeden string tipinde input alıp ogrenciNo değişkeni içinde bu değer saklanır
ogrenciAcessogrenciler=ogrenciler[int(ogrenciNo)] #ogrenciNo değikeni içinde tutulan sayı değeri ogrenciler listesine parametre olarak verilir ve böylelikle indis gibi düşün klavyeden ogrenciNo 101 girilirse burada ogrenciler[101] keyin içindeki değerler çağırılır ve ogrencilerAcess değişkeni içie atılır
#ogrenciAcess değişkeni içinde misal 101 iinde tutulan değerler vardır ve biz bu değişkeni kullanarak ve buna parametreler göndererek 'Ad','Soyad' GİBİ BU VERİELRE BU DEĞİŞKEN ÜZERİNDEN ERİŞİRİZ
#ERİŞİM KAFANI KARIŞTIRMASIN AYNI INDİSLEME GİBİ


#klavyeden girilen ögrenci numarasına göre şu cümleyi yazdırın
#örnek : 101 numaralı Yiğit bilgi öğrenci yaş 14 not ort 70

yasHesapla = 2024-int(ogrenciAcessogrenciler['DogumYili'])
notAvarage = (ogrenciAcessogrenciler['notlar'][0]+ogrenciAcessogrenciler['notlar'][0]+ogrenciAcessogrenciler['notlar'][0])/3 #ogreciAcessOgrenciler değişkeninden not value eriştik ve oradan da indis değerleini topladık

print(f'{ogrenciNo} numaralı {ogrenciAcessogrenciler["Ad"]}   {ogrenciAcessogrenciler["Soyad"]} yaş : {yasHesapla} {ogrenciAcessogrenciler["notlar"]} ortlaması {notAvarage}')

#klavyeden girilen değerlere göre
