#Range metodu elimizde bir liste olmadan liste oluşturmayı ve for'da kullanmayı sağlar
#normalde for elimizde hazır bir liste varken kullanılır bu yüzden while döngüsü kullanıyorduk liste yokken
#ama range metodu whilde döngüsü kullanmadan for'u hazır liste olmadan kullanmayı sağlar

#range(başlangıç,bitiş,step sayısı)
#kodun açıklaması : 1'den başla 100'e kadar 2 şer 2 şer arttır
for i in range(1,100,2):
    print(i)

#range metodunu değişken içine tanımlayarak yapacaksak bu sefer list yapısına dönüştürmemiz gerekecek.

rng =range(10) #başlangıç ve step belirtmezsek içinde yazan sayı dahil olmadan 0'dan başlar yazmaya
rng =range(10,20) #10'dan başlar 20 dahil olmadayn 20'ye kadar yazdırır.
rng = range(100,200,10) #100 ile 200 arasını 10'ar 10'ar gider
rng=range(200,100,-20) #200'den başla 100'e kadar -20 -20 azaltarak ilerle

sonuc = list(rng)
print(sonuc)


#50 ile 250 arasındaki çift sayıları range metodu ile yazdır

for i in range(50,250):
    if(i%2==1):
        continue
    print(i)
