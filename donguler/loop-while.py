#listeler = for ile

#while = koşullu durumda while kullan (eğer koşul sağlandığı sürece kodun çalışmasını istiyorsam WHILE kullanmam daha mantıklıdır)

#while zaten ingilizce'de -iken anlamına gelir .... iken bunu çalıştır demek aslında

# i=0;
# while i<10:
#     print(i)
#     i +=1 #bunu koymamızın sebebi sonsuz döngü olmasın ve i 10'a ulaşıp yazmayı bitirsin diye





#listeleri while ile de kullanabiliriz
#kodun açıklaması : sayılar adlı 9 elemanlı bir liste tanımladık.
#i=0 dedikk koşul olsun ve koşul sağlanana kadar döngü çalışır ve len(sayılar) ile 9 elelmanlı olduğu için 9 a kadar çalışacaktır 0'dan başalyıp koşul sağlandıkça while içine girip print çalışıcak o da sayıların index numarası ile erişip içindeki değeri yazacak ve her seferinde b,t,nce i 1 artacak ki döngü koşulu sağlasın ve sonlansın
sayilar = [1,2,3,4,5,6,7,8,9]

i=0;

while (i<len(sayilar)): #len burada işlemi dinamikleşitir yai liste genişledikçe bizim müdahale etmemize gereke kalmaz
     print(sayilar[i])
     i+=1

#ama elimizde bir liste varsa for kullanmak çok daha kolay