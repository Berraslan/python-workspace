
#soru1
yas= int(input("yaşınızı giriniz : "))
veliIzinizVarMi= input("Evet mi Hayır mı? : 'Evet' 'Hayır' : ")

if ((yas>18) or (veliIzinizVarMi=='Evet')) :
    print("Bir işte çalışabilir")

else :
    print("bir işte çalışamazsınız")



#soru2

dersNot = int(input("ders notunuz nedir ? "))

if ((dersNot >= 50 and dersNot<=100)) :
    print("Tebrikler")

else :
    print("malesef")
#
#
# #soru3

notOrtalaması =int(input("not ortalamanız kaçtır ? "))
zayıfınızVarMı =input("zayıfınız var mı 'Evet' 'Hayır'  :  ")

if (notOrtalaması>=70 and zayıfınızVarMı !='Evet'):
    print("teşekkür belgesi alabilirsin")
else :
    print("teşekkür belgesi alamazısnız")

#soru4

neMezunusunuz =input ("Ne mezunu olduğunuzu giriniz : ")
sigaraKullanımı = input("sigara içiyor musunuz ? 'evet 'Hayır'")

if (neMezunusunuz == 'Önlisans' or 'Lisans') and (sigaraKullanımı=='Hayır'):
    print("İşe alındınız ")

else :
    print("malesef")

# #soru5 uygulamaya ister kullanıcı adıyla ister email ile giriş yapılır ama şifre mutlaka olmalıdır
#burası bizim daha önce kullanıcının kayıt olduğu verileri tutan veri tabanı
email ="info@deneme.com.tr"
username = "denemeDeneme"
password ="21231"

girilen_bilgi= input("email veya username giriniz : ")
girilen_sifre=input("şifrenizi giriniz : ")

if ((girilen_bilgi==email or girilen_bilgi==username) and (girilen_sifre==password)) :
    print("Giriş başarılı")

else :
    print("Başarısız giriş.")


