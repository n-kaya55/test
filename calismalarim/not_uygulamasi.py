def ortalamalari_oku():
    with open("sinav_notlari.txt","r",encoding="utf-8") as file:
        for satir in file:
           print(not_hesapla(satir))

def not_hesapla(satir):
    satir=satir[:-1]
    liste=satir.split(':')
    ogrenciAdi=liste[0]
    notlar=liste[1].split(',')
    not1=int(notlar[0])
    not2=int(notlar[1])
    not3=int(notlar[2])
    ortalama=(not1+not2+not3)/3

    if ortalama>=90 and ortalama <100:
        harf='AA'
    elif ortalama>=85 and ortalama<=89:
        harf='BB'
    elif ortalama>=65:
        harf='CC'
    else:
        harf='DD'

    return (ogrenciAdi + ":" + harf +"\n")

def not_gir():
    ad=input("ogrenci adi: ")
    soyad=input("ogrenci soyad: ")
    not1=input("ogrenci not1: ")
    not2=input("ogrenci not2: ")
    not3=input("ogrenci not3: ")

    with open("sinav_notlari.txt","a",encoding="utf-8") as file:
        file.write(ad +' '+soyad+':'+not1+','+not2+','+not3+'\n')



def notlari_kayitEt():
    with open("sinav_notlari.txt","r",encoding="utf-8") as file:
        liste=[]
        for i in file:
            liste.append(not_hesapla(i))
    
    with open("sonuclar", "w",encoding="utf-8") as file2:
        for i in liste:
            file2.write(i)


while True:
    islem=input("1-Notlari oku\n2-Not Gir\n3-Notlari Kaydet\n4-Cikis")

    if islem=='1':
        ortalamalari_oku()
    elif islem=='2':
        not_gir()
    elif islem=='3':
        notlari_kayitEt()
    else:
        break