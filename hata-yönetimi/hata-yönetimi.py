while True:  # except bloğuna düşmediği sürece programı kesmeden çalıştır
    try:

        x = int(input("x : "))
        y = int(input("y : "))
        print(x / y)

    # burada hata'yı spesific olarak belirtirsek sadece o hatanın geldiği durumda ilgili except bloğu çalışır
    except (ZeroDivisionError,
            ValueError) as e:  # e adında bir değişken tanımlayıp hataları bu değişkenin içine loglayabiliriz ve herhanigi bir dosya'ya veya bir yere akatarabiliriz veya print() ile de bastırabiliriz
        print("x ve y sayı olmalıdır ve bu sayı sıfır olamaz")
        print(e)  # hatayı ekrana log'lar

        # en sona genel bir hata except bloğu koyarız ve tanımlanmamış hatalar buraya düşeer haa objesi fırlatmasındansa
    except Exception as e:  # Exception genel hata objesidir diğer yukarıdakiler özel hata objeleridir ama biz genel bir hata objesi tanımlayıp daha sonrasında da as e değişkeni ile loglarayak hata çeşitlerini de öğrenebiiliriz
        print("Bilinmeyen bir hata oluştu...")
    else: #else burada except bloklarının else'dir eğer exceptler çalışmazsa else içine grirlier ve program break ile sondlandırılır ki bu durumda hata ile karşılaşmadığını programın gösterir
        break
    finally:
        print("Finally bloğu çalıştı")#finally bloğu her halikarda çalışır bunu proragmın en sonunda açık kalan doyaların kapatılması işlemini de yapmak için kullanabiliriz

"""Not : except içinde farklı iki hatayı virgülle ayırıp tek bloğa bağlayabiliriz except ZeroDivisionError,ValueError diyerek o zaman tek bir bloğa düşer"""
"""Try ile eslse de kullanılabailir mesela bu kodda while döngüsü içinde eğer değerler doğru girilip except çalışmamışa program sonlanır ama except içine girilirse program çalışmaya devam edicektir"""