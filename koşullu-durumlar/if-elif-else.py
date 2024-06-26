#if-elif-else blogu

login= "deneme@deneme.com"
parola = "2132"

loginCheck = input("email giriniz : ")
parolaCheck = input("parolanızı girniz : ")


if (loginCheck == login) and (parolaCheck==parola): #login içindeki değer loginChek inputu ile alınan değere eşit ise burası çalışır
    print("Login Olundu ! ")

elif (loginCheck==login and parolaCheck !=parola) :
    print("Parola Yanlışlığından kaynaklı login olunamadı.")

elif (loginCheck !=login and parolaCheck ==parola):
    print("email adresi yanlış olduğu için login olunamadı.")

else: #yanlış ise burası çalışır
    print("Login başarısız çünkü hem parola hem de email adresi yanlış !")
