

def selamVer(isim = "ziyaretçi"): #string değerinde bir parametre veririsiz fonskiyona eğer parametre atamazsak default olarak ziyaretçi desin demiş olduk
    print("Merhaba " + isim)


selamVer("Berra")
selamVer() #default paremtre ile çalıştı biz parametre vermediğimiz için

def dikUcgenHesapla(sayi1,sayi2):
    print("sayı1 : " +str(sayi1))
    print("sayı : " +str(sayi2))

    return int(sayi1+sayi2)


print(dikUcgenHesapla(3,5))