#kendi hata sınırlarımızı çizmek
#eğer bizim tanımladığımız çerçevede birşeyler gerçekleşiyorsa buna uygun şu hata nesnesini fırlat demektir

x=10

if x>5:
    raise ValueError("x 5'den büyük olamaz")#tamamen farazi bizim ürettiğimiz bir hata ile karşılasın dediğimizde raise kullanırız. ValueError aslında Exception sınıfına aittir ve ValueError aslında Exception sınıfından kalıtım almıştır.
