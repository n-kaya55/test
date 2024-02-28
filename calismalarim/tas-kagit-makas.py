
# tas + makas = tas
# tas + kagit = kağit
# makas + kagit = makas
# berabere
# 

import random 

hak=5
kullanici_skore=0

while hak>0:
    hak-=1
    
    liste=['tas', 'makas','kagit']

    bilgisayar= liste[random.randint(0,2)]
    kullanici=input("Tas Kagit Makas ").lower()

    #beraber
    if not (kullanici=='tas' or kullanici=='makas' or kullanici=='kagit'):
        print("yanlis deger!!! ")

    else:
        if bilgisayar==kullanici:
            print(f"Bilgisayar: {bilgisayar} Berabere!!")

        elif bilgisayar=='tas':
            if kullanici=='makas':
                print(f"Bilgisayar: {bilgisayar} kullanici kaybetti")
            else:
                print(f"Bilgisayar: {bilgisayar} kullanici kazandi")
                kullanici_skore+=10
            
        elif bilgisayar=='kagit':
            if kullanici=='makas':
                print(f"Bilgisayar: {bilgisayar} kullanici kazandi")
                kullanici_skore+=10
            else:
                print(f"Bilgisayar: {bilgisayar} kullanici kaybetti")
                

        elif bilgisayar=='makas':
            if kullanici=='tas':
                print(f"Bilgisayar: {bilgisayar} kullanici kazandi")
                kullanici_skore+=10
            else:
                print(f"Bilgisayar: {bilgisayar} kullanici kaybetti")
                
    print(f" Kullanici skor:  {kullanici_skore}")