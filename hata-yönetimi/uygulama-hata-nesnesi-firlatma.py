# def faktoriyel(x): # fonksiyon x adında bir parametre alır
#
#     x = int(x) # burada alınan x değerin, integer'a çeviriyoruz ki faktöriyel işlemini doğru yapalım
#
#     if x < 0:
#         raise ValueError("NEGATİF DEĞER") # eğer gelen parametre negatif bir sayı ise faktöriyel hesaplanamaz ve ValueError raise edilir.
#
#     sonuc = 1
#
#     for i in range(1, x + 1): # burada gelen x parametresini faktöriyel işleminde çarpmaya başlamadan önce açıyoruz
#         sonuc *= i # sonuc normalde 1 değerini tutuyor, gelen parametre range içinde 1'den mevcut olduğu x sayısının +1 haline kadar açılacak ve bu sayılar için bu çarpma işlemi devam edecek
#     return sonuc
#
# list = [3, 6, 7, '2a', -1, -7, 9]
#
# for i in list:
#     try:
#         x = faktoriyel(i) # i liste içinden her elemanı tek tek gezip buraya getirir ve faktoriyel fonksiyonuna parametre olarak atar
#     except ValueError as e: # except'e bir şey gelirse e olarak hata kaydedilir ve print ile ekrana yazılır
#         print(e)
#         continue
#     else: # eğer değer except'e girmiyorsa buraya gelip x değerlerini yazdır
#         print(x)
#

#kullanıcında alınan password değerininin türkçe karakter içeip içermedğini kontrol etme
def checkIsTurkish(password): #kullanıcıdaan alınan password kontrol için fonksiyona verildi
    turkish_characters = "öüşıçğÖÜŞİÇĞ"  # Türkçe karakterler bitişik string olarak tanımlandı.
    passwordLenght= len(password)
    if passwordLenght != 8: #for döngüsünün dışında koyduk çünkü karakter karakter tanımlanırken her seferinde uzunluğu de hesaplayactır döngü dışında tanımlamak bu sorunda kurutlup sadece 1 kere bu kotnrolün yapılamsını sağlar
         raise ValueError("Parola 8 karakterden daha az")

    for char in password:  # Parolanın her bir karakterini for tek tek kontrol eder.
        if char in turkish_characters:
            return(f"Türkçe karakter girildi: {char}")  # Türkçe karakter bulunursa TypeError hata fırlatılır.
        elif passwordLenght != 8:
           return("Parola 8 karakterden daha az")


    print("Parola geçerli:", password) #eğer hata yoksa parola geçerli diye yazdırır

# Kullanıcıdan parola al
password = input("Lütfen bir parola giriniz: ")

try:
    checkIsTurkish(password) #doğru ise try bloğu çalışır
except TypeError as e: #yanlış ise except içine girer e ise yakalanan hatayı e değişknei ile kullanabilmeyi sağlar.
    print(e)
except ValueError as e: #yanlış ise except içine girer e ise yakalanan hatayı e değişknei ile kullanabilmeyi sağlar.
    print(e)
#try except sayesinde kullanıcıya daha düzgün bir görünütü gösteriyoruz


"""Raise bir hata fırlatır try except'de bunu yakalar return kullanırsa raise yerine ek kod yazmamız gerkeiy çünkü return hata fırlatmaz sadece hata değeri döndürü onu ele almak için ek kod yazarız ama raise bir hata fırlatır ve bu hata try exceptte yakalanır"""