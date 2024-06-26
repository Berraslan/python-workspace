# #soru1

beginningValue= int(input("Bir başlangıç değeri girinz: "))
lastestValue = int(input("Son değeri giriniz: "))

i =beginningValue

while(i<lastestValue):
    if(i %2 ==0):
        print(i)
    i+=1 #if içine yazma while içine yaz if den çıkına sayı loop olmamamsı için 1 arttırılmalıdır.


# #soru2
#
i=100

while(i>0):
    print(i)
    i-=1

#soru3
#bu kodun açıklaması : i=0 değişkeni tanımladık ki 5 tane sayı alsın ve boş bir liste tanımladık az sonra alacağımız sayıları append ile liste sonuna ekleye ekleye gidicez sayilar ilestesine alınan sayıyı append ile ekleyip i 'yi bir arttırıyoruz ki sıradaki sayımızı alalım 5'e ulaşınca artık listemizde karşışık olarak sayılar ekli  biz bunları küçükten büyüğe sıralamak içinde sort() metdodunu kullandık
i=0
sayilar = []
while i < 5:
    sayi= int(input("Sayı giriniz : "))
    sayilar.append(sayi)
    i +=1

sayilar.sort()
print(sayilar)


#soru4#10 tane sayı alınız ve bu 10 sayının içinden sadece 2 ye bölünenleri yazıdırınız
#
# i=0
# liste=[]
# while i<10:
#     sayi=int(input("Sayı giriniz : "))
#     if sayi%2==0:
#         liste.append(sayi)
#     i+=1
# print(liste)

#soru5 kullanıcıdan username verisi al ama eğer kullanıcı usernamei boş gönderiyorsa sürekli olarak username girene kadar soruyu tekrarla
#kodun açıklaması : username değişkenni normalde "" durmunda boş strindir ve boş string programda bool karşılığı olarak false'ı işaret eder biz while döngüsünü çalıştırmaya itmek için true değer sağlamalayız ki sorgu çalışsın bu sebeple
#whilse not username deriz ki "" olan false değer true değere döndürürüüz ve while'ın çalışmasını sağlarız while içine girince username'e yeni değer atamaya çalışırız içini doldurualım ki usrname true olsun ve while not false olup döngüden çıksın ve print userenaame ekrana yazılsın
username=""

print(bool(username)) #boş durumda bool değeri false'dur.

while not username:
    username=input("username bilgisini giriniz") #

print("girilen username : "+username)