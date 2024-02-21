# 1- İlk iki elemanı 1'e eşit olan, en az 20 elemanlı bir fibonacci serisini liste halinde oluşturan döngü yazalım.

elemanBir=1
elemanİki=1
geciciToplam=0 
print(elemanBir)

for i in range(1,5):
  
    print(elemanİki) 

    geciciToplam=elemanBir+elemanİki 
    elemanBir=elemanİki  
    elemanİki=geciciToplam 
    


# 2- Kullanıcıdan aldığı sayının mükemmel olup olmadığını söyleyen bir program yazınız.(Arş. Mükemmel sayı?)
# 6= 1 2 3 
sayi= int( input("Bir sayi girin: "))
a=0
for i in range(1,sayi):
     if ( sayi % i ==0):
        a=a+i
        
if (a==sayi):
     print (f'{sayi} sayi mükemmel sayidir')
else:
     print(f'{sayi} girdiginiz sayi mükemmel degildir')    

# 3- Kullanıcıdan girilen sayının EBOB ve EKOK'unu bulan programı yazınız.
#  12 15 |2
#  6  15 |2
#  3  15 |3
#  1  5  |5
#  1  1   

# 17 34 |2
# 17  17|17
 
sayiBir= int( input("Bir sayi girin: "))
sayiİki= int( input("Bir sayi girin: "))  

if ( sayiBir> sayiİki):
     kucukSayi=sayiİki
else:
    kucukSayi=sayiBir

for i in range(1,kucukSayi+1):
   if( sayiBir % i ==0)  and (sayiİki % i==0):
        ebob=i
        ekok= (sayiBir*sayiİki)//ebob  

print('ebob', ebob)
print('ekok',ekok)
 

# 4- Kullanıcıdan girilen sayının asal sayı olup olmadığını söyleyen bir program yazınız.
# asal sayi kendisine ve 1 e bol

sayi= int( input("Bir sayi girin: "))
i =2
# 17 1 2 3 4 5 ... 17 
# #8 2 
sayi= int( input("Bir sayi girin: "))
i =2
asalmi= True

if sayi==1 or sayi==0 :
    asalmi = False

while i<sayi:
    if sayi %i == 0:
        asalmi = False
        break
    else:
        i+= 1

if asalmi:
    print("sayi asaldir")
else:
    print("sayi asal degildir")
    


# 5- Kullanıcıdan girilen sayının asal çarpanlarını bulan bir program yazınız. 

# sayi= int( input("Bir sayi girin: "))

# i=2

# print ( sayi, "sayisinin asal carpanlari:")

# 17 17 1 
# 17 2 1 
# 17 3 2 
# 17 17 

# while i <= sayi:
#     if sayi %i==0:
#         print(i)
#         sayi //= i
#     else:
#         i+=1


# sayi = int(input("Bir sayı girin: "))

# i = 2
# print(sayi, "sayısının asal çarpanları:")
# while i <= sayi:
#     if sayi % i == 0:
#         print(i)
#         sayi //= i
#     else:
#         i += 1