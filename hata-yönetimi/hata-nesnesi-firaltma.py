#kendi hata sınırlarımızı çizmek '.'n hata nesnesini raise ile oluştururuz
#eğer bizim tanımladığımız çerçevede birşeyler gerçekleşiyorsa buna uygun şu hata nesnesini fırlat demektir
#ValueError,TypeError gibi error'ler Exception sınıfından kalıtım(miras) almıştır.

x=10

if x>5:
    raise ValueError("x 5'den büyük olamaz")#tamamen farazi bizim ürettiğimiz bir hata ile karşılasın dediğimizde raise kullanırız. ValueError aslında Exception sınıfına aittir ve ValueError aslında Exception sınıfından kalıtım almıştır.
