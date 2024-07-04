#liste elemanları içinden yanlız sayısal değerleri bulunuz sayısal olmayan değerleri görünce program hata fırlatsın


liste=["1","2","3","4","325gf","44","rg","9"]

for x in liste:
    try:
        sonuc = int(x) # x int ise sonuc içine atar ve printler alt satırda
        print(sonuc)

    except ValueError: #eğer program ValueError ile karşılaşırsa except içine girer except'de contunie dediği için aslında tekrar try içine girer ve sadece int değerleri ekrana print edilmiş olur.
        continue