#if-else blogu

login= "deneme@deneme.com"
parola = "2132"

loginCheck = input("email giriniz : ")
parolaCheck = input("parolanızı girniz : ")

#iç içe if

if(loginCheck==login): #mail doğru ise alltaki if çalışır
    if(parola==parolaCheck): #parola doğru ise if yanlısa else run edilir
        print("login olundu. ")
    else:
        print("parola yanlıştır. ")
else: #mail adresi yanlışsa direk bu print edilir
    print("mail adresi yanlıştır. ")