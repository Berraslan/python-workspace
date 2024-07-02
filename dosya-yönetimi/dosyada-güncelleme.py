# """Dosya'da Güncelleme"""
#
#
# """Sona eleman ekler"""
# with open("markalar.txt","a") as file:
#     file.write("6-Bmw")
#
# # """Eğer aşağıdaki gibi bir ekleme işlemi yaparsanız seek kullanarak 0.indise bu veri kaybına sebep olur yani 0.indisteki bilginin üstüne yazar onu ötelemez"""
# # with open("markalar.txt","r+",encoding="utf-8") as file:
# #     file.seek(0)
# #     print(file.write("1-BMW"))
#
#
# """VERİ KAYBI OLMADAN DOSYAYI GÜNCELLEYİP ELEMAN EKLEMEK İÇİN (başa)"""
#
# with open("markalar.txt","r+",encoding="utf-8") as file:
#     markalar=file.read() #burada okuyup txt dosyasını markalar adlı değişkene atadık yani bir nevi yedekledik
#     markalar="1-Toyota\n"+markalar #markalar içindeki string veri ile bu string yapıyı birleştirdik ve markalara yeniden yazdık
#     file.seek(0)#crusor'ü 0 konumuna getirdim ki
#     file.write(markalar) #markalar txt'ye baştan basılsın
#
"""Araya eleman eklemek"""

with open("txt/markalar.txt", "r+", encoding="utf-8") as file:
    markalar =file.readlines() #önce readlines ile file içindeki txt'yi listeye çevirdik daha sonra bu listeyi markalar adlı değişkene atadık
    markalar.insert(2,"3-Renault\n")#artık markalar bir liste tuttuğu için liste method olan insert() kullanarak araya eleman ekleyebiliriz istediğimiz konumu ve eklenmek isteneneni yazarak
    file.seek(0)#crusoru 0.indise getirdik
    """for marka in markalar:#markalar listesini marka marka txt içine yazacak 
        file.write(marka)"""
    file.writelines(markalar) #for ile tek tek ulaşıp yazdırmak yerine writelines() metdou kullanarak yazdırabilsin

