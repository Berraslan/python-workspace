#soru2

yazili1= int(input("1.yazılınız kaçtır : "))
yazili2=int(input(" 2.yazılınız kaçtır : "))
sozluNotu =int(input("Sözlü notunuzu giriniz : "))

ortalamaHesapla = float((yazili1+yazili2+sozluNotu)/3)

if(ortalamaHesapla>=0 and ortalamaHesapla <=24):
    print(f"ortalamnız :{ortalamaHesapla}değerlendirme sonucunuz O aldınız")

elif(ortalamaHesapla>=25 and ortalamaHesapla <=44):
    print(f"ortalamnız :{ortalamaHesapla} değerlendirme sonucunuz  1 aldınız")

elif(ortalamaHesapla>=45 and ortalamaHesapla <=54):
    print(f"ortalamnız :{ortalamaHesapla} değerlendirme sonucunuz 2 aldınız")

elif(ortalamaHesapla>=55 and ortalamaHesapla <=69):
    print(f"ortalamnız :{ortalamaHesapla} değerlendirme sonucunuz 3 aldınız")

elif(ortalamaHesapla>=70 and ortalamaHesapla <=84):
    print(f"ortalamnız :{ortalamaHesapla} değerlendirme sonucunuz 4 aldınız")

elif(ortalamaHesapla>=85 and ortalamaHesapla <=100):
    print(f"ortalamnız :{ortalamaHesapla} değerlendirme sonucnuz 5 aldınız")

else :
    print("Yanlış not bilgisi girilidi ")

