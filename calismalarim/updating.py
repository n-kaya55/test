# r+ modu hem açma hem yazma hem okuma modu

# with open("newfile.txt","r+",encoding="utf-8") as file:
#     print(file.read())
#sayfa sonunda guncelleme yapar
# with open("newfile.txt", "a", encoding='utf-8') as file:
#     file.write("\nkaya ailesi")

# with open("newfile.txt","r+",encoding="utf-8") as file:
#      print(file.read())

# sayfa basında guncelleme yap
# with open("newfile.txt","r+",encoding="utf-8") as file:
#     content=file.read()
#     content="kaya ailesi\n"+content
#     file.seek(0) # indexi sıfırıncı indexe al
#     file.write(content)

# with open("newfile.txt", "r",encoding="utf-8") as file:
#     print(file.read())

#Sayfa ortasında yazı ekleme
with open("newfile.txt","r+",encoding="utf-8") as file:
    list=file.readlines()
    list.insert(1,"merve kaya\n")
    file.seek(0) #imlecin yerini değisigor nereye yazmak istersen oraya cek
    file.writelines(list) # writeline ile liste seklinde ekleme yapabilirsin for kullanmadan

with open("newfile.txt", "r",encoding="utf-8") as file:
     print(file.read())