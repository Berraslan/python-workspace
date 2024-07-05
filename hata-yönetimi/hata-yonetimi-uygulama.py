# # #liste elemanları içinden yanlız sayısal değerleri bulunuz sayısal olmayan değerleri görünce program hata fırlatsın
# #
# # #soru1
# # liste=["1","2","3","4","325gf","44","rg","9"]
# #
# # for x in liste:
# #     try:
# #         sonuc = int(x) # x int ise sonuc içine atar ve printler alt satırda
# #         print(sonuc)
# #
# #     except ValueError: #eğer program ValueError ile karşılaşırsa except içine girer except'de contunie dediği için aslında tekrar try içine girer ve sadece int değerleri ekrana print edilmiş olur.
# #         continue
# #
# # #soru2 : kullanıcı klavyeden (q) tuşuna bamadıkça aldığınız her inputun sayı olduğundan emin olunuz aski halde hata mesajı fırlatınız
#
# while True:
#     sayi=input("Sayı giriniz : ")
#     if sayi=="q":
#         break #programı sonlandır
#     try:
#        sonuc = float(sayi)
#        print(f"girilen sayi : {sayi}")
#     except ValueError:
#         print("geçersiz sayı giridniz")
#         continue#contunie programın devam etmesini sağlar ki doğru sonuç alana kadar dönsün program

#soru3 Dictionary ve key bilgilerini parametre olarak alan get(dict,key) fonksiyonu hazırlayınız.
# urun={"urunAdi":"samsung s20","fiyat":10000}
#
# def get(list,key):#parametre olarak bir liste ve key ver
#     try:
#         return list[key]
#     except:
#         return None
# sonuc=get(urun,key="fiyat")
# sonuc = get(urun,key="urunAdi") #burada fonksiyonu çağırınca bizden parametre olarak liste ve key istedi liste olarak urun verdik key adı olarak da "urunAdi"
# print(sonuc)

"""Gönderdiğimiz text'i verdiğimiz renk ile yazmasını istiyoruz"""
def renklendir(text,renk):#dışarıdan renk ve text parametreleri alarak bu fonksiyon çalışacak çağrıldığında
    renkler =("White","Black","Orange","blue")
    if renk not in renkler:
        raise ValueError("Yanlış değer girildi Lütfen listeden renk seçiniz")
    if type(text) is not str : #eğer fonkisyonun parametre olarak aldığı text bilgisi str değilse farklı türse kullanıcıya aşağıdaki if bloğu çalışarak hata raise edilir
        raise TypeError("yanlış tipte veri girişi")
    print(f"{text} bilgisi {renk}'de yazıldı.") #eğer hiç bir hataya uğramazsa bu satıra gelir

renklendir("Merhaba","purple")#hata fırlatır TypeError purple listede yok

#try except ile gelenhatayı yakalayabiliriz as e diyerek de loglama yapıp ekrana print ile de yazdırabiliriz
try:
    renklendir("merhaba","Black")
    renklendir(10,"blue")
except Exception as e:
    print(e)


