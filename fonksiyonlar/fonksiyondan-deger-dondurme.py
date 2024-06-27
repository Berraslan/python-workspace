#deger-dondürme kodun bi nevi platformadan bağımsız olmasını sağlar yani

def sum():
    return 10+20 #burada print() i kullanmadık çünkü kullancağımız platform pritni desteklemeyebilir return ettik ve

sonuc = sum() #return ettiğimiz sum() değerini sonuc değişkenine atamamız gerekir yoksa dönen değeri görüntüleyemeyiz veya print(sum()) yazılabilir

print(sonuc)


#örneğin şu anın yılından kendi yaşımızı return döndürerek hesaplama

def year():
    import datetime #burada dışarıdan modül import ettik alttaki bilgisayrın güncel tarihine erişim sağlamk için
    return datetime.datetime.now().year #bilgisayarın yılını return etiyor

def yasHesapla():
    return year()-2001 #return edilen year'dan 2001 çıkarılıyor year bilgisi burada bilgisayarınki ile aynıdır.

print(yasHesapla())


#bilgisyarın saat bilgisine göre karşılama mesajı yazaılım

def hour():
    import datetime
    return datetime.datetime.now().hour #import ettiğimiz modül sayesinde bilgisayarın saat bilgisini return alabiliyoruz

def greetings():
    if(hour()<12): #greeting() fonksiyonu içinde hour() fonkisyonu içinden gelen saat bilgisi hangi aralığa denk geliyorsa ona göre bir ekran çıktısı alırız
        return "Günaydın "
    else:
        return "Merhaba ! "

print(greetings())

#return yaptığın değer artok o fonksiyonu içinde barındırdığı değerdir yani hour() fonskiyonu return hour verdiği için fonksiyona fonksiyon aslına hour değerini temsil eden bir değişken görevi görüyor