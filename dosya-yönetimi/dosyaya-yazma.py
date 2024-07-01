"""
Dosyaya yazma

erişim modunua "w" yazdığımızda dosyaya yazma özelliğini aktif etmiş olacağız

Normalde read modunda belirtilen dosya adında bir doysnın daha önce oluşturulmuş olması gerekiyordu
ama

write modu için böyle bir şart yok çünkü eğer öyle bir doysa yoksa o isimle yeni bir dosya oluşturur

Eğer belirtlien konumda aynı dosya varsa dosyayı siler yeni beir tane oluşturur.

"""


"""file = open("dosya.txt","w",encoding="utf-8")
#not: burada berra aslan yerine çınar turan yazarsak ne olur berra aslan'ı içeren dosya tamamen silinir ve yerine çınar turan yazılır yani write modunda veri ekleme değil veri yazma'dır bu da veri kaybına sebep olur dikkat
file.write("berra aslan\n") #geriye değer döndüren bir şey olmadığı için write'ı print() içine koymaya gerek yoktur
file.write("efe turan\n")

file.close() #close demek zorundayız çünkü demezsek dosya kapanmaz ve efile nesnesi bellkete açık kalır ve boşu boşuna yer kaplar"""

#dosyaya write yapar
with open("dosya1.txt","w",encoding="utf-8") as file:
    file.write("berra aslan\n")
    file.write("efe turan\n")


#yazılan dosyayı read eder r modu ile ve for ile de bu dosyanın içeriğini dosyayı gezerek çıktılar
with open("dosya1.txt","r",encoding="utf-8") as file:
    for i in file:
        print(i,end="")
