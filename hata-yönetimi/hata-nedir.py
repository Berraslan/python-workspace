"""
error : önceden kalıbı tanımlanmış bir objedir - yani hata bir class'a mensuptur bir class'a mensup olduğu için bir kalıbı vardır yani nerden gelmiş; hangi hata türünü temsil ediyor vs ...

error handling : bir hata geldiğinde uygulamanın çalışması ve akışı bozlumasın diye kullanıcıya bir hata mesajı gösteririm ve bu gelen hatayı log'larım ve tekrar gelip bu hataya ne sebep olmuş onu araştırırım


"""

""" try : 
ve 

    except :

blokları  içine yazılan kodlar sayesinde eğer kod bir hata ile karşılaşırsa kullanıcıya error objesinin teknik kısmını vs gösterene kadar hata except: bloğuna düşer ve except içine yazılan kullanıcıya print edilir"""

# #try except kullanmadan karşılaşılan mesaj x ve y normalde int'dir ama eğer kullanıcı str bir değer girese kullanıcıya hata sınıfına ait error objesi fırlatılır biz bunu kullanıcını görmesini istemsezk try except kullanırız ve except içine kullanıcının gösrmesini istediğimizi yazarız
#
# x = int(input("x : "))
# y = int(input("y : "))
#
# sum = x+y
#
# print(sum)
#
#

#try except kullanarak aynı kodu yazalım
try :
    x = int(input("X: "))
    y = int(input("Y: "))

    sum = x+y
    print(sum)

except:
    print("yanlış tuşalamdan kaynaklı hata oluştu. Lütfen yeniden tuşlama yapınız")







