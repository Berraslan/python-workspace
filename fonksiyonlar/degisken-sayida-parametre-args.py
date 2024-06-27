#fonksiyonlara değişken sayıda parametre nasıl gönderilir?

def sum (a,b): #dışarıdan a,b değişkenlerini alıyor ve toplayım return edelim
    return a+b

sonuc = sum(10,20) #buraya c için ekleme yapsak hata alırız çünkü parametre olarak tanımlı değil
print(sonuc)

#yukarıdaki sorunu çözmek için yöntem1

#bir liste tanımlanır veya tuple tuple'a eklendikçe fonksiyon içindeki for tüm elemanları gezer ve toplar bir değişken içinde daha sonra onu print eder
#kodun açıklaması : önce sayilar isimli bir tuple tanımladık  daha sonra sum isimli bir fosnkiyon tanımladık ve parametre olarak liste isimli bir parametre ismi verdik ama liste parametresi tipi any'dir yani biz ne atasak onu alacaktır bunu : str,int vs yazarak ayarlayabilirizde neyse
#daha sonra sonuc= 0 dedik ki for ile liste içindeki elemanları tek tek gezicez ve gezdiğimiz indisin değerini i'ye atıyım sonra sonuç ile i'yi toplayıp sonuca atıcaz en sonda tüm elemanları gezdikten sonra return sonuc diye sonucu döndürcez ama return çalışmak için print'e ihtiyac duyar
#fonksiyondan çıkıp print dicez ve içine sum() fonksiyonunu çağıracağız ve sum fonksiyonu liste adında any veri tipinde bir parametre istiyoru bizde sayilar isimli tuple veri tipli listemizi veriyoruz ve tamamdır.
#bu saatten sonra tuple içine eleman ekledikçe fonskiyon kendini yeni elemana göre güncelliyip toplama yansıtacaktır
sayilar =(10,20,30)

def sum (liste):
    sonuc=0 #for ile tuple gezilecek her indisteki sayı buraya atılan değerle toplanacak ve bu sonucun son hali print edilecek
    for i in liste:
        sonuc = sonuc+i
    return sonuc

print(sum(sayilar))




#yöntem2

def toplam(*args):
    print(args)
    print(type)