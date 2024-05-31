

sayi1 = int(input("1.sayı : " ))
sayi2 = int(input("2.sayi : "))

islem= input(""""Yapmak istediğiniz işlemi giriniz

(Toplama: + , Çıkarma: -, Bölme: /, Çarpma: * ) """)

if islem =="+":
    print("sonuç : "+str(sayi1+sayi2))

elif  islem =="-":
    print("sonuc : "+str(sayi1-sayi2))

elif  islem =="/":
    print("sonuc : "+str(sayi1/sayi2))

elif  islem =="*":
    print("sonuc : "+str(sayi1*sayi2))

#"sonuc"+str(say1+sayi2)) demek aslında sonuç string olduğu için ve say1+sayi2 int olduğu için toplama işlemi yapıldıktan sonra hata atmaması için stringe döndürdük