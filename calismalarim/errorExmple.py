#liste = ["1","2","a5","10b","abc","10","50"]

# 1: Liste elemanları içindeki sayısal değerleri bulunuz

# for i in liste:
#     try:  
#          result=int(i)
#          print(result)
#     except ValueError:
#          continue



# for i in liste:
#     try:
#         result=int(i)
#         print(result)
#     except ValueError:
#         continue


# 2: Kullanıcı 'q' değerini girmedikçe aldığınız her inputun sayı 
# olduğundan emin olunuz aksi halde hata mesajı yazın.

# while True:
#     deger=input("bir deger girin: ")

#     if deger=='q': #quit
#         break
    
#     try:     
#         result=float(deger)  # deger harf 
#         print(f'sonuc:  {result}')
#         break
#     except Exception : 
#         print('girdigin deger sayisal bir deger degil!!!')
#         continue  
        

# while True:
#     deger=input("bir deger giriniz: ")
#     if deger=="q":
#         break

#     try:
#         result=float(deger)
#         print(f"sonuc:", result)
#         break
#     except Exception:
#         print("girdiğiniz deger sayisal bir deger degildir") 
#         continue

# girilen parola icinde turkce karakter hatasi verin
# psw = aşka
# def checkPassword(pws):
#     turkceKarakter='şçığüöİ'
    
#     for i in pws:
#         if i in turkceKarakter:
#             raise TypeError ("sifreniz turkce karakter icermemelidir!!!")
#     print("gecerli sifre ")


# try:
#     checkPassword(input("Bir sifre girin: "))
# except Exception as ex:
#     print(ex)

# eger bir exception varsa bunu try da yakala
    # programı durdurmasın except Exception yakala 
# try kod bir hata yoksa kod calısıyor 


# def chechPassword(psw):
#     turkceKarakterler='şiçüğöİ'

#     for i in psw:
#         if i in turkceKarakterler:
#             raise TypeError('Parola Turkce karakter icermemelidir.')
        
#     print('gecerli parola')

# try:
#     chechPassword(input('Lutfen bir parola giriniz: '))

# except Exception as ex:
#     print(ex)

#4 # 4: Faktöriyel fonksiyonu oluşturup fonksiyona gelen değer için
# hata mesajları verin. sayiya cevrilemiyorsa ve eksi degerse hata ver
# 4! 1*2*3*4
 
def faktoriyelHesapla(sayi):
    x=int(sayi)

    if x<0:
        raise ValueError('Negatif degerin faktoriyeli alinamaz!!! ')

    result=1

    for i in range(1,x+1):
        result*=i
    # result   i    x
    # 1        1    5
    # 1        2    5
    # 2        3    5
    # 6        4    5
    # 24       5    5

    print(result)

try:
    faktoriyelHesapla(input('Bir deger giriniz: '))

except Exception as ex:
    print(ex)