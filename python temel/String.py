isim = "ber'r'a"

print(isim)

isim1= 'be"r"ra'
print(isim1)

mektup=""""merhbas,,, 
fdkvvmdfk....""" #3 yukardan virgülle yazılan stringlerde noktasına virgülüne varıncaya kadar yazılır değiştirilmez

print(mektup)

isim2="ayşe"
isim3="FATMA"
print(isim2[0]) #isim değişkeninin 0.indisi verilir.
print(isim2[0:3]) #0.indisten 3.indis' kadar dahil eder 3.indis dahil değildir
print(isim2[-1])#sondan başlar almaya sondan 1.indisi yazar
print(isim[-4:-1])#sondan saymaya başlar

print(len(isim2)) #string'in karakter uzunluğunu verir
print(isim2.title()) #string'in sadece ilk harfini büyütür.
print(isim2.upper())#değişkenin bütün harfelrini büyütür
print(isim3.lower())#değişkenin bütün harflerini küçültür

print(isim2.find("a")) # a harfinin değişkende hangi indiste olduğunu bulur fakat python büyük küçük duyarılıdır.EĞER HARFİ BULAMZSA -1 DEĞER VERİR

sample = "Ahmet okula gidiyor"
print(sample.replace("gidiyor","gitmiyor")) #değişkende replace ile kelimeyi değiştirebilirsin
