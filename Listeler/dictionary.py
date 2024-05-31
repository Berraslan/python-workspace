#key-value türünde bilgi saklar
#order işlemine update işlemine tabi tutulabilir
#aynı keyler birden fazla kullanılamaz


#dictionary kullanmadan zahmetli hal ( yapamk istediğimiz işlem İstanbul verisi verildiği zaman 34 döndürmesi)
sehirler = ['Kocaeli','Istanbul']
plakalar1 = [41,34]

print(plakalar1[sehirler.index('Istanbul')]) #sehirler listesinden index metdou yardımıyla Istanbul'u bulduk ve index metodu indis döndürdüğü için aslında 1 döndürdü plaklalar[1]= 34 deriz.


#dictionary ile kolay yol
#{'key':value}

plakalar={'Kocaeli':41,

          'Istanbul':34,

          'Antalya': 6
         }

print(plakalar) #izmir yoktur.


plakalar['Antalya']= 7 #antalya ilinin liste'de yapılmış olan hatası burada 7 atanarak düzeltildi
print(plakalar)


plakalar['Izmir'] = 35 #sonradan eleman ekleme
print(plakalar) #artık izmir de eklidir


print(plakalar['Kocaeli']) #key değeri value olan 41 döndürür
