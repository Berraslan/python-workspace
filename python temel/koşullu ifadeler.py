#if else bizim koşullarımızı bildirir.
#EĞER DIŞARISI YAĞMURLU İSE CEKETİNİ GİY

#YAĞMURLU BİZİM DEĞŞKENİZİMİZ VE EĞER TRUE OLURSA ONUN İÇİNDEKİ KODLAR ÇALIŞSIR FALSE İSE ELSE İÇİNDEKİ KODLAR ÇALIŞIR

isRain = False
isSunny =False
#NOT: if elif durumunda ilk if doğru ise diğerleirne bakmaz direk döngüden çıkar yanlış ise diğer elif'e gider
#hiçbir durum doğru değilse else çalışır
if isRain:
    print("ceketini giy")

elif  isSunny:
    print("güneş gözlüğü tak")

else:
    print("direk dışaı çıkıcam")
