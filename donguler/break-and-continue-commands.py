#continue komutu sadece belli bir şart gerçekleşmesi durumunda sadece o turdaki döngüyü iptal eder
#break komutu ise arkasından gelecek tüm döngüyü iptal eder

isim = "Sadık Turan"

# for harf in isim:
#     if (harf =="d"):
#         continue# continue olunca d ile karşılaşınca program d'yi atlar ve sonraki harfi yazdırmaya devam eder
#     print(harf)

for harf in isim:
    if (harf =="d"):
        break# break olunca d ile karşılaşınca program arkasından gelen tüm döngüyü iptal eder ve döngüden çıkar.
    print(harf)


#while dongüsü ile continue ve break komutu çalıştırma ("1'den 5'e kadar sayıları yazdır fakat 2'yi yazdırma )
#kodda önce sıfır değeri atayarak başlıyoruz i'ye sonra while içinde 5'den küçük olduğu sürece kodun çalışmasını söylüyoruz
#daha sonra koşulu vermeden önce i'yi 1 arttırıyoruz ki continue komutu geldiği zaman altındaki kodları çalıştırmaz direk döngünün başına gider bu seferde biz defatle aynı sayıyı görörürz bunu engellemk için i'yi bir arttır işlemini başta tanımlıyoruz sonda değil
i = 0

while(i<5):
    i+=1
    if(i==2):
        continue
    print(i)


#1'den 100'e kadar çift sayıların toplamını yazdır
#kodun açıklaması : önce 0'a eşit i değeri tanımlıyoruz sonra i 100den küçük ve eşit olduğu sürece alttaki kodu çalıştırır önce i'yi bir arttırır ki contunie den sonra koysak arttırmaz çünkü
#eğer i'nin 2'ye bölümünden kalan 1 ise tek sayıdır ve bunları yazdırma demektir ve if'e girmesi için sayının 2ile böümü 1 kalanını vericek eğer vermezse if'den çıkar ve toplam kısmına girer eğer 1 kalanını veren sayı varsa o sayı alt satıra gönderilmeden döngü başına döner ve sayı arttırılıp tekrardan gelir if'e

i=0
toplam=0
while (i<=100):
    i+=1
    if(i%2==1):
        continue
    toplam+=i

print(toplam)











