class Teacher:

    def __init__(self, isim, soyisim, bolum,maas,zamOrani):
        self.isim= isim
        self.soyisim= soyisim
        self.bolum= bolum
        self.maas=maas
        self.zamOrani=zamOrani

    def bilgi(self):
        print(f"öğretmen Adı: {self.isim} Soyadı: {self.soyisim} Bölümü: {self.bolum}")

    def zamliMaas(self):
        zamliMaas= self.maas + (self.maas* self.zamOrani/100)
        return zamliMaas