# #hesap bilgileri tutulacak {ad:, soyada: yas: , hesapdaOlanPara: }
#
# accounts = [
#     {
#         "ad":"berra",
#         "soyad":"aslan",
#         "bakiye":20000,
#         "ekHesap":1000,
#         "username":"berra",
#         "password":"1234"
#     },
#     {
#         "ad":"ayşe",
#         "soyad":"tur",
#         "bakiye":10000,
#         "ekHesap":2000,
#         "username":"ayşe",
#         "password":"124334"
#     },
#
# ]
#
# def menu(hesap): #hesap adında bir parametre alıcaz
#     print(f"mevcut bakiyeniz {hesap['bakiye']} daha detaylı bilgi için aşağıda yapmak istefdiğiniz işleme tıklayınız") #burada {hesap['bakiye']} kullanmalıyız çünkü hesap parametresi üzerinden erişiyoruz accounts listesine ama eğer accounts üzeerinden erişemeye çalışırsan oraya erişim yetki bloğunda olmadığından hata alırsın
#
# def login():
#     username= input("username bilgisi giriniz : ")
#     password= input("password bilgisi giriniz : ")
#
#     isLoggedIn =False
#
#     for hesap in accounts:
#         if hesap["username"] ==username and hesap["password"]==password:
#             isLoggedIn =True
#             menu(hesap) #login olmuş hesap için menu'yu göstermek adına menu fonskiyonunu çağırıp içine de login olmuş hesap değişkenini atadık
#             break #break deriz ki for'dan çıksın sonraki hesaplara bakmasın
#
#     if not (isLoggedIn):# eğer username veya password veya ikiside yanlışsa o zaman for'a girmez ve buraya gelir zaten başta false olan IsLoggedIn'in not hali alınır ve TRUE olunca if içi çalışırı ve ekrana hata mesajı kullanıc adı veya şifre der
#         print("Kullanıcı adı veya parola yanlış")
#
# login()

#hesap bilgileri tutulacak {ad:, soyada: yas: , hesapdaOlanPara: }

#account kısmını aslında daha gelişmiş projelerde veri tabanı gibi düşünebilirsin çünkü bu tarz müşteri verileri oradan gelicektir proje içine
accounts = [
    {
        "ad":"berra",
        "soyad":"aslan",
        "bakiye":20,
        "ekHesap":1000,
        "username":"berra",
        "password":"1234"
    },
    {
        "ad":"ayşe",
        "soyad":"tur",
        "bakiye":10000,
        "ekHesap":2000,
        "username":"ayşe",
        "password":"124334"
    },

]

def menu(hesap): #hesap adında bir parametre alıcaz
    print(f"Merhaba {hesap['ad']}")

    print("1 - Bakiye sorgulama")
    print("2 - Para Çekme")
    print("3 - Para Yatırma ")

    islem = input("Yapmak istediğiniz işlem nedir ?")

    if islem == "1":
       bakiye_Sorgula(hesap)
    elif islem=="2":
       para_Cek(hesap)
    elif islem =="3":
        para_Yatir(hesap)
    else:
        print("yanlış tuşlama yaptınız")

    menu(hesap) #bu fonksiyonu çağıralım ki tekradan tuşalma yapıldıktan sonra uygulma durmasın diğerlerini de test edebilelim

def login():
    username= input("username bilgisi giriniz : ")
    password= input("password bilgisi giriniz : ")

    isLoggedIn =False

    for hesap in accounts:
        if hesap["username"] ==username and hesap["password"]==password:
            isLoggedIn =True
            menu(hesap) #login olmuş hesap için menu'yu göstermek adına menu fonskiyonunu çağırıp içine de login olmuş hesap değişkenini atadık
            break #break deriz ki for'dan çıksın sonraki hesaplara bakmasın

    if not (isLoggedIn):# eğer username veya password veya ikiside yanlışsa o zaman for'a girmez ve buraya gelir zaten başta false olan IsLoggedIn'in not hali alınır ve TRUE olunca if içi çalışırı ve ekrana hata mesajı kullanıc adı veya şifre der
        print("Kullanıcı adı veya parola yanlış")


def bakiye_Sorgula(hesap):
    print(f"{hesap['ad']} adlı müşterimizin {hesap['bakiye']} bakiye bilgisi gösterilmektedir")
    print(f"ek hesap bilgisi :{hesap['ekHesap']}")

def para_Cek(hesap):

    cekilmekIstenenTutar= float(input("Çekilmek istenen tutarı giriniz : "))

    if hesap['bakiye']> cekilmekIstenenTutar:
        hesap['bakiye'] -=cekilmekIstenenTutar # hesap['bakiye'] normalde int bir değer ve bu işlem sayesinde hesap['bakiye'] -=cekilmekIstenenTutar cekilen tutarı bakiyedn düşüp aslında bakiye'yi güncelemiş oluyoruz
        print(f"Hesapda kalan güncel bakiye {hesap['bakiye']}")

    else : #neden elif diyip hesapda yeterli miktar yok ek hesaba yönlendirmedik çünkü belki normalde + bakiyedir ama çekeceği tutar kadar yoktu bu durumda bakiye+ek hesap deriz o toplamı gösteririz paranın yeten kısmını + bakiyedn yetmeyen kısmını ise ek hesaptan isteyip istemediğini sorarark öyle veririz
        toplam = hesap['bakiye']+hesap['ekHesap']

        if toplam >= cekilmekIstenenTutar:
            ekHesapKullanimiIzni = input("Hesabınızda yeterli miktarda bakiye yok ek hesap kullanmak ister misiniz ? 'E' veya 'H'")

            if ekHesapKullanimiIzni =='E': #ek heasp kulanımınıa izin verdiyse kişi önce bi + bakiyesi var mı diye bakılır eğer varsa bi kısmı oradan alınır daha sonrasında ek hesaba geçilir yoksa tamamı ek hesaptan tahsil edilirA
               ekHesaptanKullanilacakMiktar = cekilmekIstenenTutar -hesap['bakiye']
               hesap['bakiye']=0
               hesap['ekHesap'] -= ekHesaptanKullanilacakMiktar
               print(f"Ek hesaptan para çekme isteğinize istinaden para çekimi ek hesabınızdan gerçekleşmiştir mevcut bakiyeniz {hesap['bakiye']} ve ek hesap'da kalan bakiyeniz'de {hesap['ekHesap']}'dir.")


            elif ekHesapKullanimiIzni =='H':
                print("Başka bir işlem yapmak ister misiniz: ? Çünkü cari hesabınıda  istediğiniz tutarı çekecek limit bulunmamaktadır isterseniz ek hesaptan kullanabilirsiniz ")
                menu(hesap)
        else:
            print("Üzgünüz cari hesapta ve ek hesapta gereken limit mevcut değildir")


def para_Yatir(hesap,accounts):
    yatirilmakIstenenTutar= int(input("Yatırmak istediğiniz miktarı tuşlayınız : "))
    if hesap['ekHesap']==0 and hesap['bakiye']==0:
        ekHesapLimiti= accounts['ekHesap']
        hesap['ekHesap'] +=yatirilmakIstenenTutar
        if hesap['ekHesap'] > ekHesapLimiti:
            cariHesabaYatirilacakTutar= hesap['ekHesap']-ekHesapLimiti #burada ek hesaba fazladan ne kadar geçmiş onu hesaplıyorz fazla geçeni cari hesaba aktarıcaz
            hesap['ekHesap']  == ekHesapLimiti #burada ek hesap limiti tutarına sabitliyoruz artık para yatırma işlemi buraya devaö etmicek kalanı cari bakiye'ye aktaraacağız
            hesap['bakiye'] += cariHesabaYatirilacakTutar
        else


login()