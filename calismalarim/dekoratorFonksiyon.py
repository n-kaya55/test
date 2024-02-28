# def my_decarator(func):
#     def wrapper(name):
#         print("fonksiyondan öncesi islemler")
#         func(name)
#         print("fonksiyondan sonraki işlemler")
#     return wrapper

# @my_decarator
# def sayHello(name):
#     print("hello",name)

# sayHello("ali")
import math
import time

def calculate_time(func):
    def wrapper(*arg,**kwargs):
        start=time.time()
        time.sleep(1)
        func(*arg,**kwargs)
        finish=time.time()
        print("fonkstiyon "+str(finish-start) + " saniye surdu")
    return wrapper

@calculate_time
def usAlma(a,b):    
    print(math.pow(a,b))
   

@calculate_time
def faktoriyel(num):
    print(math.factorial(num))
 

usAlma(2,3)
faktoriyel(4)