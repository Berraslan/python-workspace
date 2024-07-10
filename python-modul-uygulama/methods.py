#method dosyamızda projenin yapamacağı işler yani methodlar vs bulunur

import db

def urunEkle(urunAdi,fiyat): #dışarıdan parametre olarak urunAdi ve fiyat bilgisi alacak bir fonkdiyondur ve db'deki urunler listesine eklicek alınan parametreleri
     db.urunler.append({
        "id":(len(db.urunler)+1),#db'deki tüm satır elamalnlarını nin bir fazalsını al ve ekle böylelikle id sayısı sistemiatik artmış olur çünkü her satır 1 elemanı tutuyor
        "urunAdi":urunAdi,#parametre olarak kullanıcıdan alınan değeri listeye append eder
        "fiyat":fiyat#parametre olarak kullanıcıdan alınan değeri listeye append eder
    })
#çalışma mantığı : id,urunAdi,fiyat parametrelerini alıyor fonksiyon for ile db.urunler listesini geziyor ve if ile eğer id'si parametre olarak gönderilenki ile aynı ise if içine girip urunun üzerinde güncelleme işlemleri yapıyor
def urunGuncelle(id,urunAdi,fiyat):
    for urun in db.urunler:
        if(urun["id"]==id):
            urun["urunAdi"]=urunAdi
            urun["fiyat"]=fiyat
            break #eğer aradığımız ürünü bulduysak ve if çalıştıysa break der ve döngüden çıkarız
#parametre almaz db içindeki urunleri return eder
def urunleriGetir():
    return db.urunler

def urunleriSil(id):
    for urun in db.urunler:
        if(urun["id"]==id):
            db.urunler.remove(urun)#urun geçici değişkeni parametre olarak id'yi bulunca db.urunler'e ılsş ve remove ile o urunu sil