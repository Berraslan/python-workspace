def all_Args_Func(a,b,c,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

all_Args_Func(10,20,30,40,50,60,34,"berra",yas=23,mail="yazilim@gmail.com")

#karşılık geldiği değerler;
#a -> 10
#b -> 20
#c -> 30
#args -> (40,50,60,34,"berra")
#kwargs -> yas=23,mail="yazilim@gmail.com" # çünkü bunlar key :value tipinde o yüzden kwargs yani dict