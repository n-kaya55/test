class Student:
    def __init__(self, isim, soyisim,vize,final):
        self.isim= isim
        self.soyisim= soyisim
        self.vize=vize
        self.final=final
    
    def bilgi(self):
        print(f"öğrenci adı: {self.isim}, soyadı: {self.soyisim}")
    
   
    def ortalamaHesaplama(self):
        ortalama= (self.vize*0.4) + (self.final*0.6)
        return ortalama