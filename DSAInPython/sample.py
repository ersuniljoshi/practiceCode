def multiarg(*args,**kwargs):
    for arg in args:
        print arg,
    for key,value in kwargs.items():
        print key,value,


l = [1,2,3,4,5,5,6]
multiarg(*l, k =1, l =2)