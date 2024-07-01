#dosya açmak için open() metodu kullanılır.

"""Dosya açamak ve oluşturmak için open() fonkisyonu kullanılır

 Kullanımı (usage) : open(dosya_Adi, erişim_modu)
 dosya_Erişim_modu : dosyayı hangi amaçla açtığınızı belirtir
 "r" okuma modudur : okuma modu ayarlandığı zaman mutlaka o konumda var olan bir dosya bulunmalıdır eğer erişim modu belirtilmezse otomatik olarak read modu atanır.
 seek : crusor
 """

"""open( metodu bize geri dönüş olarak bir obje döndürür io.TextIOWrapper adında ve bu nesnenin üzerinde yapılabilecek işlemler tanımlanabilir kısaca log.txt dosyası bellekte bir obje ile temsil edilir)"""
f=open("log.txt","r",encoding="utf-8")#encoding ="utf-8 yapmaszak karakterler saçmalar" #open() metodu çalışması için bir değişkene atanmalı çünkü bir değer döndürür ve biz bu değere bu değişken üzerinden erişebiliriz
print(f.read()) #bu f değişkeni bir obje tutuyor ve bu objenin sahip olduğu metodlar vardır



"""python crusor mantığı ile çalışır yani bir ker f.read() metodu çağrıldığı zaman dosya başatn sona okunur eğer aynı anda alt alta iki tane f.read() tanımlanırsa
sadece biri çalışır diğeri boş döner çünkü ilki hepsini okumuştur ve crusor dosyanın sonunda durur eğer proje çalışırken txt'ye yeni eleman eklersek cruosor kaldığı yer doyanın en sonu olduğu için baştan okuyup
eklemez sadece o yeni eklene değeri ekler 

eğer crusor'ü 0 yapıp en başa dönemk istiyorsak seek(0) metodunu kullanmalıyız


seek(10) demek imleci 10.byte'a al demek 1.satır\n2.satır\n3.satır\n4.satır şeklinde bellkelte tutulur ve her bir karakter 1 byte değere tahmül eder ve \n'lar da sayılır

satır satır okuması için : f.readline() metodu kullanılır ve bu her saatırı tek tek bastırır

f.readlines() : her satırı tek tek okur ve bunu bir listeye yazdırır ve liste elemanı olarak geri döndürür.

satirlar =f.readlines()  satirlar adlı değişken artık bir liste tutuyor readlines() metodu sayesinde
>>> satirlar[0] dediğimiz zaman bize listede 0.indisteki elemanı döndürür
'1.satır\n'

"""
"""f=open() metodu bize bellekte bir referans veriri ve biz elimizdeki dosyayı bellekte bir obje olarak tutarız eğer
dosyamız açık mı bellekte kapalı mı öğrenmek için 

f.closed -> deriz ve eğer dosya bellekte açıksa false döner kapalıysa true döner 

dosyayı bellekte kapatmak için f.close() metodu kullanılır yanlız bu metod kullanıldıktan sonra bellekteki obje kapatılacağı için dosya üzerinde seek().read() gibi veya başka şeyler yapılamaz
tekrar o dosyayı f.open() metodu ile bellekte objeyi aktive etmek gerekir.

"""