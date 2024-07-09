#debu işlmei uygulamamızda hata ayıklama işlemidir.

#bazen kodumduzdaki hatayı bulmak için satır satır işletmek gerekebilir.

""""
Debug için pyhtonda import pdb kütüphanesini koda dahil etmeliyiz. daha sonraa da kodun içinde pdb.set_trace() metodunu çağırmamız gerekir.
Ne zaman  kodda  pdb.set_trace() kodunu çağırırız o zaman o yerde kod kesilir ve o ana kara işletilen kodlar gösterilir.

l -> listeleme = tüm kodları listele
n -> next line =bir sonraki satıra geç
p -> print = satırı print et ekrana
c -> continue = kodu devam ettir
"""

import pdb

one ="one"
two ="two"

sonuc = one+two #output : onetwo

pdb.set_trace()

three ="three"

sonuc +=three

print(sonuc) #output : onetwothree