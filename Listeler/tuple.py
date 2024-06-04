#tuple: bir liste çeşididir. fakat liste'nin sahip olduğu çoğu metodu çalıştıramaz mesela tuple oluşturulduktan sonra eleman silini çıkarılamaz.
#neden tuple'a gerek duyarız.
# farz edelim ki veritababnından pull işlemi yaptık ve bu pull yaptığımız verileri değiştimicez o zaman kodun çalışma performanısnı arttırmak için
# tuple kullanılır çünkü list yapısın göre daha light'dir.

#veya çektiğiniz verilerin değiştirilmesini yanlışlıkla istemiyorsunuz güvenli bir kod yazmak için de tuple kullanılır.

my_list = [1,2,3] #normal liste tanımlamada [] karakterler kullanılır

my_tuple= (1,2,3) #parantezli tanımlama ise tuple tanımlamadır.

print(my_list) #değiştirilebilir
print(my_tuple) #değiştirilemez

sonuc = my_list