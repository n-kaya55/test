#dosya acmak ve olusturmak open()
# open(dosya_adi,dosya_erişme_modu)
#dosya_erisme_modu dosyayı hangi amacla actıgımızı belirtir

#w: write yazma modu dosyayı konumda olusturur
# file=open("newfile.txt","w",encoding="utf-8")
# # file.write("nesibe kaya hoşoğlu")
# file.close()
# w ile acıtıgın dosyadaki bilgiler her seferinde silinir ustune ekleme yapmaz

#file=open("C:/Users/Nesibe/Desktop/newfile.txt","w")
#file.close

#a: append ekleme dosya konumda yoksa ekleme
# file=open("newfile.txt","a",encoding="utf-8")
# file.write("nesibe kaya \n")
# file.close

#x: create olusturma dosya zaten varsa hata verir
#dosya olsutur ama icine yazi eklemez
#file=open("newfile2.txt","x",encoding="utf-8")

#r read okuma varsyaılan dosya konumda yoksa hata verir

