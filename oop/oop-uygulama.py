
class Bank_Account():

    def __init__(self,name):
        self.name =name # bunun anlamı nesnemizi tutan self'in name alanına dışardan aldığımız name bilgisini atıyoruz
        self.bakiye = 0.0 #başlangıç hesap açılışı 0'dır. parametre olarak () içine  vermek zorunda değiliz eğer ilk başta kullanıcıdanbir değer almıcaksak


    def para_yatir(self):
       yatirilacak_miktar= float(input("Yatırmak istediğiniz miktarı giriniz : "))
       self.bakiye+= (yatirilacak_miktar)
       return f"Hesabınıza yatırma işleminden sonra güncel bakiyeniz {self.bakiye}"

    def para_cek(self):
        cekilecek_miktar= float(input("Çekmek  istediğiniz miktarı giriniz : "))
        self.bakiye-= (cekilecek_miktar)
        return f"Hesabınıza yatırma işleminden sonra güncel bakiyeniz {self.bakiye}"


hesap = Bank_Account("Sadık Turan")

while True:
    print("\nİşlem Menüsü:")
    print("1. Para Yatır")
    print("2. Para Çek")
    print("3. Güncel banka hesap bilgisni gönder")
    print("4. Çıkış")

    secim = input("Lütfen yapmak istediğiniz işlemi seçiniz (1, 2, 3, 4): ")

    if secim == "1":
        print(hesap.para_yatir())
    elif secim == "2":
        print(hesap.para_cek())
    elif secim =="3":
        print(f"\nGüncel hesap bakiyeniz : {hesap.bakiye}")
    elif secim == "4":
        print("\nÇıkış yapılıyor...")
        break
    else:
        print("\nGeçersiz seçim. Lütfen tekrar deneyiniz.")

