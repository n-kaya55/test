# try:
#     file=open("newfile.txt","r", encoding="utf-8")
#     print(file)
# except: 
#     print("dosya okuma hatası")
# finally:
#     file.close
#     print("dosya kapandi")

file=open("newfile.txt","r", encoding="utf-8")

# #for ile okuma
# for i in file:
#     print(i, end="")

#read fonksiyonu
# content=file.read()
# print("icerik bir")
# print(content)

# content2=file.read()
# print("icerik iki")
# print(content2)
# # ilk okumayı yaptıktan sonra imlec en sonra bekler ikinci kez read dersen tekrar okuma yapmaz boş döner

# content=file.read(3)
# print(content)

#readline() her seferinde bir satırı okur
# content=file.readline()
# print(content,end="")

#readlines()
# liste=file.readlines()
# print(liste)


file.close