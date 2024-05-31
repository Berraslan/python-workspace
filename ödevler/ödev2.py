
yas = int(input("Yaşınızı giriniz"))

ogrenciMi= bool(input("Öğrenci misiniz?  (evet : e, hayır : h)"))

if yas >= 18 and ogrenciMi =="h":
    print("Askere gitme yaşınız geldi")

elif yas <= 18 and ogrenciMi=="e":
    print("Okul bitince askere gidiceksiniz")

else:
    print("Askerlik yaşınız daha gelmedi")