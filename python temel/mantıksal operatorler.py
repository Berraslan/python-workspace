
ehliyetVarMi = False

arabaVarMi = True


if ehliyetVarMi and arabaVarMi :
    print("Araba kullanabilirsin.")

elif arabaVarMi and not ehliyetVarMi:
    print("Bizi tercih ederek araba kullanabilirsin")


elif ehliyetVarMi or arabaVarMi:
    print("Araba kullanmana çok az kaldı")

else:
    print("Araba kullanman için çok zaman var")

