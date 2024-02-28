
#parola buyuk harf, kucuk harf, sayi, ? _ @ icerebilsin, bosluk iceremesin ve 8 karakterli olmalıdır


def checkPass(psw):
    if len(psw)==8:
        import re
        
        if not re.search("[A-Z]",psw):
            raise Exception("parola buyuk harf icermelidir!!")
        elif not re.search("[a-z]",psw):
            raise Exception("parola kucuk harf icermelidir.")
        elif not re.search("[0-9]",psw):
            raise Exception("parola sayi icermelidir")
        elif not re.search("[?_@]",psw):
            raise Exception("parola ? _ @ karakteri icermeli")
        elif re.search("[" "]", psw):
            raise Exception("sifre bosluk icermemelidir")
        else:
            print(" parola olusturuldu")


    else:
        print("parola 8 karakterli olmalidir!!")    






try:
   checkPass( input("parola giriniz: "))
except Exception:
    print(Exception)