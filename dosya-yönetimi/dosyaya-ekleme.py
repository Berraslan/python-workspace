#erişim modları:

"""
r : dosya okuma modudur ->mutlaka o konumda bir dosya bulunmalıdır
w : dosyaya yazma modudur ->eğer dosya yoksa kendi bir tane açar ve içine yazar
a:  dosyaya ekleme modudur aynı ->aynı write gibidir eğer öyle bir dosya yoksa kendi açar ve üstüne ekler
r+ : hem okuma hem yazma modunda açılır.Eğer dosya konumda yoksa hata verir aynı read gibi

"""
"""with open("dosya.txt","a",encoding="utf-8") as file:
     file.write("birinci satır\n") #file değişkeni içine atanmış dosya.txt içine "birinci satır" yazısı atanır eğer uygulamyaı bir kere daha çalıştırısam cursorun olduğu yerden yine yazdırır
     #ama eğer append ile değil de write ile açmış olsaydık dosaynın içerisini tamamen silip yeniden yazdıracaktır
"""


with open("dosya.txt","a",encoding="utf-8") as file:
    file.seek(0)
    file.write("ikinci satır\n")