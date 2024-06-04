#karşılaştırma operatörleri
# == - eşit
# != - eşit değil
# >  - büyük
# <  - küçük
# >= - büyük eşit
# <= - küçük eşit

a,b,c,d = 2,2,10,5

sonuc = (a == b) #eğer a == b ise true veya false değeri sonuc değişkeni içine atılır bu sonrasında programnda bir yerde kullanılır veya print ile aşağıda bastırılır
print(sonuc)


sonuc = (a != b)  #a=2 b=2 bu durumda ikisi birbirine eşit buradaki sorgu eşitse false döndürür çünkü sorgu a eşit değil b mi diye soruyor.
print(sonuc)


e_posta = "info@deneme.com"
parola ="1324354647"

sonuc2= (e_posta ==input('eposta : ')) #buradaki işlem : kullanıcıdan string bir epsoat input'u alıyoruz ve eğer e_posta değişkenimize eşit ise sonuc2 değişkeni true döner
sonuc3 = (parola ==input('şifre bilginizi giriniz: '))
print(sonuc2)
print(sonuc3)

#not : true ==1 ; false ==0 'dır

sonucKiyas= (True == 1)
print(sonucKiyas)

sonuc = int(True) #bize 1 döndürür true değerini int karşılığı olan 1'e dönüşütürür
print(sonuc)

kiyasla = (a>=c)
print(kiyasla)