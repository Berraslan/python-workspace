#if-else blogu

login= "deneme@deneme.com"
parola = "2132"

loginCheck = input("email giriniz : ")
parolaCheck = input("parolanızı girniz : ")


#1.yöntem parola ve mail adresi kontol etmek için
if (loginCheck == login) and (parolaCheck==parola): #login içindeki değer loginChek inputu ile alınan değere eşit ise burası çalışır
    print("Login Olundu ! ")

elif (loginCheck==login and parolaCheck !=parola) :
    print("Parola Yanlışlığından kaynaklı login olunamadı.")

elif (loginCheck !=login and parolaCheck ==parola):
    print("email adresi yanlış olduğu için login olunamadı.")

else: #yanlış ise burası çalışır
    print("Login başarısız çünkü hem parola hem de email adresi yanlış !")


#2.yöntem mail adresi ve parola doğrulamak için

if(loginCheck==login): #mail doğru ise alltaki if çalışır
    if(parola==parolaCheck): #parola doğru ise if yanlısa else run edilir
        print("login olundu. ")
    else:
        print("parola yanlıştır. ")
else: #mail adresi yanlışsa direk bu print edilir
    print("mail adresi yanlıştır. ")