# kullaniciya secenek sun: ürün kaydet, ürünü güncelle, ürünleri listele, cikis
# ürün kaydet: kullanicidan ürün ismi ve fiyat bilgisi al ve alinan bilgileri bir dosyada kaydet
# ürün güncelle: alinan ürünün sadece fiyatini güncellesin
# ürün listele
# çıkış
def urun_kaydet():
    urun_adi=input("Bir urun adi giriniz: ")
    urun_fiyati=input("Urunun fiyatini giriniz: ")

    with open("urunler.txt", "a", encoding="utf-8") as file:
        file.write("Urun adi: "+ urun_adi  + " Urunun Fiyati: "+urun_fiyati+"\n")
       

def urun_fiyat_topla():
    with open("urunler.txt","r",encoding="utf-8") as file:
        for satir in file:
          satir=satir[:-1]  
          liste=satir.split(" ")
          toplam=0
    
          for i in satir: 
            fiyat=int(i[-1])
            toplam+=fiyat

        print("ToplamFiyat: "+ toplam)    
        



def urun_listele():
    with open("urunler.txt","r",encoding="utf-8") as file:
        content=file.read()
        print(content)



while True:
    secim=int(input("1-Urun Kaydet \n2-Urun toplam fiyat \n3-Urun Listele \n4-Cikis "))

    if secim==1:
        urun_kaydet()
    elif secim==2:
        urun_fiyat_topla()
    elif secim==3:
        urun_listele()
    else:
        break