#bu string metodalrı python'da default olarak gelir

#not: ctrl +k+c kısayolu toplu yorum satırı yapar

mesaj ="BTK Akademi Python Kursu"

sonuc=mesaj.upper() #bu işlem sayesinde mesaj değişkeninde her hangi bir değişiklik olmayacak olan değişiklik sonuc içine yazılacak
sonuc1 = mesaj.lower() #tüm harfleri küçültür
sonuc2= mesaj.title()#her kelimenin ilk harfini büyütür
sonuc3=mesaj.capitalize() #ilgili cümlenin sadece ilk kelimesinin ilk harfini büyütür

sonuc4 = "abc".isupper() #is ile başlayanlar soru cümleleridir sonucu bool döndürür (burada büyük harf mi sorgusu yapılır)
sonuc5 =  "abc".islower()


deneme="   bu bir boşluk metnidir."

sonuc6 =deneme.strip() #baştaki boşluk kısmını atar çünkü veritabanına kayıt ederken bu bazen sorun olabilir



sonuc7 =mesaj.split() #bu string metodu cümledeki boşlıkların olduğu yerden kelimeleri ayrır ve bunları bir listeye çevirirp elemanları yapar o kelimelri de
sonuc8=mesaj.split()[1] #boşluklardan kelimeleri liste yaptığı için burada 1.indise denk gelen elemanı çağırcak 'Akademi'

#split() metodu default olaral boşluktan ayırır ama biz örneğin virgülden ayır da diyebiliriz
mesaj1="python ders , videoları bu platformda"
sonuc9= mesaj1.split(',')

sonuc10 =mesaj.replace("Python","javascript") #replace() metodu metinde Python yazan kelimeyi bul Javascript ile değiştir


#bütün string metodları yeni bir value döndürür orjinal string üzerinde güncelleme yapmaz
print(mesaj)
print(sonuc)
print(sonuc1)
print(sonuc2)
print(sonuc3)
print(sonuc4)
print(sonuc5)
print(sonuc6)
print(deneme)
print(sonuc7)
print(sonuc8)
print(sonuc9)
print(sonuc10)