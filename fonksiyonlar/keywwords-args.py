def full_name(firstname: str, lastname: str, age: int) -> str:  #burada yapılan işlem şudur; normalde alınacak parametrelere str int demesezek herhangi tip atsak firstname veya lastname kabul eder ama biz böyle tip atayarak kısıtlıyoruz. -> str: derkende return bize yine str döndürsün diyoruz
    return f"Your name is {firstname}{lastname} and {age} years old"



sonuc = full_name("Berra ","Aslan",22)  #eğer böyle yazarsak mutlaka değeri atadığımız parametreye göre doldurmalıyız yani firstname kısmına aslan yazamayız
print(sonuc)

#parametreyi karışık yazmak için
sonuc1 = full_name(lastname=" Aslan ", firstname=" Berra", age=22) #böyle atandığı parametre değerini yazarsak karışık sırayla değer atayabiliriz
print(sonuc1)

